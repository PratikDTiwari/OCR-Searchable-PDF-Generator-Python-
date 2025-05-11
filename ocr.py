import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os

# 👇 IMPORTANT: Set this to your actual install location if different
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_pdf_without_poppler(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    output = fitz.open()

    for page_number in range(len(doc)):
        print(f"OCR processing page {page_number + 1}...")

        page = doc.load_page(page_number)
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))

        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
        ocr_page = fitz.open("pdf", pdf_bytes)
        output.insert_pdf(ocr_page)

    output.save(output_pdf_path)
    output.close()
    print(f"✅ Searchable PDF saved to: {output_pdf_path}")

# 🧾 Ask for folder and file
folder = input("Enter the full folder path where your PDF is located: ").strip()
filename = input("Enter the name of the PDF file (e.g., file.pdf): ").strip()
input_path = os.path.join(folder, filename)
output_path = os.path.join(folder, "searchable_" + filename)

if not os.path.isfile(input_path):
    print(f"❌ File not found: {input_path}")
else:
    ocr_pdf_without_poppler(input_path, output_path)
