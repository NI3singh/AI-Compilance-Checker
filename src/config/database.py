import psycopg2
from dotenv import load_dotenv
import os
from typing import List, Dict

# Load environment variables
load_dotenv()

def get_db_connection():
    """
    Connect to the PostgreSQL database.

    Returns:
        psycopg2.connection: A connection to the database.
    """
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

def create_tables():
    """
    Create the necessary tables in the database.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Create tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            document_name TEXT NOT NULL,
            parties TEXT NOT NULL,
            agreement_date DATE,
            expiration_date DATE,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT,
            question_embedding VECTOR(1536),
            answer_embedding VECTOR(1536),
            document_name_embedding VECTOR(1536)
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def save_pdf_metadata(document_name: str, file_path: str) -> int:
    """
    Save PDF metadata (filename and file path) to the database.

    Args:
        document_name (str): Name of the PDF file.
        file_path (str): Path where the PDF file is saved.

    Returns:
        int: The ID of the inserted record.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Insert PDF metadata into the database
    cur.execute("""
        INSERT INTO documents (document_name, file_path)
        VALUES (%s, %s)
        RETURNING id;
    """, (document_name, file_path))
    
    # Get the ID of the inserted record
    pdf_id = cur.fetchone()[0]
    
    conn.commit()
    cur.close()
    conn.close()
    
    return pdf_id

def save_extracted_text(pdf_id: int, text: str):
    """
    Save extracted text into the database.

    Args:
        pdf_id (int): The ID of the PDF record.
        text (str): The extracted text.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Update the record with the extracted text
    cur.execute("""
        UPDATE documents
        SET question = %s
        WHERE id = %s;
    """, (text, pdf_id))
    
    conn.commit()
    cur.close()
    conn.close()

def insert_embeddings(dataset: List[Dict]):
    """
    Insert the dataset with embeddings into the database.

    Args:
        dataset (List[Dict]): The dataset to insert.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    for row in dataset:
        cur.execute("""
            INSERT INTO documents (
                document_name, parties, agreement_date, expiration_date,
                question, answer, category,
                question_embedding, answer_embedding, document_name_embedding
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            row["Document Name"], row["Parties"], row["Agreement Date"], row["Expiration Date"],
            row["Question"], row["Answer"], row["Category"],
            row["question_embedding"], row["answer_embedding"], row["document_name_embedding"]
        ))
    
    conn.commit()
    cur.close()
    conn.close()