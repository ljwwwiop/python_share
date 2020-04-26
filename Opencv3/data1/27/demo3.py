'''
    Opencv3 色彩空间 处理 inrange
    通道分离，与合并
    像素 的 + - * /
    dst = cv.add(m1,m2)
    cv.imshow("",dst)
    逻辑运算
    dst = cv.bitwise_or(m1,m2)
    cv.imshow("",dst)
    dst = cv.bitwise_not(image)
    cv.imshow("",dst)
'''
import cv2 as cv
import numpy as np

# 目标追踪
def extract():
    capture = cv.VideoCapture(r"D:\python\爬虫\video\小鲜肉拳击冠军,爱护肤自称吴彦祖.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 低 高 值填入
        low_hsv = np.array([0,43,46])
        high_hsv = np.array([10,255,255])
        change = cv.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
        dst = cv.bitwise_and(frame,frame,mask=change)
        # cv.imshow("video",frame)
        cv.imshow("video",dst)
        c = cv.waitKey(100)
        if c ==27:
            break

# 提高亮度
def contrast_image(image, c, b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("new",dst)
# hsv 与RGB转换
# YUV 和 RGB转换
def color_space_demo(image):
    # 灰度处理
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    # hsv 处理
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    # yuv 处理
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    # ycrcb 处理
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
# color_space_demo(img)
# extract()

# 1.2 对比度  10 为亮度
contrast_image(img,1.2,10)
# 分离
# b,g,r = cv.split(img)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# # 合并
# img[:,:,2] = 0
# img = cv.merge([b,g,r])
# cv.imshow("change_image",img)



cv.waitKey(0)
#关闭窗口
cv.destroyAllWindows()




