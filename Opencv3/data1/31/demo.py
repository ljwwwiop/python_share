'''
    直方图应用 均衡化 自动调整对比度 图像增强的手段
    一般都是Gray灰度处理  直方图只认识gray
    直方图对比  判断图片相似性  巴氏距离  相关性  卡方
'''
import cv2 as cv
import numpy as np

# 均衡化两种方法 增强对比度的  适合较黑色的
def equalHist_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("dst",dst)

# 自然处理直方图 不会过分处理 局部的
def clahe_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    # 默认是 40 太高了 调低   大小 CL 是对比度
    dst = clahe.apply(gray)
    cv.imshow("dst",dst)

def create_rgb_hist(img):
    # 创造一个三通道的直方图
    h,w,c = img.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256/16
    # 遍历
    for row in range(h):
        for col in range(w):
            b = img[row,col,0]
            g = img[row, col, 1]
            r = img[row, col, 2]
            # index 不可以为浮点是数
            index = np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0]+1
    return rgbHist

def hist_compare(image1,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA) # 调用巴氏距离  越大越相似
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL) # 相关性  越大越想
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR) # 卡方   越大越不想
    print("巴氏距离:{},相关性:{},卡方:{}".format(match1,match2,match3))


img = cv.imread("timg (1).jpg")
img2 = cv.imread("man.jpg")
print('创建成功')
cv.imshow('ljw',img)
cv.imshow('ljw2',img2)
hist_compare(img,img2)

cv.waitKey(0)
cv.destroyAllWindows()

