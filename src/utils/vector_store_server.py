import pinecone

def store_embeddings_pinecone(embeddings, ids, index_name="compliance-checker"):
    """
    Store embeddings in a hosted vector database (Pinecone).

    Args:
        embeddings (list): List of embeddings.
        ids (list): List of IDs corresponding to embeddings.
        index_name (str): Name of the Pinecone index.
    """
    pinecone.init(api_key="your-api-key", environment="us-west1-gcp")
    index = pinecone.Index(index_name)
    index.upsert(vectors=zip(ids, embeddings))