import unittest
import os
from doc_loader import load_pdf, load_docx, load_csv
from text_splitter import chunk_text

# path to the samples folder
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "..", "samples")

class TestTextSplitter(unittest.TestCase):

    def test_pdf_chunks(self):
        file_path = os.path.join(SAMPLES_DIR, "sample.pdf")
        text = load_pdf(file_path)
        chunks = chunk_text(text, chunk_size=30, overlap=5)

        self.assertGreater(len(chunks), 0)  # at least one chunk
        self.assertTrue(all(len(c) <= 30 for c in chunks))  # no chunk too long

    def test_docx_chunks(self):
        file_path = os.path.join(SAMPLES_DIR, "sample.docx")
        text = load_docx(file_path)
        chunks = chunk_text(text, chunk_size=40, overlap=10)

        self.assertGreater(len(chunks), 0)
        self.assertTrue(all(len(c) <= 40 for c in chunks))

    def test_csv_chunks(self):
        file_path = os.path.join(SAMPLES_DIR, "sample.csv")
        text = load_csv(file_path)
        chunks = chunk_text(text, chunk_size=50, overlap=5)

        self.assertGreater(len(chunks), 0)
        self.assertTrue(all(len(c) <= 50 for c in chunks))


if __name__ == "__main__":
    unittest.main()
