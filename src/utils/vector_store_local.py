import pickle

def save_embeddings(vectorstore, embedding_file="embeddings.pkl"):
    """
    Save embeddings to a local file.

    Args:
        vectorstore (FAISS): FAISS vector store.
        embedding_file (str): Path to save the embeddings.
    """
    with open(embedding_file, "wb") as f:
        pickle.dump(vectorstore, f)