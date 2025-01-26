from openai import OpenAI
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_embedding(text: str, model: str = "text-embedding-3-small") -> List[float]:
    
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def generate_embeddings_for_dataset(dataset: List[Dict]) -> List[Dict]:
    
    for row in dataset:
        # Generate embeddings for the Question, Answer, and Document Name
        row["question_embedding"] = get_embedding(row["Question"])
        row["answer_embedding"] = get_embedding(row["Answer"])
        row["document_name_embedding"] = get_embedding(row["Document Name"])
    
    return dataset