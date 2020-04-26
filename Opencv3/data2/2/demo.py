'''
    图像二值化  把图像只表现出 黑和白 0 255
    二值化方法 openCV3.0 以后 API 才有 两种方法
    全局阈值
    局部阈值
'''
import cv2 as cv
import numpy as np

# 全局阈值
def threshold_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret , binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    '''
        cv.THRESH_OTSU 局部变量是自动切割的 ret 对应0 的位置 常用的
        如果去除掉|后面内容 则 ret 可以自己调整 如127
        cv.THRESH_TRIANGLE 是算阈值的 三角分割主要用于
        只有 直方图只有三个波峰的时候 效果最好  其余效果不太好  
        刚开始主要用于医学细胞 分割
    '''
    print("阈值：{}".format(ret))
    cv.imshow("img",binary)

# 局部阈值 是个好方法
def local_threshold(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,12)
    '''
        cv.adaptiveThreshold 这个是局部阈值的方法，在里面使用了2种
        可用的是 一个高斯方法  一个方格均值方法  二值化发方法cv.THRESH_BINARY
        blocksize 必须是奇数  cv.ADAPTIVE_THRESH_MEAN_C  cv.ADAPTIVE_THRESH_GAUSSIAN_C
        常量 10是每个方格的均值象素 方格中每个值 -10 大于10 为255 小于10 0
    '''
    cv.imshow("dst",dst)

# 自定义均值阈值  分割
def custom_threshold(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray,[1,w+h])
    mean = m.sum()/(w+h)
    print("mean:%s"%mean)
    ret,binary = cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    cv.imshow("MEAN",binary)


img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
# threshold_demo(img)
custom_threshold(img)

cv.waitKey(0)
cv.destroyAllWindows()



