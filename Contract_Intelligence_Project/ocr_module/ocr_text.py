

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("sample.png")

text = pytesseract.image_to_string(img)

with open("output/ocr_result.txt", "w", encoding="utf-8") as f:
                                                               f.write(text)

print("OCR text saved successfully!")