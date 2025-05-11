📄 OCR Searchable PDF Generator (Python)
Convert image-based PDFs (scanned or photo PDFs) into searchable text PDFs using Python and Tesseract OCR – without requiring external tools like Poppler.

🚀 Features
Converts non-searchable (scanned) PDFs to searchable PDFs
Keeps the original layout (adds hidden text layer)
Works with multi-page PDFs
No need to install Poppler or use pdf2image
CLI prompts for folder and PDF file path

🛠 Requirements
📦 Python Libraries
Install required packages with:
Open cmd and write the below command - pip install pytesseract pymupdf pillow

⚙️ External Dependency
🧠 This script requires Tesseract-OCR to be installed (not a Python package).

Download Tesseract for Windows:
https://github.com/UB-Mannheim/tesseract/wiki

Install to:
C:\Program Files\Tesseract-OCR

Add to System PATH (or specify the path in code, see below)

💻 How It Works

This script uses:

PyMuPDF to render each PDF page into an image
pytesseract to extract text from images
Outputs a new searchable PDF with the same layout and text layer added

🧪 Usage























