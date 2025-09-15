# text_splitter.py

import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def chunk_text(text, chunk_size=100, overlap=1):
    """
    Split text into chunks without cutting sentences in half using spaCy.
    
    Parameters:
        text: full text to split
        chunk_size: approx max characters per chunk
        overlap: number of sentences to repeat in next chunk
    """
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    chunks = []
    current_chunk = []

    i = 0
    while i < len(sentences):
        chunk_candidate = ' '.join(current_chunk + [sentences[i]])
        if len(chunk_candidate) <= chunk_size:
            current_chunk.append(sentences[i])
            i += 1
        else:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            # Prepare next chunk with overlap sentences
            current_chunk = current_chunk[-overlap:] if overlap <= len(current_chunk) else current_chunk

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


# --- Quick test ---
if __name__ == "__main__":
    sample_text = "Hello world. This is a sample text. It should be split into chunks without cutting sentences."
    chunks = chunk_text(sample_text, chunk_size=50, overlap=1)
    for i, c in enumerate(chunks):
        print(f"Chunk {i+1}: {c}")
