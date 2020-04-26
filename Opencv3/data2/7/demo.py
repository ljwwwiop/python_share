'''
    人脸检测  主要有HAAR 和LBP数据
'''
import cv2 as cv
import numpy as np

def face_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face = cv.CascadeClassifier('D:\python\whl\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
    eye = cv.CascadeClassifier('D:\python\whl\opencv-master\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml')

    # 图象  每次是原来的1.02倍 检测，如果检测不出来 1这个可以调低找到几个才认为是人脸  越高越严格
    faces = face.detectMultiScale(gray,1.1,2)
    # faces 获取人脸参数  x,y,w,h
    for (x, y, w, h) in faces:
        # 画图
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    eyes = eye.detectMultiScale(gray,1.1,2)
    for (x,y,w,h) in eyes:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow("face_detect",img)

img = cv.imread("man.jpg")

print('创建成功')
# cv.imshow('ljw',img)
# face_detect_demo(img)
capture = cv.VideoCapture(0)
# 1外置
while True:
    ret,frame = capture.read()
    frame = cv.flip(frame,1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c ==27: # ESC
        break


cv.waitKey(0)
cv.destroyAllWindows()