#test_retriever.py
import sys
import os

# --- Fix: Make sure Python can find doc_loader.py in project root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vector_db import VectorDB
from embeddings import get_embeddings
from retriever import retrieve_chunks

def test_retrieve_chunks():
    chunks = ["Apple is a fruit", "Car drives on road", "Python is a language"]
    embeddings = get_embeddings(chunks)
    db = VectorDB(dim=len(embeddings[0]))
    db.add_embeddings(embeddings)

    result = retrieve_chunks("What is Python?", db, chunks, top_k=1)

    assert "Python" in result[0]
    print(f"\n Test passed: Retrieved chunk → '{result[0]}'")

if __name__ == "__main__":
    test_retrieve_chunks()
    print("All retriever tests passed successfully!")
