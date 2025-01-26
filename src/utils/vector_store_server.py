import pinecone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def store_embeddings_pinecone(embeddings, ids, index_name="compliance-checker"):
    """
    Store embeddings in Pinecone.

    Args:
        embeddings (list): List of embedding vectors.
        ids (list): List of IDs corresponding to the embeddings.
        index_name (str): Name of the Pinecone index.
    """
    # Initialize Pinecone
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENVIRONMENT")
    )

    # Connect to the Pinecone index
    index = pinecone.Index(index_name)

    # Upsert embeddings into Pinecone
    index.upsert(vectors=zip(ids, embeddings))