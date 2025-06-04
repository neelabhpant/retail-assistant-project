# config/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """
    A class to manage application settings using Pydantic.
    It loads environment variables and provides them as typed attributes.
    """
    # OpenAI API Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    openai_model_name: str = "gpt-4o"

    # Embedding Model Configuration
    embedding_model_name: str = "all-MiniLM-L6-v2"

    # Data File Paths
    products_data_path: str = "data/products.csv"
    orders_data_path: str = "data/orders.json"
    faqs_data_path: str = "data/faqs.txt"

    # ChromaDB Configuration
    chroma_host: str = "localhost"
    chroma_port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()