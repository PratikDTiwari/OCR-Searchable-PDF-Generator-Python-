# 🧾 OCR Searchable PDF Generator (Python)

Convert **image-based (scanned) PDFs** into **searchable PDFs** using Python and Tesseract OCR – no Poppler or external tools required.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [How It Works](#how-it-works)
- [FAQ](#faq)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Features

- 🖼 Converts scanned PDFs to searchable PDFs
- 📄 Preserves original PDF layout
- 📚 Handles multi-page PDFs
- ❌ No Poppler dependency
- 🖥 CLI-based: enter folder path and file name at runtime

---

## Requirements

- **Python** 3.7+
- **Python Libraries**: `pytesseract`, `pymupdf`, `Pillow`
- **Tesseract-OCR Engine** (must be installed separately)

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/your-username/ocr-searchable-pdf.git
    cd ocr-searchable-pdf
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Install Tesseract-OCR:**
    - Download from: https://github.com/UB-Mannheim/tesseract/wiki
    - Add the install directory to your System PATH, or set the path manually in your code:
      ```
      pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
      ```

---

## Usage

Run the script:

python ocr.py

Follow the prompts:

Enter the full folder path where your PDF is located: C:\Users\YourName\Documents
Enter the name of the PDF file (e.g., file.pdf): scanned_notes.pdf

**Output:**

✅ Searchable PDF saved to: C:\Users\YourName\Documents\searchable_scanned_notes.pdf


---

## Folder Structure

ocr-searchable-pdf/
├── ocr.py
├── requirements.txt
├── .gitignore
├── README.md
└── scanned_pdfs/
└── sample.pdf

---

## How It Works

- Uses PyMuPDF to convert PDF pages to images
- Uses pytesseract to perform OCR on each image
- Combines OCR-processed pages into a searchable PDF

---

## FAQ

**Q: Do I need Poppler or pdf2image?**  
❌ No. This project uses PyMuPDF and Pillow only.

**Q: Does it support color PDFs?**  
✅ Yes. Both color and grayscale images are supported.

**Q: Can I convert multipage PDFs?**  
✅ Absolutely.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome!  
- Open issues for bugs or feature requests
- Submit pull requests to enhance functionality

---

## Contact

For questions, suggestions, or support, open an issue or contact the maintainer via GitHub.

---

## Last Updated

This README was last updated on 2025-05-11.

---


