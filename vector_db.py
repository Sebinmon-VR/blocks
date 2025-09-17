# vector_db.py
import faiss
import numpy as np

class VectorDB:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)  # L2 distance search
        self.vectors = []
    
    def add_embeddings(self, embeddings):
        """
        Add embeddings to the FAISS index.
        """
        np_embeddings = np.array(embeddings).astype("float32")
        self.index.add(np_embeddings)
        self.vectors.extend(embeddings)

    def search(self, query_embedding, top_k=5):
        """
        Search top-k similar vectors.
        """
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)
        return indices[0], distances[0]
