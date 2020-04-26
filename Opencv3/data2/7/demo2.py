'''
    数字验证码识别 基础最后一课
    tesserocr 是识别库  tesseract 是win10对应ocr工具  pytes.是python上识别的
    图片处理后 降噪 二值化  干扰都去掉在检测
'''
import cv2 as cv
import numpy as np
import pytesseract as pyt
from PIL import Image

# 不同情况不同验证
def recognize_text(img):
    dst =  cv.medianBlur(img, 3)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dit = cv.dilate(binary,kernel)
    cv.imshow("binary",dit)
    text = pyt.image_to_string(Image.fromarray(dit))
    print(text)

img = cv.imread("num2.jpg")
print('创建成功')
cv.imshow('ljw',img)
recognize_text(img)

cv.waitKey(0)
cv.destroyAllWindows()


