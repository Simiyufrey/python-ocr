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



## sample Output




Extracted Text:
IT 643 InfoSec Lab Guidelines and Rubric

Overview
‘Throughout tis cours, you willbe completing several labs. These labs have two purposes:

+ To provide you with valuable opperturities to “walk a mile inthe shoes" ofa forensic practitioner performing basic forensic tasks. Gaining this type of experience is necessary for
‘managing and relating tothe individuals and teams you willnteract with in the fed
+ Tohelp you practice the communication and writing skis you wll need to employ in both pieces of your fina project

‘These activites are relevant to your final project. Tey ae practice opportunities that focus on some ofthe specific topics and sls that need to be addressed in the network defense
traning manual you wll create, and the milestones you will complete inthe modules throughout the course Include examples and details from your experiences with the labs to support the

sections in your training manual.
Directions

To complete the abs, you will summarize each lab and provide screenshots to demonstrate your completion ofthe tasks
Specifically, you must address the fllowing rubric criteria

1. Lab Summary: Provide a thorough summary ofthe lab
2, Required Screenshots: In your lb report submission, include the screenshots outlined inthe InfoSec Lab Expectations document, Screenshots need to splay your name and the date

within the image. Follow these steps to complete the screenshot:

## License

MIT License