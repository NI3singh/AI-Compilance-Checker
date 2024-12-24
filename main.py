import os
import pickle
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain import hub
from langchain_groq import ChatGroq
def load_pdf(uploaded_file):
    """Load the PDF file."""
    start_time = time.time()
    with open("temp_pdf_file.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    docs = PyPDFLoader("temp_pdf_file.pdf").load()
    end_time = time.time()
    st.write(f"PDF loading time: {end_time - start_time:.2f} seconds")
    return docs

def split_document(docs):
    """Split the document into chunks."""
    start_time = time.time()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    end_time = time.time()
    st.write(f"Document splitting time: {end_time - start_time:.2f} seconds")
    return splits

def create_embeddings(splits):
    """Create and save embeddings if no existing embeddings are found, with a progress bar."""
    start_time = time.time()

    # Remove old embedding file if it exists
    if os.path.exists(embedding_file):
        st.write("Removing old embeddings file...")
        os.remove(embedding_file)

    st.write("Embedding the document...")

    # Setup progress bar
    progress_bar = st.progress(0)
    total_chunks = len(splits)

    model_name = "BAAI/bge-small-en"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    
    hf_embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
    )

    # Initialize an empty list to hold the documents and their embeddings
    embedded_docs = []

    # Embed chunks one by one and update progress bar
    for i, split in enumerate(splits):
        embedded_docs.append(split)  # Add the split to the list for embedding

        # Update the progress bar
        progress_percentage = (i + 1) / total_chunks
        progress_bar.progress(progress_percentage)

    # Create FAISS vectorstore after all chunks are embedded
    vectorstore = FAISS.from_documents(embedded_docs, hf_embeddings)

    # Save embeddings to disk
    with open(embedding_file, "wb") as f:
        pickle.dump(vectorstore, f)
    
    end_time = time.time()
    st.write(f"Embedding time: {end_time - start_time:.2f} seconds")
    return vectorstore