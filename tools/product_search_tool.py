# tools/product_search_tool.py
from typing import Type, List
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from config.config import settings
import chromadb
from sentence_transformers import SentenceTransformer

class ProductSearchInput(BaseModel):
    """Input model for the ProductSearchTool."""
    query: str = Field(description="The user's search query for a product.")

class ProductSearchTool(BaseTool):
    name: str = "Product Search Tool"
    description: str = "Searches the product catalog to find items relevant to the user's query."
    args_schema: Type[BaseModel] = ProductSearchInput

    _chroma_client: chromadb.HttpClient
    _embedding_model: SentenceTransformer
    _collection: chromadb.Collection

    def __init__(self):
        super().__init__()
        try:
            self._chroma_client = chromadb.HttpClient(host=settings.chroma_host, port=settings.chroma_port)
            self._embedding_model = SentenceTransformer(settings.embedding_model_name)
            self._collection = self._chroma_client.get_collection(name="products")
        except Exception as e:
            print(f"Error initializing ProductSearchTool: {e}")
            raise

    def _run(self, query: str) -> str:
        """The method that executes when the tool is called."""
        query_embedding = self._embedding_model.encode(query).tolist()

        try:
            # Query for the top 3 most relevant products
            results = self._collection.query(
                query_embeddings=[query_embedding],
                n_results=3
            )
        except Exception as e:
            return f"Error querying product database: {e}"

        if results and results['metadatas'] and results['metadatas'][0]:
            # Format the results into a readable string
            response_str = "Found relevant products:\n"
            for metadata in results['metadatas'][0]:
                response_str += (
                    f"- Name: {metadata['name']} (ID: {metadata['product_id']})\n"
                    f"  Category: {metadata['category']}\n"
                    f"  Price: ${metadata['price']}\n\n"
                )
            return response_str
        else:
            return "No relevant products found in the catalog."