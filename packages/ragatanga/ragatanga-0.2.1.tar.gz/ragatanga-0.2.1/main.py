import asyncio
import os
import tempfile
from datetime import datetime
from typing import List, Tuple

import aiofiles
import faiss
import instructor
import numpy as np
import openai
import owlready2
import rdflib
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rdflib.plugins.sparql.parser import parseQuery
from contextlib import asynccontextmanager
from rdflib.plugins.sparql import prepareQuery
from loguru import logger
from owlready2 import sync_reasoner, sync_reasoner_pellet, get_ontology

###############################################################################
# CONFIGURATION
###############################################################################
# Update file paths to use Modal volume
OWL_FILE_PATH = "./ontology.ttl"
KBASE_FILE = "./knowledge_base.md"
KBASE_FAISS_INDEX_FILE = "./knowledge_base_faiss.index"
KBASE_EMBEDDINGS_FILE = "./knowledge_base_embeddings.npy"

# Update OpenAI client configuration
openai_client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")
openai_client.api_key = api_key

# Create patched client using from_openai
client = instructor.from_openai(openai_client)

# Embedding + Model Config
EMBED_MODEL            = "text-embedding-3-large"   # OpenAI embedding model
GPT_MODEL              = "gpt-4o"                   # or "gpt-4" if you have access
GPT_MODEL_REASONING    = "o3-mini"                  # or "o3-mini" if you have access
BATCH_SIZE             = 16                         # Batch size for embedding calls
TOP_K                  = 10                         # Retrieve top-K entries
DIMENSIONS             = 3072                       # Dimensionality for embedding model

###############################################################################
# FASTAPI MODELS
###############################################################################
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    retrieved_facts: List[str]
    answer: str
    

class Query(BaseModel):
    """
    A model for handling SPARQL query generation with validation.
    
    Examples:
    - user_query: "Find all exercises targeting biceps"
      reasoning_about_schema: "The ontology contains Exercise class with muscle groups"
      valid_sparql_query: "SELECT ?exercise WHERE { ?exercise a :Exercise ; :targets :Biceps }"
    """
    user_query: str = Field(..., description="The user's original query")
    reasoning_about_schema: str = Field(..., description="Reasoning about the schema and how it relates to the user's query")
    valid_sparql_query: str = Field(..., description="A valid SPARQL query")

    @field_validator("valid_sparql_query")
    def check_sparql_validity(cls, value):
        try:
            parseQuery(value)
        except Exception as e:
            raise ValueError(
                f"Invalid SPARQL query: {e}. Please prompt the LLM to generate a correct SPARQL query."
            ) from e
        return value

