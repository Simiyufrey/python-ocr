import pytesseract
from PIL import Image
import os
from fpdf import FPDF
import fitz  # PyMuPDF for PDF manipulation     
import io
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def extract_images_from_pdf(pdf_path):
    """
    Extract images from a PDF file.
    
    :param pdf_path: Path to the PDF file.
    :return: List of image objects.
    """
    images = []
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            print("Extracting images from page", page_num + 1, "of", len(pdf_document))
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            images.append((page_num, img_index, image_bytes, image_ext))
    return images
   

def ocr_image_bytes(image):
    """
    Perform OCR on a list of images and return the extracted text.
    
    :param image: List of image objects.
    :return: Extracted text as a string.
    """
    image = Image.open(io.BytesIO(image))
    text = pytesseract.image_to_string(image)
    return text  


def save_text_to_pdf(image_text_pairs, output_file):

    pdf= FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", "fonts/dejavu-sans/DejaVuSans.ttf")
    pdf.set_font("DejaVu", size=12)

    for idx, (img_bytes, img_ext, text) in enumerate(image_text_pairs):
        pdf.add_page()
       
        for line in text.split('\n'):
            pdf.cell(0, 10, text=line, new_x="LMARGIN", new_y="NEXT", align='L')
        
    pdf.output(output_file)


def main():
    pdf_path = "pdfs/admission.pdf"  # Your input PDF
    output_pdf = "output/ocr_output.pdf"
    images = extract_images_from_pdf(pdf_path)
    image_text_pairs = []
    for page_num, img_index, img_bytes, img_ext in images:
        text = ocr_image_bytes(img_bytes)
        image_text_pairs.append((img_bytes, img_ext, text))
    save_text_to_pdf(image_text_pairs, output_pdf)
    print(f"OCR results saved to {output_pdf}")

if __name__ == "__main__":
    main()
