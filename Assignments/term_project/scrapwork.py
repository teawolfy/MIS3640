import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/twolf1/Google Drive/College/BABSON/SENIOR S1/Problem Solving & Software Design\Python\Assignments/term_project/Tesseract-OCR/tesseract'
print(pytesseract.image_to_string(Image.open('old-big.png')))
