
import pytesseract as pyt
from PIL import Image
import cv2 as cv

img = cv.imread("timg.jpg")
text = pyt.image_to_string(Image.fromarray(img))
print(text)
