import cv2
import pytesseract
from PIL import Image

def process_image(image_path):
    # Load image
    image = cv2.imread(image_path)

    # Preprocess image (grayscale, thresholding, etc.)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Use Tesseract to do OCR on the processed image
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    
    return text
