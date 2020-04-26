'''
    图像直方图
    将像素转为直方图
    观察直方图的 波峰，波谷 做出结论
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    # image.ravel 将多通道像素转化为 平面直方图   最大256  范围0-256
    plt.hist(image.ravel(),256,[0,256])
    plt.title("DistranGe")
    plt.show()

# 获取我们想要的直方图
def image_hist(image):
    color = ["yellow","red","blue"]
    for i , color in enumerate(color):
        # 把三个通道的 所有象素 取出来 并且不同颜色表示出来
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()

img = cv.imread("man.jpg")
print('创建成功')
cv.imshow('ljw',img)
image_hist(img)
cv.waitKey(0)
cv.destroyAllWindows()


