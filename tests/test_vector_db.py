#test_vector_db.py
import sys
import os

# --- Fix: Make sure Python can find doc_loader.py in project root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from vector_db import VectorDB

def test_add_and_search():
    db = VectorDB(dim=3)
    embeddings = [np.array([1,2,3], dtype="float32"),
                  np.array([2,3,4], dtype="float32")]
    db.add_embeddings(embeddings)

    query = np.array([1,2,3], dtype="float32")
    indices, distances = db.search(query, top_k=1)
    assert indices[0] == 0
    print(f"\n✅ Test passed: Retrieved index {indices[0]} with distance {distances[0]:.4f}")

if __name__ == "__main__":
    test_add_and_search()
    print("All tests passed!")
