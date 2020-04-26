'''
    高斯模糊  和 高斯噪音
'''
import cv2 as cv
import numpy as np

def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv

# 高斯噪声  高斯模糊， 对高斯噪声有一定的抑制作用
def gaosi_nosie(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]   # blue
            g = image[row,col,1]   # blue
            r = image[row,col,2]   # blue
            image[row,col,0 ] =  clamp(b + s[0])
            image[row, col, 1] = clamp(b + s[1])
            image[row, col, 2] = clamp(b + s[2])
    cv.imshow("image",image)



img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
t1 = cv.getCPUTickCount()
gaosi_nosie(img)
t2 = cv.getCPUTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time:{}".format(time*1000))

# 高斯模糊 轮廓在 ，画面模糊 噪声对 模糊影响很小
dst = cv.GaussianBlur(img,(3,3),0)
#             这个地方的值 是高斯分布的公式分布  ，变量和参量 (x,y) & 二选一给值
cv.imshow("Gaussi",dst)
cv.waitKey(0)
cv.destroyAllWindows()



