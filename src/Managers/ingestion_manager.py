import os
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader
from src.utils.text_utils import split_document

import sys
import os
# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.embedding_model import get_embedding
from src.utils.vector_store_server import store_embeddings_pinecone
from src.utils.vector_store_local import save_embeddings
from src.config.database import save_pdf_metadata
class FileIngestionManager:
    def __init__(self, upload_dir: str = "./uploaded_files"):
        
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)

    async def save_file(self, file: UploadFile) -> str:
        
        # Save the uploaded file
        file_path = os.path.join(self.upload_dir, file.name)
        with open(file_path, "wb") as f:
            if hasattr(file, "read"):  # For Streamlit's UploadedFile
                f.write(file.read())
            else:  # For FastAPI's UploadFile
                f.write(await file.read())
        
        # Save PDF metadata to PostgreSQL
        pdf_id = save_pdf_metadata(file.filename, file_path)
        
        # Extract text from PDF
        docs = self.extract_text_from_pdf(file_path)
        for doc in docs:
            store_embeddings_pinecone(pdf_id, doc.page_content)
            save_embeddings(pdf_id, doc.page_content)
        
        # Split text into chunks
        chunks = split_document(docs)
        
        # Generate embeddings
        embeddings = get_embedding(chunks)
        
        # Save embeddings locally
        save_embeddings(embeddings, "embeddings.pkl")
        
        # Store embeddings in Pinecone
        store_embeddings_pinecone(embeddings, [str(i) for i in range(len(embeddings))])
        
        return file_path

    def extract_text_from_pdf(self, pdf_path: str):
        
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        return docs