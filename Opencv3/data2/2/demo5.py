'''
    Canny 边缘提取 先降梯度 再二值化处理
    Canny 算法原理 五步 1 高斯模糊  2 灰度转换  3 计算梯度  4 非最大信号抑制  5 高低阈值输出二值图象
    4  5
'''
import cv2 as cv
import numpy as np

def edge_demo(img):
    # 1 降低噪声 必须要先高斯降噪
    blurred = cv.GaussianBlur(img,(3,3),0)
    # 2
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # X 方向的梯度
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # Y 梯度
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    # edge 边缘  Y1 ,Y2 3:1 或者 2:1 比例最好 两种方法 可以blurred直接使用 自己判断两种方式
    # edge_output = cv.Canny(xgrad,ygrad,50,150)
    edge_output = cv.Canny(blurred, 50, 150)

    # 输出黑白图片
    cv.imshow("edge_output",edge_output)

    # 输出彩色图片
    dst = cv.bitwise_and(img,img,mask=edge_output)
    cv.imshow("Color img",dst)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
edge_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()

