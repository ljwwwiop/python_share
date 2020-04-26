'''
    轮廓检测  基于图象的边缘检测 寻找对象轮廓的方法
    所以边缘提取的阈值选定会影响最终轮廓发现
    两个 API  findcontours 发现轮廓  drawcontours 绘制轮廓
    利用梯度 避免阈值烦恼
'''
import cv2 as cv
import numpy as np

# Canny 边缘提取
def edge_demo(img):
    # 1 降低噪声 必须要先高斯降噪
    blurred = cv.medianBlur(img,15)
    # 2
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # X 方向的梯度
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # Y 梯度
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    # edge 边缘  Y1 ,Y2 3:1 或者 2:1 比例最好 两种方法 可以blurred直接使用 自己判断两种方式
    # edge_output = cv.Canny(xgrad,ygrad,50,150)
    edge_output = cv.Canny(blurred, 155, 310)

    # 输出黑白图片
    cv.imshow("edge_output",edge_output)
    return edge_output

def contours_demo(img):
    '''# 第一步降噪 可选
    dst = cv.medianBlur(img,13)
    # 灰度
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    # 二值化 处理 ret-0
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("gray",binary)'''
    # 只需要contours 这个参数   对象，方法cv.RETR_TREE 和cv.RETR_EXTERNAL 简单的cv.CHAIN_APPROX_SIMPLE
    binary = edge_demo(img)
    cloneimage,contours,heriachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        # 对象，返回所有轮廓绘制i的,RGB颜色      2 对应的 -1为全部填充
        cv.drawContours(img,contours,i,(0,255,255),2)
        print(i)
    cv.imshow("contour",img)

img = cv.imread("yuan.jpg")
print('创建成功')
cv.imshow('ljw',img)
contours_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()








