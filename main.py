import pytesseract
from fpdf import FPDF
from PIL import Image
import os

# Set tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    
    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def save_text_to_file(text, output_file):
    """
    Save extracted text to a file.
    
    :param text: Text to save.
    :param output_file: Path to the output file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", "fonts/dejavu-sans/DejaVuSans.ttf")
    pdf.set_font("DejaVu", size=12)


    for line in text.split('\n'):
        pdf.cell(0, 10, text=line, new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.output(output_file)


def main():
    image_path = 'images/test image.PNG'  # Replace with your image path
    output_file =os.path.join("output", os.path.basename(image_path).split(".")[0] + ".pdf")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)


    print(output_file)
    # # Extract text from the image
    extracted_text = text_from_image(image_path)
    
    # # Save the extracted text to a PDF file
    save_text_to_file(extracted_text, output_file)

    print(f"Text extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
