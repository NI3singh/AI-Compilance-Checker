from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_document(docs):
    """
    Split the document into chunks.

    Args:
        docs (list): List of documents to split.

    Returns:
        list: List of document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits