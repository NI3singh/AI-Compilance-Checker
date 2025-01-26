import pandas as pd
from typing import List, Dict

def load_dataset(file_path: str) -> List[Dict]:
    # file_path = r'C:\Users\itsni\Desktop\Compliance-Checker\data\contracts_dataset.csv'
    # Load the dataset from the CSV file
    df = pd.read_csv(file_path)
    
    # Convert date columns to datetime format (if they exist)
    if "Agreement Date" in df.columns:
        df["Agreement Date"] = pd.to_datetime(df["Agreement Date"], format="%Y-%m-%d")
    if "Expiration Date" in df.columns:
        df["Expiration Date"] = pd.to_datetime(df["Expiration Date"], format="%Y-%m-%d")
    
    # Handle missing values (if any)
    df.fillna({"Parties": "Unknown", "Category": "Uncategorized"}, inplace=True)
    
    # Convert the DataFrame to a list of dictionaries
    dataset = df.to_dict(orient="records")
    
    return dataset