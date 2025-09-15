import sys
import os

# --- Fix: Make sure Python can find doc_loader.py in project root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doc_loader import load_pdf, load_docx, load_csv

# --- Test PDF loader ---
def test_load_pdf():
    text = load_pdf("samples/sample.pdf")
    assert "Hello" in text  # check if PDF text contains "Hello"

# --- Test Word loader ---
def test_load_docx():
    text = load_docx("samples/sample.docx")
    assert "Sample DOCX" in text  # check if DOCX text contains heading

# --- Test CSV loader ---
def test_load_csv():
    text = load_csv("samples/sample.csv")
    assert "Alice" in text  # check if CSV text contains first row name

# --- Run all tests ---
if __name__ == "__main__":
    test_load_pdf()
    test_load_docx()
    test_load_csv()
    print("All tests passed!")
