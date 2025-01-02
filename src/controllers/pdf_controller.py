from fastapi import APIRouter, UploadFile, HTTPException
from Managers.ingestion_manager import FileIngestionManager

# Initialize router
router = APIRouter()

# File upload endpoint
@router.post("/upload/")
async def upload_file(file: UploadFile):
    """
    Endpoint to upload a PDF file.

    Args:
        file (UploadFile): The uploaded file object.

    Returns:
        dict: A message and the file path where the file is saved.
    """
    # Check if file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    try:
        # Initialize FileIngestionManager
        manager = FileIngestionManager()
        
        # Save and process the file
        saved_path = await manager.save_file(file)
        return {"message": "File successfully uploaded", "file_path": saved_path}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")