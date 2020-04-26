'''
    2019/1/27 开始学习opencv3
'''
import cv2 as cv

def get_imageinfo(image):
    print(type(image))
    # 长宽 还有 3通道得 3个方向
    print(image.shape)
    print(image.size)
    # 大小 size = 长*宽*通道
    print(image.dtype)
    #  类型

#   导入
img = cv.imread("timg (1).jpg")
print('创建成功')
# #创建窗口
# cv.namedWindow("out",cv.WINDOW_AUTOSIZE)
cv.imshow('ljw',img)
# get_imageinfo(img)
# #显示图片
# 灰度图片
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imwrite("one.png",gray)
cv.waitKey(0)
#关闭窗口
cv.destroyAllWindows()
