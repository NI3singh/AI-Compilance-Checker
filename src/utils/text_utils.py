from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_document(docs):
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits