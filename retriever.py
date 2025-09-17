# retriever.py
from embeddings import get_embeddings

def retrieve_chunks(question, vector_db, chunks, top_k=3):
    """
    Retrieve top-k most relevant chunks for a given question.

    Args:
        question (str): User query.
        vector_db (VectorDB): FAISS index.
        chunks (list[str]): Original text chunks.
        top_k (int): Number of results.

    Returns:
        list[str]: Relevant text chunks.
    """
    query_embedding = get_embeddings([question])[0]
    indices, _ = vector_db.search(query_embedding, top_k=top_k)
    return [chunks[i] for i in indices]
