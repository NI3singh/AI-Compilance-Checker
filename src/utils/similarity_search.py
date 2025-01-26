from src.models.embedding_model import get_embedding
from src.config.database import get_db_connection
from typing import List, Dict

def similarity_search(query: str, top_k: int = 5) -> List[Dict]:
    """
    Perform a similarity search on the database.

    Args:
        query (str): The query to search for.
        top_k (int): The number of results to return.

    Returns:
        List[Dict]: The top-k most similar results.
    """
    # Generate the query embedding
    query_embedding = get_embedding(text=query)
    
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Perform the similarity search
    cur.execute("""
        SELECT document_name, parties, agreement_date, expiration_date, question, answer, category
        FROM documents
        ORDER BY question_embedding <=> %s::vector
        LIMIT %s;
    """, (query_embedding, top_k))
    
    results = cur.fetchall()
    
    # Format the results
    formatted_results = []
    for row in results:
        formatted_results.append({
            "document_name": row[0],
            "parties": row[1],
            "agreement_date": row[2],
            "expiration_date": row[3],
            "question": row[4],
            "answer": row[5],
            "category": row[6]
        })
    
    cur.close()
    conn.close()
    
    return formatted_results