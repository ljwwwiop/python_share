'''
    图像分割  分水岭算法(有噪声一定先降噪)
    流程  1输入图像  2灰度  3二值化  4距离变换  5寻找种子  6生成Marker  7分水岭变换  8输出

'''

import cv2 as cv
import numpy as np

# 分水岭算法
def watered_demo(img):
    # 高斯模糊 cv.pyrMeanShiftFiltering(img,10,100)

    dst = cv.medianBlur(img, 15)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)

    # morphology operation 填充上边缘
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (4, 4))
    # iterations*2 两次开操作
    nb = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sure_bg = cv.dilate(nb,kernel,iterations=3)
    cv.imshow("sure_bg",sure_bg)

    # 距离计算  卷积中的3
    dist = cv.distanceTransform(nb,cv.DIST_L2,3)
    # 距离变换结果  0-1.0程度
    dist_output = cv.normalize(dist ,0,1.0,cv.NORM_MINMAX)
    cv.imshow("dist_output",dist_output*50)

    ret,surface = cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface",surface)
    # markers
    surface_fg = np.uint8(surface)
    # unknown 为着色准备
    unknown = cv.subtract(sure_bg,surface_fg)
    # 找到markers
    ret,markers = cv.connectedComponents(surface_fg)
    print(ret)

    # 分水岭变换
    markers = markers + 1
    # unknown 象素操作   markers[unknown==255] =0
    markers[unknown==255] = 0
    markers = cv.watershed(img,markers=markers)
    img[markers==-1] = [255,255,0]
    cv.imshow("img",img)

    print(img.shape)

img = cv.imread("yuan.jpg")
print('创建成功')
cv.imshow('ljw',img)
watered_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()


