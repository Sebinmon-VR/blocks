#test_embeddings.py
import sys
import os

# --- Fix: Make sure Python can find doc_loader.py in project root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from embeddings import get_embeddings


def test_get_embeddings():
    chunks = ["Hello world", "OpenAI embeddings"]
    embeddings = get_embeddings(chunks)

    assert len(embeddings) == 2
    assert embeddings[0].shape[0] > 100  # dimensionality > 100

    print(f"\n Test passed: Generated {len(embeddings)} embeddings "
          f"with dimension {embeddings[0].shape[0]}")

if __name__ == "__main__":
    test_get_embeddings()
    print("All embedding tests passed successfully!")

