'''
    图象梯度 反应象素梯度变化情况 反应边缘
    一阶导数与算子 soble 算子
    二阶导数与拉普拉斯算子
'''
import cv2 as cv
import numpy as np

# 拉普拉斯算子  默认的是 [0,1,0],[1,-4,1],[0,1,0]
# 自己可以定义一个 [1,1,1],[1,-8,1],[1,1,1]
def lapulasi_demo(img):
    dst = cv.Laplacian(img,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls",lpls)


# soble算子
def soble_demo(img):
    # Sobel Scharr是Sobel的增强版
    grad_x = cv.Scharr(img,cv.CV_32F,1,0)
    grad_y = cv.Scharr(img,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x",gradx)
    cv.imshow("y",grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("xy",gradxy)

def custom_demo(img):
    # 自己定义一个拉普拉斯算子
    kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    dst = cv.filter2D(img,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    # cv.convertScaleAbs 把他变成一个单通道的8位的 0-255象素的图象
    print(lpls.shape)
    cv.imshow("lpls",lpls)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
# soble_demo(img)
# lapulasi_demo(img)
custom_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()





