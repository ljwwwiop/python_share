'''
    ROI 泛洪填充
'''
import cv2 as cv
import numpy as np

# 填充 改变图像 泛洪填充
def fill_color(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    # 像素的加减 并不是距离
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    #             demo , mask,seeDpoint, 颜色, 低值，高值，x+topx,y+topy, x-minx,y-miny
    cv.imshow("copying",copyImg)

# 第二张 only填充 不改变图像
def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("only",image)

    # mask 很重要 填充必须使用mask
    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(100,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("only2",image)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)

# # 部分 ry操作
# face = img[20:120,50:200]
# gray = cv.cvtColor(face , cv.COLOR_BGR2GRAY)
# # cv.imshow("new",gray)
# backface = cv.cvtColor(gray,cv.COLOR_BGR2GRAY)
# img[20:120,50:200] = backface
# cv.imshow("face",img)
# fill_color(img)
fill_binary()

cv.waitKey(0)
cv.destroyAllWindows()





