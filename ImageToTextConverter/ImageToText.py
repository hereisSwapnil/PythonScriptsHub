!pip install pytesseract
!sudo apt-get install tesseract-ocr
!pip install opencv-python-headless
from PIL import Image
import pytesseract
import cv2
from google.colab import files

def extract_text_from_image(image_path):
    # Load the image from the provided path
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text
    _, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(thresh)

    return text

# Function to upload an image file in Google Colab
def upload_image():
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename

# Ask the user whether to upload a file or provide a path
choice = input("Do you want to upload a file? (yes/no): ").strip().lower()
if choice == "yes":
    # Upload the image file
    image_filename = upload_image()
    if image_filename:
        # Extract text from the uploaded image
        extracted_text = extract_text_from_image(image_filename)
        print("Scanned Text:")
        print(extracted_text)
else:
    # Provide the path to the image you want to scan
    image_path = "123.png"
    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Scanned Text:")
    print(extracted_text)
