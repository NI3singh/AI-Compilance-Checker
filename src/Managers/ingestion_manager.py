import os
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader

class FileIngestionManager:
    def __init__(self, upload_dir: str = "./uploaded_files"):
        """
        Initialize the FileIngestionManager with an upload directory.

        Args:
            upload_dir (str): Directory to save uploaded files.
        """
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)  
    
    async def save_file(self, file: UploadFile) -> str:
        """
        Save the uploaded file to the server.

        Args:
            file (UploadFile): The uploaded file object.

        Returns:
            str: Path where the file is saved.
        """
        file_path = os.path.join(self.upload_dir, file.filename)
        
        # Write the file asynchronously
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Trigger further processing
        self.process_file(file_path)
        
        return file_path

    def process_file(self, file_path: str):
        """
        Process the file (e.g., text extraction or other operations).

        Args:
            file_path (str): Path of the saved file.
        """
        print(f"Processing file: {file_path}")
        docs = self.extract_text_from_pdf(file_path)
        return docs

    def extract_text_from_pdf(self, pdf_path: str):
        """
        Extract text from the PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            list: Extracted documents.
        """
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        return docs