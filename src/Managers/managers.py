import os
from fastapi import UploadFile

class FileIngestionManager:
    def __init__(self, upload_dir: str = "./uploaded_files"):
        """
        Initialize the FileIngestionManager with an upload directory.
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
        
        # Placeholder: Trigger further processing here if required
        self.process_file(file_path)
        
        return file_path

    def process_file(self, file_path: str):
        """
        Process the file (e.g., text extraction or other operations).

        Args:
            file_path (str): Path of the saved file.
        """
        print(f"Processing file: {file_path}")
        # Add placeholder logic here (e.g., call text extraction service)
