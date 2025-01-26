import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.data_loader import load_dataset
from src.models.embedding_model import generate_embeddings_for_dataset

# Load the dataset
dataset = load_dataset(r"C:\Users\itsni\Desktop\Compliance-Checker\data\contracts_dataset.csv")

# Generate embeddings for the dataset
dataset_with_embeddings = generate_embeddings_for_dataset(dataset)

# Print the first row with embeddings
print(dataset_with_embeddings[0])