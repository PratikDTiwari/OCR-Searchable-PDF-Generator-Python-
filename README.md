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
