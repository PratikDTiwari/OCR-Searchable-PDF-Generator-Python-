🧾 **OCR Searchable PDF Generator (Python)**
Convert image-based (scanned) PDFs into searchable PDFs using Python and Tesseract OCR – no Poppler or external tools required.

🚩 **Table of Contents**
Features
Requirements
Installation
Usage
Folder Structure
How It Works
FAQ
License
Contributing
Contact

🚀 **Features**
🖼 Converts scanned PDFs to searchable PDFs
📄 Preserves original PDF layout
📚 Handles multi-page PDFs
❌ No Poppler dependency

🖥 CLI-based: enter folder path and file name at runtime

🛠 **Requirements**
Python 3.7+
Python Libraries:
pytesseract
pymupdf
Pillow

**Install all dependencies with**:

bash
pip install -r requirements.txt
Or individually:

bash
pip install pytesseract pymupdf Pillow
Tesseract-OCR Engine (Required)
Download and install Tesseract from:
https://github.com/UB-Mannheim/tesseract/wiki

Add the install directory to your System PATH, or set the path manually in your Python code:

**python**
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

💾 **Installation**
Clone the repository:

**bash**
git clone https://github.com/your-username/ocr-searchable-pdf.git
cd ocr-searchable-pdf
Install dependencies:

**bash**
pip install -r requirements.txt
Install Tesseract-OCR:
Follow the instructions above for your operating system.

🧪 **Usage**
Run the script:

**bash**
python ocr.py
Follow the prompts:

**text**
Enter the full folder path where your PDF is located: C:\Users\YourName\Documents
Enter the name of the PDF file (e.g., file.pdf): scanned_notes.pdf
Output:

**text**
✅ Searchable PDF saved to: C:\Users\YourName\Documents\searchable_scanned_notes.pdf
📂 Folder Structure
text
ocr-searchable-pdf/
├── ocr.py
├── requirements.txt
├── .gitignore
├── README.md
└── scanned_pdfs/
    └── sample.pdf

📌 **How It Works**
Uses PyMuPDF to convert PDF pages to images

Uses pytesseract to perform OCR on each image

Combines OCR-processed pages into a searchable PDF

❓ **FAQ**
Q: Do I need Poppler or pdf2image?
❌ No. This project uses PyMuPDF and Pillow only.

Q: Does it support color PDFs?
✅ Yes. Both color and grayscale images are supported.

Q: Can I convert multipage PDFs?
✅ Absolutely.

📄 **License**
This project is licensed under the MIT License.

💬 **Contributing**
Contributions are welcome!

Open issues for bugs or feature requests

Submit pull requests to enhance functionality

📫 **Contact**
For questions, suggestions, or support, open an issue or contact the maintainer via GitHub.

Tips for further improvement:
Add a screenshot or GIF of the tool in action for clarity.
Consider including a "Troubleshooting" section for common errors (e.g., Tesseract not found).
Optionally, add badges (build status, license, etc.) at the top for visual appeal.
If you plan to accept contributions, consider adding a CONTRIBUTING.md file.
Your README already covers all essential sections: project overview, features, requirements, installation, usage, folder structure, FAQ, license, and contribution guidelines. Including a table of contents and contact section further improves navigation and usability.

