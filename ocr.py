"""
OCR Searchable PDF Generator

If you encounter any issues or need support, please reach out:

LinkedIn: https://www.linkedin.com/in/pratikdtiwari/
Email: Pratikdtiwari@gmail.com

Last updated: 2025-05-11
"""

import os
import io
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def set_tesseract_cmd():
    """
    Set the Tesseract command path.
    Checks the TESSERACT_CMD environment variable first,
    otherwise uses the default Windows path.
    """
    tesseract_cmd = os.environ.get("TESSERACT_CMD")
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    else:
        # Default Windows path; modify as needed for your OS
        default_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = default_path

def ocr_pdf_without_poppler(input_pdf_path, output_pdf_path):
    """
    Converts a scanned PDF to a searchable PDF using PyMuPDF and pytesseract.
    Args:
        input_pdf_path (str): Path to the input scanned PDF.
        output_pdf_path (str): Path to save the searchable PDF.
    """
    try:
        doc = fitz.open(input_pdf_path)
        output = fitz.open()

        for page_number in range(len(doc)):
            print(f"OCR processing page {page_number + 1} of {len(doc)}...")

            page = doc.load_page(page_number)
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))

            pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
            ocr_page = fitz.open("pdf", pdf_bytes)
            output.insert_pdf(ocr_page)

        output.save(output_pdf_path)
        output.close()
        print(f"✅ Searchable PDF saved to: {output_pdf_path}")

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")

def get_pdf_paths():
    """
    Prompts the user for folder and PDF file name, and returns input/output paths.
    Returns:
        tuple: (input_pdf_path, output_pdf_path)
    """
    folder = input("Enter the full folder path where your PDF is located: ").strip()
    while not os.path.isdir(folder):
        print(f"❌ Folder not found: {folder}")
        folder = input("Please enter a valid folder path: ").strip()

    filename = input("Enter the name of the PDF file (e.g., file.pdf): ").strip()
    input_path = os.path.join(folder, filename)
    while not os.path.isfile(input_path):
        print(f"❌ File not found: {input_path}")
        filename = input("Please enter a valid PDF file name: ").strip()
        input_path = os.path.join(folder, filename)

    output_path = os.path.join(folder, f"searchable_{filename}")
    return input_path, output_path

if __name__ == "__main__":
    set_tesseract_cmd()
    input_pdf, output_pdf = get_pdf_paths()
    ocr_pdf_without_poppler(input_pdf, output_pdf)
