import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config.database import create_tables, insert_embeddings
from src.utils.data_loader import load_dataset
from src.models.embedding_model import generate_embeddings_for_dataset

# Load the dataset
dataset = load_dataset("../data/contracts_dataset.csv")

# Generate embeddings for the dataset
dataset_with_embeddings = generate_embeddings_for_dataset(dataset)

# Create tables and insert embeddings
create_tables()
insert_embeddings(dataset_with_embeddings)

print("Data successfully inserted into the database!")