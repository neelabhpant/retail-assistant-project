# rag/embed_products.py
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from config.config import settings

def embed_products():
    """
    Processes product data from a CSV file, generates embeddings for product descriptions,
    and stores them in ChromaDB.
    """
    print("Starting product embedding process...")

    try:
        chroma_client = chromadb.HttpClient(host=settings.chroma_host, port=settings.chroma_port)
        embedding_model = SentenceTransformer(settings.embedding_model_name)
        print("Successfully connected to ChromaDB and loaded model.")
    except Exception as e:
        print(f"Failed to initialize clients: {e}")
        return

    collection = chroma_client.get_or_create_collection(name="products")
    print("ChromaDB 'products' collection is ready.")

    try:
        df = pd.read_csv(settings.products_data_path)
        print(f"Found {len(df)} products to process from {settings.products_data_path}.")
    except FileNotFoundError:
        print(f"Error: Product data file not found at {settings.products_data_path}")
        return

    documents = []
    metadatas = []
    ids = []
    for index, row in df.iterrows():
        doc = f"Product Name: {row['name']}, Category: {row['category']}, Description: {row['description']}"
        documents.append(doc)
        
        metadatas.append({
            "product_id": row["product_id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        })
        
        ids.append(f"product_{row['product_id']}")

    embeddings = embedding_model.encode(documents).tolist()
    collection.add(
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"\nSuccessfully embedded and stored {len(df)} products in ChromaDB.")
    print("Total documents in collection:", collection.count())


if __name__ == "__main__":
    embed_products()