class SPARQLQueryGenerator(BaseModel):
    """
    A model for generating SPARQL queries using a plan-and-solve approach.
    """
    query_analysis: str = Field(..., description="Analysis of the natural language query and relevant ontology concepts")
    query_plan: str = Field(..., description="Step-by-step plan for constructing the SPARQL query")
    sparql_query: str = Field(..., description="The final SPARQL query with proper PREFIX declarations")

    @field_validator("sparql_query")
    def validate_sparql(cls, value):
        if "PREFIX" not in value:
            prefixes = """PREFIX : <http://www.semanticweb.org/ontologies/pratique-fitness/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""
            value = prefixes + value
        try:
            parseQuery(value)
        except Exception as e:
            raise ValueError(f"Invalid SPARQL query: {e}")
        return value

###############################################################################
# ONTOLOGY LOADING
###############################################################################
def materialize_inferences(onto):
    """Loads the ontology with rdflib first, then converts to a format Owlready2 can read."""
    try:
        # Load with rdflib first
        g = rdflib.Graph()
        g.parse(OWL_FILE_PATH, format='turtle')
        
        # Save as RDF/XML temporarily
        temp = tempfile.NamedTemporaryFile(suffix='.owl', delete=False)
        g.serialize(destination=temp.name, format='xml')
        temp.close()
        
        # Now load with Owlready2
        onto_path = "file://" + temp.name
        onto = get_ontology(onto_path).load()
        
        # Run reasoner
        with onto:
            sync_reasoner_pellet(infer_property_values=True)
        
        # Save materialized version with absolute path
        materialized_file = os.path.abspath(OWL_FILE_PATH.replace(".ttl", "_materialized.ttl"))
        g.serialize(destination=materialized_file, format='turtle')
        
        # Clean up temp file
        os.unlink(temp.name)
        
        return onto
        
    except Exception as e:
        logger.error(f"Failed to load ontology: {str(e)}")
        raise

async def load_ontology_schema() -> str:
    """
    Return the filtered ontology schema without individual declarations.
    Uses the materialized file if it exists and is nonempty.
    """
    materialized_file = OWL_FILE_PATH.replace(".ttl", "_materialized.ttl")
    
    # Use the materialized file if it exists and is non-empty
    if os.path.exists(materialized_file):
        async with aiofiles.open(materialized_file, "r", encoding="utf-8") as file:
            contents = await file.read()
        if not contents.strip():
            logger.warning("Materialized ontology is empty, falling back to original file.")
            async with aiofiles.open(OWL_FILE_PATH, "r", encoding="utf-8") as file:
                contents = await file.read()
    else:
        async with aiofiles.open(OWL_FILE_PATH, "r", encoding="utf-8") as file:
            contents = await file.read()
    
    logger.debug(f"Raw ontology schema length: {len(contents)}")
    
    # Define patterns to keep (schema-related)
    keep_patterns = [
        r'^@prefix',  # Prefix declarations
        r'^\s*:\w+\s+a\s+owl:Class\s*;',  # Class declarations
        r'^\s*:\w+\s+a\s+owl:(Object|Datatype)Property\s*;',  # Property declarations
        r'^\s*rdfs:domain\s+:',  # Property domains
        r'^\s*rdfs:range\s+:',  # Property ranges
        r'^\s*rdfs:subClassOf\s+:',  # Class hierarchy
    ]
    
    # Join patterns with OR
    import re
    pattern = re.compile('|'.join(keep_patterns))
    
    # Keep only schema-related lines and their associated labels/comments
    schema_lines = []
    current_block = []
    in_relevant_block = False
    
    for line in contents.splitlines():
        if pattern.search(line):
            if current_block:  # Save previous block if it was relevant
                if in_relevant_block:
                    schema_lines.extend(current_block)
                current_block = []
            in_relevant_block = True
            current_block.append(line)
        elif line.strip().startswith('rdfs:label') or line.strip().startswith('rdfs:comment'):
            if in_relevant_block:
                current_block.append(line)
        elif not line.strip():  # Empty line
            if in_relevant_block and current_block:
                schema_lines.extend(current_block)
                schema_lines.append('')
            current_block = []
            in_relevant_block = False
        elif line.strip().endswith(';') or line.strip().endswith('.'):
            if in_relevant_block:
                current_block.append(line)
    
    # Add any remaining block
    if in_relevant_block and current_block:
        schema_lines.extend(current_block)
    
    filtered_schema = '\n'.join(schema_lines)
    
    logger.debug(f"Filtered ontology schema length: {len(filtered_schema)}")
    
    if not schema_lines:
        raise ValueError("Filtered schema is empty - check keep patterns.")
    
    return filtered_schema

def load_ontology(owl_path: str):
    """Loads the ontology with rdflib first, then converts to a format Owlready2 can read."""
    try:
        # Load with rdflib first
        g = rdflib.Graph()
        g.parse(owl_path, format='turtle')
        
        # Save as RDF/XML temporarily
        temp = tempfile.NamedTemporaryFile(suffix='.owl', delete=False)
        g.serialize(destination=temp.name, format='xml')
        temp.close()
        
        # Now load with Owlready2
        onto_path = "file://" + temp.name
        onto = owlready2.get_ontology(onto_path).load()
        
        # Clean up
        os.unlink(temp.name)
        
        return onto
        
    except Exception as e:
        logger.error(f"Failed to load ontology: {str(e)}")
        raise

###############################################################################
# BUILD TEXT ENTRIES FROM ONTOLOGY
###############################################################################
def get_all_individuals(onto):
    """Collect all individuals, including those only available as instances of a class."""
    inds = set(onto.individuals())
    for cls in onto.classes():
        for instance in cls.instances():
            inds.add(instance)
    return list(inds)

def build_ontology_entries(onto):
    """
    Collect textual representations of classes, individuals, and properties
    from the loaded ontology.
    """
    entries = []
    idx = 0

    print("\nBuilding ontology entries...")

    # 1) Classes
    for cls in onto.classes():
        label = ", ".join(cls.label) if cls.label else cls.name
        doc = f"[CLASS]\nName: {cls.name}\nLabel: {label}\n"
        if cls.comment:
            doc += f"Comment: {', '.join(cls.comment)}\n"
        parents = [p.name for p in cls.is_a if p is not owlready2.Thing and hasattr(p, "name")]
        if parents:
            doc += f"subClassOf: {', '.join(parents)}\n"
        print(f"✓ Class: {cls.name}")
        entries.append({"id": idx, "text": doc.strip()})
        idx += 1

    # 2) Individuals
    for indiv in get_all_individuals(onto):
        doc = f"[INDIVIDUAL]\nName: {indiv.name}\n"
        if hasattr(indiv, 'label') and indiv.label:
            doc += f"Label: {', '.join(indiv.label)}\n"
        if hasattr(indiv, 'comment') and indiv.comment:
            doc += f"Comment: {', '.join(indiv.comment)}\n"
        types = [t.name for t in indiv.is_a if hasattr(t, "name")]
        if types:
            doc += "rdf:type: " + ", ".join(types) + "\n"
            
        # Get properties more safely
        properties = [p for p in onto.properties() if not p.name.startswith('_')]
        for prop in properties:
            try:
                if prop in indiv.get_properties():
                    values = prop[indiv]
                    if isinstance(values, list):
                        doc += f"{prop.name}: {', '.join(str(v) for v in values)}\n"
                    else:
                        doc += f"{prop.name}: {str(values)}\n"
            except Exception:
                # Skip problematic properties
                continue
                
        print(f"✓ Individual: {indiv.name}")
        entries.append({"id": idx, "text": doc.strip()})
        idx += 1

    # 3) Properties
    for prop in onto.properties():
        doc = f"[PROPERTY]\nName: {prop.name}\n"
        if prop.label:
            doc += f"Label: {', '.join(prop.label)}\n"
        if prop.comment:
            doc += f"Comment: {', '.join(prop.comment)}\n"
        if prop.domain:
            dom_list = [d.name for d in prop.domain if hasattr(d, "name")]
            if dom_list:
                doc += "Domain: " + ", ".join(dom_list) + "\n"
        if prop.range:
            rng_list = [r.name for r in prop.range if hasattr(r, "name")]
            if rng_list:
                doc += "Range: " + ", ".join(rng_list) + "\n"
        print(f"✓ Property: {prop.name}")
        entries.append({"id": idx, "text": doc.strip()})
        idx += 1

    print(f"✓ Total entries: {len(entries)}")
    return entries

###############################################################################
# EMBEDDING UTILS (Async versions)
###############################################################################
async def embed_texts_in_batches(texts: List[str], batch_size: int = 16) -> np.ndarray:
    """
    Embed a list of strings in batches. Returns a numpy array of shape (N, D).
    Uses the sync OpenAI embeddings call wrapped in asyncio.to_thread.
    """
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        # Wrap the synchronous embedding call using asyncio.to_thread
        response = await asyncio.to_thread(openai.embeddings.create, input=batch, model=EMBED_MODEL)
        for j in range(len(batch)):
            emb = response.data[j].embedding
            all_embeddings.append(emb)
    return np.array(all_embeddings, dtype=np.float32)

def build_faiss_index(embeddings: np.ndarray) -> Tuple[faiss.IndexFlatIP, np.ndarray]:
    """
    Build a FAISS index for inner product (cosine if we normalize vectors).
    """
    # Normalize embeddings for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings_norm = embeddings / (norms + 1e-10)

    index = faiss.IndexFlatIP(DIMENSIONS)
    index.add(x=embeddings_norm) # type: ignore
    return index, embeddings_norm

def save_faiss_index(index, index_file: str, embeddings: np.ndarray, embed_file: str):
    faiss.write_index(index, index_file)
    np.save(embed_file, embeddings)
    print(f"FAISS index saved to {index_file}, embeddings to {embed_file}")

def load_faiss_index(index_file: str, embed_file: str):
    index = faiss.read_index(index_file)
    embeddings = np.load(embed_file)
    return index, embeddings

###############################################################################
# INITIALIZATION
###############################################################################
print("=== RAGATANGA: Initializing Ontology RAG ===")

def debug_print_individuals(onto):
    """Print all individuals in the ontology to verify parsing."""
    print("\nVerifying ontology individuals...")
    for individual in onto.individuals():
        print(f"✓ {individual.name}")

def debug_print_classes(onto):
    """Print all classes and their instances in the ontology."""
    print("\nVerifying ontology classes...")
    for cls in onto.classes():
        print(f"✓ {cls.name}")

def debug_unidade_class(onto):
    """Debug the Unidade class and its instances."""
    print("\nVerifying Unidade class...")
    unidade_class = onto.search_one(iri="*Unidade")
    if not unidade_class:
        print("! Unidade class not found")
        return
    print(f"✓ Found Unidade class with {len(list(unidade_class.instances()))} instances")

# Load your ontology (for SPARQL queries, debugging, etc.)
try:
    # First try to materialize the ontology
    onto = materialize_inferences(OWL_FILE_PATH)
    with onto:
        sync_reasoner_pellet(infer_property_values=True)
    debug_print_individuals(onto)
    debug_print_classes(onto)
    debug_unidade_class(onto)
except Exception as e:
    print(f"Warning: Could not load ontology file {OWL_FILE_PATH}. Error: {e}")
    onto = None

# FastAPI app initialization should come before the startup event
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Materialize inferences first
    materialize_inferences(onto)
    
    # Rest of your existing initialization code
    global kbase_entries, kbase_index, kbase_embeddings_np
    
    if not os.path.exists(KBASE_FILE):
        print(f"Warning: Knowledge base file {KBASE_FILE} not found. Starting with empty knowledge base.")
        kbase_entries = []
        kbase_index = None
        kbase_embeddings_np = None
        yield
    else:
        # Load knowledge base content
        with open(KBASE_FILE, "r", encoding="utf-8") as file:
            kbase_content = file.read()
        kbase_entries = [chunk.strip() for chunk in kbase_content.split("\n\n") if chunk.strip()]

        # Build or load FAISS index
        if os.path.exists(KBASE_FAISS_INDEX_FILE) and os.path.exists(KBASE_EMBEDDINGS_FILE):
            print("Loading existing FAISS index and embeddings for knowledge base...")
            kbase_index, kbase_embeddings_np = load_faiss_index(KBASE_FAISS_INDEX_FILE, KBASE_EMBEDDINGS_FILE)
        else:
            print("Embedding knowledge base entries in batches...")
            kbase_embeddings_np = await embed_texts_in_batches(kbase_entries, BATCH_SIZE)
            kbase_index, kbase_embeddings_np = build_faiss_index(np.asarray(kbase_embeddings_np))
            save_faiss_index(kbase_index, KBASE_FAISS_INDEX_FILE, kbase_embeddings_np, KBASE_EMBEDDINGS_FILE)

        print(f"=== Ontology RAG System ready with SPARQL on {OWL_FILE_PATH} and semantic search on {KBASE_FILE} ===")
        yield

    # Optional shutdown code can be placed here if required.

app = FastAPI(
    title="RAGATANGA: Ontology RAG",
    description="RAGATANGA: Ontology RAG - Hybrid Retrieval API",
    version="1.0.0",
    lifespan=lifespan
)

###############################################################################
# QUERY FUNCTIONS (Async versions)
###############################################################################
async def get_query_embedding(query: str) -> np.ndarray:
    """Embed and normalize a single query string."""
    response = await asyncio.to_thread(openai.embeddings.create, input=[query], model=EMBED_MODEL)
    emb = np.array(response.data[0].embedding, dtype=np.float32)
    norm = np.linalg.norm(emb)
    return emb / (norm + 1e-10)

async def retrieve_top_k(query: str, k: int) -> List[str]:
    """
    Use FAISS to find top-k most similar knowledge base entries.
    """
    q_emb = (await get_query_embedding(query)).reshape(1, -1)
    def search_index():
        return kbase_index.search(q_emb, k) # type: ignore
    distances, indices = await asyncio.to_thread(search_index)
    return [kbase_entries[i] for i in indices[0].tolist()]

@logger.catch
async def generate_sparql_query(query: str) -> str:
    # Read the OWL schema and filter out individuals
    with open(OWL_FILE_PATH, "r", encoding="utf-8") as file:
        owl_schema = file.read()
        
    schema_lines = [
        line for line in owl_schema.splitlines()
        if not any(x in line.lower() for x in [
            "a owl:namedindividual",
            "rdf:type owl:namedindividual",
            ":individual"
        ])
    ]
    filtered_schema = "\n".join(schema_lines)
    
    system_prompt = (
        "You are a SPARQL and ontology query expert. Here's the OWL schema (classes and properties only):\n"
        f"{filtered_schema}\n\n"
        "Based on this schema, create a SPARQL query that returns structured information "
        "to answer the following question. Follow these guidelines:\n\n"
        "1. Always include necessary PREFIX declarations\n"
        "2. Use DISTINCT to avoid duplicate results\n"
        "3. When querying instances:\n"
        "   - Include rdfs:label for human-readable names\n"
        "   - Include rdfs:comment for descriptions when available\n"
        "   - Include relevant object properties linking to other instances\n"
        "   - Include relevant datatype properties for literal values\n"
        "4. Use OPTIONAL for potentially missing properties\n"
        "5. Add appropriate filters (e.g., language, numeric comparisons) when needed\n"
        "6. Order results by relevant criteria (e.g., numeric values, labels)\n"
        "7. Use subqueries or aggregates if needed for complex relationships\n\n"
        "Common prefixes:\n"
        "PREFIX : <http://www.semanticweb.org/ontologies/>\n"
        "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
        "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
        "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    )
    
    user_message = (
        f"Question: {query}\n\n"
        "Generate a SPARQL query following the guidelines above. "
        "Analyze the schema first to identify:\n"
        "1. Relevant classes and their relationships\n"
        "2. Properties that connect these classes\n"
        "3. Properties that hold the requested information\n"
        "Then construct a query that will return complete and accurate results."
    )
    
    try:
        response = await asyncio.to_thread(
            client.create,
            max_retries=3,
            response_model=Query,
            model=GPT_MODEL_REASONING,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
        )
        generated_query = response.valid_sparql_query
    except Exception as e:
        logger.warning(f"Failed to generate query: {e}. Using default query.")
        generated_query = """
    PREFIX : <http://www.semanticweb.org/ontologies/pratique-fitness/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?label ?typeLabel ?address ?planName ?planPrice ?planDescription WHERE {
        :unidade_guarani rdfs:label ?label ;
                        :hasType ?type ;
                        :hasAddress ?address ;
                        :hasPlans ?plan .
        ?type rdfs:label ?typeLabel .
        ?plan rdfs:label ?planName ;
             :hasPrice ?planPrice .
        OPTIONAL { ?plan rdfs:comment ?planDescription }
    }
    ORDER BY ?planPrice
    """
    
    print("Generated SPARQL Query:\n", generated_query)
    return generated_query

async def execute_sparql_query(sparql_query: str) -> List[str]:
    """Execute a SPARQL query against the materialized ontology."""
    try:
        prepared_query = prepareQuery(sparql_query)
    except Exception as e:
        return [f"Invalid SPARQL syntax: {str(e)}"]

    def run_query():
        g = rdflib.Graph()
        try:
            # Use materialized ontology file with absolute path
            materialized_file = os.path.abspath(OWL_FILE_PATH.replace(".ttl", "_materialized.ttl"))
            if not os.path.exists(materialized_file):
                logger.warning(f"Materialized file not found at {materialized_file}, falling back to original ontology")
                materialized_file = OWL_FILE_PATH
                
            logger.info(f"Loading ontology from: {materialized_file}")
            g.parse(materialized_file, format='turtle')
            logger.debug(f"Using ontology for query: {sparql_query}")
            
            # Execute the query
            results = g.query(prepared_query)
            logger.debug(f"Query results: {list(results)}")

            output_texts = []
            for row in results:
                if isinstance(row, bool):
                    output_texts.append(str(row))
                elif hasattr(row, '__iter__'):
                    row_values = []
                    for val in row:
                        if isinstance(val, rdflib.URIRef):
                            val_str = str(val).split('#')[-1].split('/')[-1]
                        else:
                            val_str = str(val)
                        if val_str.strip():
                            row_values.append(val_str)
                    if row_values:
                        output_texts.append(", ".join(row_values))
                else:
                    output_texts.append(str(row))

            return output_texts if output_texts else ["No matching results found in the ontology"]

        except Exception as e:
            logger.error(f"Error executing SPARQL query: {str(e)}")
            return [f"Error executing SPARQL query: {str(e)}"]

    try:
        return await asyncio.to_thread(run_query)
    except Exception as e:
        logger.error(f"SPARQL query execution error: {str(e)}")
        return [f"SPARQL query execution error: {str(e)}"]

async def hybrid_retrieve(query: str, top_k: int = TOP_K) -> List[str]:
    """
    Hybrid retrieval combining SPARQL and semantic search results.
    """
    print(f"Debug: Processing query: {query}")
    
    # Generate and execute SPARQL query
    try:
        sparql_query = await generate_sparql_query(query)
        print(f"Debug: Generated SPARQL query: {sparql_query}")
        sparql_results = await execute_sparql_query(sparql_query)
        print(f"Debug: SPARQL results: {sparql_results}")
    except Exception as e:
        print(f"Debug: SPARQL error: {str(e)}")
        sparql_results = ["Error executing SPARQL query"]

    # Perform semantic search
    try:
        semantic_results = await retrieve_top_k(query, top_k)
    except Exception as e:
        print(f"Debug: Semantic search error: {str(e)}")
        semantic_results = []

    # Merge and return results
    return merge_results(sparql_results, semantic_results)

def merge_results(sparql_results: List[str], semantic_results: List[str]) -> List[str]:
    """
    Merge and annotate results from SPARQL and semantic search.
    Duplicates are deduplicated based on their text (stripped), and their sources are combined.
    """
    merged = {}
    
    # Handle "No results found" case explicitly
    if sparql_results == ["No results found"]:
        merged["No structured data found in the ontology"] = {"SPARQL"}
    else:
        for fact in sparql_results:
            key = fact.strip()
            merged.setdefault(key, set()).add("SPARQL")
            
    for fact in semantic_results:
        key = fact.strip()
        merged.setdefault(key, set()).add("Semantic")
        
    combined = []
    for fact, sources in merged.items():
        source_str = ", ".join(sorted(sources))
        combined.append(f"{source_str}: {fact}")
    return combined

async def generate_answer(query: str, retrieved_texts: List[str]) -> QueryResponse:
    """
    Prompt the LLM with the user query and the retrieved ontology facts.
    """
    system_prompt = (
        "Você é um assistente especializado da academia Pratique Fitness. "
        "Você possui fatos da ontologia (em português) que podem ajudar a responder perguntas. "
        "Ao responder sobre unidades:\n"
        "1. Liste o nome e endereço da unidade\n"
        "2. Mencione o tipo da unidade (Slim, Premium, etc)\n"
        "3. Liste todos os planos disponíveis, incluindo:\n"
        "   - Nome do plano\n"
        "   - Preço\n"
        "   - Descrição (se disponível)\n"
        "4. Organize a resposta em seções claras\n"
        "5. Use formatação em markdown para melhor legibilidade\n\n"
        "Responda com precisão, usando apenas as informações relevantes dos fatos fornecidos. "
        "Se não souber algo, diga que não tem certeza."
    )

    context_block = "\n\n".join([f"FACT {i+1}: {txt}" for i, txt in enumerate(retrieved_texts)])
    user_message = (
        f"Query do usuário: {query}\n\n"
        f"Fatos da ontologia:\n{context_block}\n\n"
        "Por favor, elabore uma resposta estruturada em português, "
        "organizando todas as informações disponíveis sobre a unidade e seus planos. "
        "Use markdown para formatar a resposta."
    )

    response = await asyncio.to_thread(
        client.create,
        max_retries=3,
        response_model=QueryResponse,
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.2
    )

    # Format the answer if it doesn't already include markdown
    if not any(marker in response.answer for marker in ['##', '#', '*', '-']):
        facts = response.retrieved_facts
        formatted_answer = "## Unidade Pratique Fitness\n\n"
        
        # Extract unit info
        unit_info = next((f for f in facts if "label" in f.lower() and "address" in f.lower()), "")
        if unit_info:
            formatted_answer += "### Informações Gerais\n"
            formatted_answer += unit_info + "\n\n"
        
        # Extract plans
        plans = [f for f in facts if "plan" in f.lower() and "price" in f.lower()]
        if plans:
            formatted_answer += "### Planos Disponíveis\n"
            for plan in plans:
                formatted_answer += f"* {plan}\n"
        
        response.answer = formatted_answer

    return response

###############################################################################
# FASTAPI APP
###############################################################################
@app.post("/query", response_model=QueryResponse)
async def handle_query(req: QueryRequest):
    user_query = req.query

    # Hybrid retrieval: combine SPARQL and semantic search results
    hybrid_facts = await hybrid_retrieve(user_query, TOP_K)
    logger.debug("Hybrid facts: {facts}", facts=hybrid_facts)

    
    # Generate the final answer using the combined ontology facts
    answer = await generate_answer(user_query, hybrid_facts)

    return answer

@app.post("/upload/ontology")
async def upload_ontology(file: UploadFile):
    """Upload a new ontology file (.ttl or .owl)"""
    if not file.filename or not file.filename.endswith(('.ttl', '.owl')):
        raise HTTPException(status_code=400, detail="File must be .ttl or .owl")
    
    try:
        contents = await file.read()
        # Decode and encode with explicit UTF-8 handling
        try:
            decoded_contents = contents.decode('utf-8')
        except UnicodeDecodeError:
            # Fallback to latin-1 if UTF-8 fails
            decoded_contents = contents.decode('latin-1')
        
        # Write with explicit UTF-8 encoding
        async with aiofiles.open(OWL_FILE_PATH, "w", encoding='utf-8') as out_file:
            await out_file.write(decoded_contents)
            
        # Reload the ontology in a separate thread
        global onto
        onto = await asyncio.to_thread(load_ontology, OWL_FILE_PATH)
        
        return {"message": "Ontology uploaded and loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading ontology: {str(e)}")

@app.get("/download/ontology")
async def download_ontology():
    """Download the current ontology file"""
    if not os.path.exists(OWL_FILE_PATH):
        raise HTTPException(status_code=404, detail="Ontology file not found")
    return FileResponse(OWL_FILE_PATH)

@app.post("/upload/kb")
async def upload_knowledge_base(file: UploadFile):
    """Upload a new knowledge base markdown file"""
    if not file.filename or not file.filename.endswith('.md'):
        raise HTTPException(status_code=400, detail="File must be .md")
    
    try:
        contents = await file.read()
        # Decode and encode with explicit UTF-8 handling
        try:
            decoded_contents = contents.decode('utf-8')
        except UnicodeDecodeError:
            # Fallback to latin-1 if UTF-8 fails
            decoded_contents = contents.decode('latin-1')
        
        # Write with explicit UTF-8 encoding
        async with aiofiles.open(KBASE_FILE, "w", encoding='utf-8') as out_file:
            await out_file.write(decoded_contents)
            
        # Rebuild the FAISS index
        global kbase_entries, kbase_index, kbase_embeddings_np
        kbase_entries = [chunk.strip() for chunk in decoded_contents.split("\n\n") if chunk.strip()]
        kbase_embeddings_np = await embed_texts_in_batches(kbase_entries, BATCH_SIZE)
        # Wrap the FAISS index building in a thread
        def build_index():
            return build_faiss_index(np.asarray(kbase_embeddings_np))
        kbase_index, kbase_embeddings_np = await asyncio.to_thread(build_index)
        await asyncio.to_thread(save_faiss_index, kbase_index, KBASE_FAISS_INDEX_FILE, kbase_embeddings_np, KBASE_EMBEDDINGS_FILE)
        
        return {"message": "Knowledge base uploaded and indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading knowledge base: {str(e)}")

@app.get("/download/kb")
async def download_knowledge_base():
    """Download the current knowledge base markdown file"""
    if not os.path.exists(KBASE_FILE):
        raise HTTPException(status_code=404, detail="Knowledge base file not found")
    return FileResponse(KBASE_FILE)

def get_ontology_statistics(onto) -> dict:
    """Gather comprehensive statistics about the ontology."""
    classes = list(onto.classes())
    individuals = list(get_all_individuals(onto))
    properties = list(onto.properties())
    
    # Count instances per class
    class_instances = {}
    for cls in classes:
        instances = list(cls.instances())
        if instances:
            class_instances[cls.name] = len(instances)
    
    # Analyze properties
    property_stats = {}
    for prop in properties:
        if hasattr(prop, 'name'):
            domain = [d.name for d in prop.domain if hasattr(d, "name")] if prop.domain else []
            range_vals = [r.name for r in prop.range if hasattr(r, "name")] if prop.range else []
            property_stats[prop.name] = {
                "type": prop.__class__.__name__,
                "domain": domain,
                "range": range_vals,
                "label": list(prop.label) if prop.label else [],
                "comment": list(prop.comment) if prop.comment else []
            }
    
    # Individual property usage
    individual_properties = {}
    for ind in individuals:
        if hasattr(ind, 'name'):
            props = {}
            for prop in onto.properties():
                try:
                    if prop in ind.get_properties():
                        values = prop[ind]
                        if values:
                            props[prop.name] = [str(v) for v in values] if isinstance(values, list) else [str(values)]
                except Exception:
                    continue
            if props:
                individual_properties[ind.name] = props

    return {
        "statistics": {
            "total_classes": len(classes),
            "total_individuals": len(individuals),
            "total_properties": len(properties),
            "classes_with_instances": len(class_instances)
        },
        "classes": {
            cls.name: {
                "label": list(cls.label) if cls.label else [],
                "comment": list(cls.comment) if cls.comment else [],
                "instance_count": class_instances.get(cls.name, 0),
                "parents": [p.name for p in cls.is_a if p is not owlready2.Thing and hasattr(p, "name")]
            } for cls in classes if hasattr(cls, 'name')
        },
        "properties": property_stats,
        "individuals": {
            ind.name: {
                "types": [t.name for t in ind.is_a if hasattr(t, "name")],
                "label": list(ind.label) if hasattr(ind, 'label') and ind.label else [],
                "comment": list(ind.comment) if hasattr(ind, 'comment') and ind.comment else [],
                "properties": individual_properties.get(ind.name, {})
            } for ind in individuals if hasattr(ind, 'name')
        }
    }

@app.get("/describe_ontology")
async def describe_ontology():
    """
    Get a comprehensive description of the loaded ontology.
    """
    try:
        description = await asyncio.to_thread(get_ontology_statistics, onto)
        description["metadata"] = {
            "file_path": OWL_FILE_PATH,
            "file_size": os.path.getsize(OWL_FILE_PATH),
            "last_modified": datetime.fromtimestamp(os.path.getmtime(OWL_FILE_PATH)).isoformat(),
            "format": "Turtle" if OWL_FILE_PATH.endswith('.ttl') else "OWL"
        }
        return description
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error describing ontology: {str(e)}"
        )

if __name__ == "__main__":
    # This is only for local development
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)