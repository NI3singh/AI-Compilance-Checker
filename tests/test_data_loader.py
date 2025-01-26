import sys
import os
# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.data_loader import load_dataset

# Load the dataset
dataset = load_dataset(r"C:\Users\itsni\Desktop\Compliance-Checker\data\contracts_dataset.csv")

# Print the first row
print(dataset[0])