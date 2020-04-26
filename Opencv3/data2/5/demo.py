'''
    圆检测
    霍夫圆检测  一样的原理 平面坐标 转换到空间坐标系 需要已知(x0,y0,R)
    霍夫圆检测 对噪声比较敏感  先对图像进行中值滤波处理
    1  检测边缘  ，发现可能的圆心
    2  基于上一步从候选圆心开始计算最佳半径大小
'''
import cv2 as cv
import numpy as np

# 圆霍夫检测
def detect_cricle_demo(img):
    # 中值滤波 一定要降噪
    dst = cv.pyrMeanShiftFiltering(img,25,100)
    # cv.imshow("dst",dst)
    image = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    # 对象  方法只有一个cv.HOUGH_GRADIENT 基于梯度,dp 走的步长 最小距离同心圆 象素相差很小<20为统一圆,
    # parmal 边缘提取的地址和高值 , 最大半径和 最小半径 默认是5
    circle = cv.HoughCircles(image,cv.HOUGH_GRADIENT,1,100,param1=50,param2=30,minRadius=0,maxRadius=0)
    # 得到的半径不是整数  要转化为整数
    circle = np.uint16(np.around(circle))
    # 得到了(x0,y0,R)
    for i in circle[0, : ]:
        # 画圆
        cv.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(img,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow("circle",img)

img = cv.imread("yuan.jpg")
print('创建成功')
cv.imshow('yuan',img)
detect_cricle_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()