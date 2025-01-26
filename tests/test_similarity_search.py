import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.similarity_search import similarity_search

# Perform a similarity search
query = "What is the governing law?"
results = similarity_search(query, top_k=3)

# Print the results
for i, result in enumerate(results):
    print(f"Result {i + 1}:")
    print(result)
    print("-" * 50)