from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import faiss as FAISS

def create_embeddings(splits):
    """
    Create embeddings for the document chunks.

    Args:
        splits (list): List of document chunks.

    Returns:
        FAISS: FAISS vector store with embeddings.
    """
    model_name = "BAAI/bge-small-en"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    
    hf_embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
    )

    vectorstore = FAISS.from_documents(splits, hf_embeddings)
    return vectorstore