# embeddings.py
from openai import OpenAI
import numpy as np

client = OpenAI()

def get_embeddings(chunks, model="text-embedding-3-large", normalize=True):
    """
    Generate embeddings for a list of text chunks.

    Args:
        chunks (list[str]): List of text strings.
        model (str): Embedding model.
        normalize (bool): Whether to normalize embeddings.

    Returns:
        list[np.ndarray]: List of embeddings.
    """
    response = client.embeddings.create(
        model=model,
        input=chunks
    )
    embeddings = [np.array(e.embedding) for e in response.data]

    if normalize:
        embeddings = [e / np.linalg.norm(e) for e in embeddings]

    return embeddings
