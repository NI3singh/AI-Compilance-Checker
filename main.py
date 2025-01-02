from fastapi import FastAPI
from src.controllers.pdf_controller import router as pdf_router

app = FastAPI()
app.include_router(pdf_router, prefix="/pdf")

if __name__ == "__main__":
    app.run(debug=True)