'''
    弧长面积测量   approxPolyDP
    contour 轮廓  epsilon 阈值 越小越逼近真实值   close 闭合区域 一般都是闭合
    几何距计算  原点距   中心距   图象的重心坐标点
    多边形逼近  approxPolyDP  可以区分形状
'''

import cv2 as cv
import numpy as np

# 测量
def measure_demo(img):
    # dst = cv.medianBlur(img,13)
    # 灰度
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 二值化处理  INV取反
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    print("num:{}".format(ret))
    cv.imshow("binary",binary)
    # 找到轮廓
    outImage,contours,hireachy =cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # 使用迭代器
    for i,contour in enumerate(contours):
        # 面积
        area = cv.contourArea(contour)
        # 画区域
        x,y,w,h = cv.boundingRect(contour)
        # 几何距
        mm = cv.moments(contour)
        # print(mm)
        # print(mm['m01'],mm['m10'],mm['m00'])
        # 比例
        rate = min(w,h)/max(w,h)
        print("rate:%s"%rate)
        if mm['m00']:
            print(mm['m10'],mm['m01'],mm['m00'])
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
        # 2 半径
            cv.circle(img,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
        # 画矩形
        #     cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            print("area:%s"%area)
            # 4 是直线逼近上下左右之间的距离 越近越真实
            approxCurve = cv.approxPolyDP(contour,4,True)
            print(approxCurve.shape)
            if approxCurve.shape[0] >= 14:
                cv.drawContours(img,contours,i,(255,0,0),2)
            if approxCurve.shape[0] < 10:
                cv.drawContours(img,contours,i,(0,255,255),2)
            if approxCurve.shape[0] ==11 or approxCurve.shape[0] ==13:
                cv.drawContours(img,contours,i,(0,0,255),2)
    cv.imshow("measure_demo",img)

img = cv.imread("timg.jpg")
print('创建成功')
cv.imshow('ljw',img)
measure_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()








