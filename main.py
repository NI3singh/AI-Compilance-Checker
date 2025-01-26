
import sys
sys.path.append(r"C:\Users\itsni\Desktop\Compliance-Checker\src")
from fastapi import FastAPI, UploadFile, File, HTTPException
from src.Managers.ingestion_manager import FileIngestionManager
from src.utils.similarity_search import similarity_search
from typing import List, Dict

# Initialize FastAPI app
app = FastAPI()

# Initialize FileIngestionManager
ingestion_manager = FileIngestionManager()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    try:
        # Save and process the file
        file_path = await ingestion_manager.save_file(file)
        return {"message": "File successfully uploaded", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@app.get("/search/")
async def search(query: str, top_k: int = 5) -> List[Dict]:
    
    try:
        results = similarity_search(query, top_k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)