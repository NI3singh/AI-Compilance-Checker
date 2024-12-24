import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    UPLOAD_DIR = os.getenv("UPLOAD_DIR")
    HASH_DB_PATH = os.getenv("HASH_DB_PATH")


settings = Settings()