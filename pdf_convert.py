# import PyPDF2
# from pdf2image import convert_from_path

# def convert_pdf_to_images(pdf_path):
#     pages = convert_from_path(pdf_path)

#     for i, page in enumerate(pages):
#         page.save(f"page_{i}.jpg", "JPEG")


# def pdf_to_text(pdf_path, output_txt):
#     # Open the PDF file in read-binary mode
#     with open(pdf_path, 'rb') as pdf_file:
#         # Create a PdfReader object instead of PdfFileReader
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Initialize an empty string to store the text
#         text = ''

#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()

#     # Write the extracted text to a text file
#     with open(output_txt, 'w', encoding='utf-8') as txt_file:
#         txt_file.write(text)

# if __name__ == "__main__":
#     pdf_path = 'WhatsApp Image 2024-08-19 at 19.24.51.pdf'

#     output_txt = 'aadhar_1.txt'

#     pdf_to_text(pdf_path, output_txt)

#     print("PDF converted to text successfully!")
import pytesseract
from pdf2image import convert_from_path

# convert to image using resolution 600 dpi 
pages = convert_from_path("Aadhar Card New.pdf", 600)

# extract text
text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'
print(text_data)