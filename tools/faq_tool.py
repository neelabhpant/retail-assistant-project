# tools/faq_tool.py
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from config.config import settings
import chromadb
from sentence_transformers import SentenceTransformer

class FAQInput(BaseModel):
    """Input model for the FAQTool."""
    query: str = Field(description="The user's question about a specific topic.")

class FAQTool(BaseTool):
    name: str = "FAQ Search Tool"
    description: str = "Searches the FAQ database to find answers to user questions."
    args_schema: Type[BaseModel] = FAQInput
    
    # Optimization: Initialize clients and models once
    _chroma_client: chromadb.HttpClient
    _embedding_model: SentenceTransformer
    _collection: chromadb.Collection

    def __init__(self):
        super().__init__()
        try:
            self._chroma_client = chromadb.HttpClient(host=settings.chroma_host, port=settings.chroma_port)
            self._embedding_model = SentenceTransformer(settings.embedding_model_name)
            self._collection = self._chroma_client.get_collection(name="faqs")
        except Exception as e:
            # Handle cases where ChromaDB might not be running during initialization
            print(f"Error initializing FAQTool: {e}")
            print("Please ensure ChromaDB is running and the 'faqs' collection has been embedded.")
            raise

    def _run(self, query: str) -> str:
        """The method that executes when the tool is called."""
        # 1. Embed the user's query
        query_embedding = self._embedding_model.encode(query).tolist()

        # 2. Query the collection
        try:
            results = self._collection.query(
                query_embeddings=[query_embedding],
                n_results=1  # We want the single best match
            )
        except Exception as e:
            return f"Error querying FAQ database: {e}"

        # 3. Process and return the result
        if results and results['documents'] and results['documents'][0]:
            return f"Relevant FAQ found:\n{results['documents'][0][0]}"
        else:
            return "No relevant information found in the FAQ database."