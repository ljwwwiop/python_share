'''
    opencv3 中 numpy科学计算工具得用法
    数组得处理
    选择正确得float or int 后面运算比较好
'''
import cv2 as cv
import numpy as np

# 对所有像素访问
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width:{},height:{},channels:{}".format(height,width,channels))
    # 获取所有像素
    for row in range(height):
        for cal in range(width):
            for a in range(channels):
                pv = image[row,cal,a]
                image[row,cal,a] = 255 - pv
    cv.imshow("new_image",image)

# 直接使用了 cv中自带得c语言写好的库进行取素
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)

# 创建新得图像
def create_image():
    '''
    # 自己定义一个新的图片 默认黑色
    img = np.zeros([200,200,3],np.uint8)
    # 修改第一个通道值
    # img[ : , : , 0] = np.ones([200,200]) * 255
    img[:, :, 2] = np.ones([200, 200]) * 255
    cv.imshow("new2 image",img)
    '''
    # 单通道赋值
    # img = np.ones([200,200,1],np.uint8)
    # img = img * 127
    # cv.imshow("new2 image", img)
    m1 = np.ones([3,3],np.int8)
    m1.fill(12.88)
    print(m1)

    m2 = m1.reshape([1,9])
    print(m2)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
# 时间预估
t1 = cv.getCPUTickCount()
inverse(img)
t2 = cv.getCPUTickCount()
time = ((t2-t1)/cv.getTickFrequency())
print("time:{}".format(time*1000))

cv.waitKey(0)
#关闭窗口
cv.destroyAllWindows()

















