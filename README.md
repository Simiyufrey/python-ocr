# OCR Automation

This project extracts text from images using Python, Tesseract OCR, and saves the results as PDF files.

## Features

- Extracts text from image files (PNG, JPG, etc.) using Tesseract OCR.
- Saves extracted text to a PDF using a Unicode font (DejaVu Sans).
- Handles Unicode characters correctly in the output PDF.

## Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (Windows: install and set the path in `main.py`)
- Python packages:
  - pytesseract
  - pillow
  - fpdf2

## Setup

1. **Install Tesseract OCR**  
   Download and install from [here](https://github.com/tesseract-ocr/tesseract/wiki).

2. **Install Python dependencies**  
   ```
   pip install pytesseract pillow fpdf2
   ```

3. **Download DejaVu Sans font**  
   Place `DejaVuSans.ttf` in `fonts/dejavu-sans/` (create folders if needed).

## Usage

1. Place your image in the `images/` folder.



![Sample OCR Image](images/test%20image.PNG)
2. Edit `main.py` to set your image path if needed.
3. Run the script:
   ```
   python main.py
   ```
4. The extracted text will be saved as a PDF in the `output/` folder.

## File Structure

```
OCR/
├── fonts/
│   └── dejavu-sans/
│       └── DejaVuSans.ttf
├── images/
│   └── test image.PNG
├── output/
│   └── test image.pdf
├── main.py
└── README.md
```

## License

MIT License