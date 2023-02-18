import cv2
#import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
image = cv2.imread("images.jpg")
string = pytesseract.image_to_string(image)
# print it
print(string)
