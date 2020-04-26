'''
    图像金字塔 原理 高斯模糊 + 降采样  必须一步一步来
    expand = 扩大 + 卷积
    拉普拉斯金字塔  可以直接一步到位 L1 = g1 -EXPAND(g2) 计算量较小
    PyrDOWN 降采样 PyrUP 还原
    智能使用图片是2**n的 偶数次方的 奇数的 需要自己处理一下成为2 的倍数的
'''
import cv2 as cv
import numpy as np

# 降采样
def pyramid_demo(img):
    # 层数
    level = 3
    temp = img.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("num"+str(i)+"s",dst)
        temp = dst.copy()
    return pyramid_images

# 拉普拉斯方法 还原
def lapalian_demo(img):
    pyramid_images = pyramid_demo(img)
    level = len(pyramid_images)
    for i in range(level-1,-1,-1):
        if(i-1)<0:
            # 处理最后一层 防止 i <0时候 没有输出最后一张原图
            expand = cv.pyrUp(pyramid_images[i],dstsize=img.shape[:2])
            lpls = cv.subtract(img,expand)
            cv.imshow("lalp"+str(i),lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i],dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1],expand)
            cv.imshow("lapalian_down"+str(i),lpls)

img = cv.imread("timg (1).jpg")
# 图片必须是 2的倍数的
print('创建成功')
cv.imshow('ljw',img)
lapalian_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()

