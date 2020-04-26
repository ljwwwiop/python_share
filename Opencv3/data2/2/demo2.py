'''
    超大图 二值化方法

'''
import cv2 as cv
import numpy as np

# 图像二值化
def big_image_demo(img):
    print(img.shape)
    cw = 20
    ch = 20
    h,w = img.shape[:2]
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            rol = gray[row:row+ch,col:col+cw]
            print(np.str(rol),np.mean(rol))
            # 阈值方法 可用全局 可以局部  39显示 黑白度  20这个地方 控制方格里面的噪音 局部可以消除
            dst = cv.adaptiveThreshold(rol,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,39,20)
            gray[row:row+ch,col:cw+col] = dst
    cv.imshow("demo",gray)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
big_image_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()
