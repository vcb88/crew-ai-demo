# memory_tools.py
from crewai import Tool
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
import os

# Initialize ChromaDB client
# This will create a 'chroma_db' directory to store the database
client = PersistentClient(path="./chroma_db")

# Define an embedding function.
# For a local setup, you might use a SentenceTransformer model.
# For simplicity and to avoid new large downloads, we'll use a mock embedding function for now.
# In a real scenario, you'd replace this with a proper embedding model.
# Example for OpenAI embeddings (requires OPENAI_API_KEY):
# openai_ef = embedding_functions.OpenAIEmbeddingFunction(
#     api_key=os.environ.get("OPENAI_API_KEY"),
#     model_name="text-embedding-ada-002"
# )
# For a local model, you'd need to set up a local embedding server or use a library like sentence-transformers
# For now, a simple mock:
class MockEmbeddingFunction:
    def __call__(self, texts):
        # Simple mock: returns a dummy embedding for each text
        return [[1.0] * 1536 for _ in texts] # OpenAI's ada-002 has 1536 dimensions

mock_ef = MockEmbeddingFunction()

# Get or create a collection for memories
memories_collection = client.get_or_create_collection(
    name="personal_assistant_memories",
    embedding_function=mock_ef # Use the mock embedding function
)

@Tool
def store_memory(text: str, id: str, metadata: dict = None):
    """
    Stores a piece of information (memory) in the vector database.
    Args:
        text (str): The content of the memory to store.
        id (str): A unique identifier for this memory.
        metadata (dict, optional): Optional metadata associated with the memory.
    """
    try:
        memories_collection.add(
            documents=[text],
            metadatas=[metadata if metadata else {}],
            ids=[id]
        )
        return f"Memory '{id}' stored successfully."
    except Exception as e:
        return f"Failed to store memory '{id}': {e}"

@Tool
def retrieve_memory(query: str, n_results: int = 3):
    """
    Retrieves relevant memories from the vector database based on a query.
    Args:
        query (str): The query to search for relevant memories.
        n_results (int): The number of top relevant memories to retrieve.
    Returns:
        list: A list of dictionaries, each containing 'document' (the memory text) and 'distance'.
    """
    try:
        results = memories_collection.query(
            query_texts=[query],
            n_results=n_results
        )
        retrieved_memories = []
        if results and results['documents']:
            for i, doc in enumerate(results['documents'][0]):
                retrieved_memories.append({
                    "document": doc,
                    "distance": results['distances'][0][i]
                })
        return retrieved_memories
    except Exception as e:
        return f"Failed to retrieve memories: {e}"
