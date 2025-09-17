import sys
import os

# --- Fix: Make sure Python can find doc_loader.py in project root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llm_agent import generate_answer

def test_real_answer():
    chunks = [
        "My name is ChatGPT, a large language model trained by OpenAI.",
        "It supports libraries like NumPy and Pandas."
        "Cat is a small domesticated carnivorous mammal."
        "Python is a programming language often used for AI and data science."
    ]
    question = "What is cat"
    answer = generate_answer(question, chunks)
    assert "Cat" in answer
