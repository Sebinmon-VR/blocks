import re
import pdfplumber
import docx
import pandas as pd

def clean_text(text):
    """
    Remove extra spaces, empty lines, and weird characters.
    """
    if not text:
        return ""
    # Replace multiple spaces/newlines/tabs with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def load_pdf(file_path):
    """
    Load text from a PDF file.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # sometimes extract_text() returns None
                text += page_text + " "
    return clean_text(text)


def load_docx(file_path):
    """
    Load text from a Word (.docx) file.
    """
    doc = docx.Document(file_path)
    text = " ".join([para.text for para in doc.paragraphs])
    return clean_text(text)



def load_csv(file_path):
    """
    Load text from a CSV file.
    """
    df = pd.read_csv(file_path)
    text = df.to_string(index=False)
    return clean_text(text)