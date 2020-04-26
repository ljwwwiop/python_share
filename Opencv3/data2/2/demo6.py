'''
    直线检测  --- 基于 霍夫直线变换  降直线 转到  空间极坐标
'''
import cv2 as cv
import numpy as np

def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    # 默认窗口大小3
    # 两个方法 一个出 极坐标图  另一个P 出 直线图
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    # 极坐标半径 角度 边缘提取中的低值
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a+rho
        y0 = b+rho
        x1 = int(x0+1000*(-b))
        x2 = int(x0 - 1000 * (-b))
        y1 = int(y0+1000*(a))
        y2 = int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),1)
    cv.imshow("line",image)

def line_detect_possible_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    # 核心api 是 最小长度minLineLength支持50个象素  和maxLineGap小于等于这个 1象素宽度自动连接起来
    lines = cv.HoughLinesP(edges,1,np.pi/180,50,minLineLength=70,maxLineGap=1)
    for line in lines:
        print(lines)
        x1,y1,x2,y2 = line[0]
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),1)
    cv.imshow("line_detect_possible_demo",img)

img = cv.imread("zhixian.jpg")
print('创建成功')
cv.imshow('ljw',img)
line_detect_possible_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()
