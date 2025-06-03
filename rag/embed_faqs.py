# rag/embed_faqs.py
import chromadb
from sentence_transformers import SentenceTransformer
from config.config import settings

def embed_faqs():
    """
    Processes FAQs from a text file, generates embeddings, and stores them in ChromaDB.
    """
    print("Starting FAQ embedding process...")
    
    # 1. Initialize ChromaDB client and Sentence Transformer model
    try:
        chroma_client = chromadb.HttpClient(host=settings.chroma_host, port=settings.chroma_port)
        print("Successfully connected to ChromaDB.")
    except Exception as e:
        print(f"Failed to connect to ChromaDB: {e}")
        print("Please ensure the ChromaDB Docker container is running.")
        return

    embedding_model = SentenceTransformer(settings.embedding_model_name)
    print(f"SentenceTransformer model '{settings.embedding_model_name}' loaded.")

    # 2. Get or create the 'faqs' collection
    collection = chroma_client.get_or_create_collection(name="faqs")
    print("ChromaDB 'faqs' collection is ready.")

    # 3. Read and parse the FAQ data
    with open(settings.faqs_data_path, 'r') as f:
        # Split by '---' and filter out any empty strings
        faqs = [qa.strip() for qa in f.read().split('---') if qa.strip()]
    
    print(f"Found {len(faqs)} FAQs to process.")

    # 4. Generate embeddings and create documents to store
    # We use the full text of the Q&A as the document to be embedded and stored.
    embeddings = embedding_model.encode(faqs).tolist()
    ids = [f"faq_{i}" for i in range(len(faqs))]

    # 5. Add to the ChromaDB collection
    # This will update existing documents with the same ID or add new ones.
    collection.add(
        embeddings=embeddings,
        documents=faqs,
        ids=ids
    )

    print(f"\nSuccessfully embedded and stored {len(faqs)} FAQs in ChromaDB.")
    print("Total documents in collection:", collection.count())

if __name__ == "__main__":
    embed_faqs()