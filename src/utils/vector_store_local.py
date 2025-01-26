import pickle

def save_embeddings(vectorstore, embedding_file="embeddings.pkl"):

    with open(embedding_file, "wb") as f:
        pickle.dump(vectorstore, f)