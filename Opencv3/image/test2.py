import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读入的图像是BGR空间图像
frame = cv2.imread(r"D:\python\pycharm\Opencv3\image\b.jpg")
b = np.zeros(frame.shape, dtype=np.uint8)

b[100:200, 100:200] = 255
c = cv2.bitwise_and(frame, b)


cv2.imwrite('shape_mask.jpg', b)
cv2.imwrite('shape.jpg', c)

# 部分1：将BGR空间的图片转换到HSV空间
hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

# 部分2：
# 在HSV空间中定义蓝色
lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])
# 在HSV空间中定义绿色
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
# 在HSV空间中定义红色
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 部分3：
# 从HSV图像中截取出蓝色、绿色、红色，即获得相应的掩膜
# cv2.inRange()函数是设置阈值去除背景部分，得到想要的区域
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
green_mask = cv2.inRange(hsv, lower_green, upper_green)
red_mask = cv2.inRange(hsv, lower_red, upper_red)

# 部分4：
# 将原图像和mask(掩膜)进行按位与
blue_res = cv2.bitwise_and(frame, frame, mask=blue_mask)
green_res = cv2.bitwise_and(frame, frame, mask=green_mask)
red_res = cv2.bitwise_and(frame, frame, mask=red_mask)

# 最后得到要分离出的颜色图像
res = blue_res + green_res + red_res

# 部分5:将BGR空间下的图片转换成RGB空间下的图片
frame = frame[:, :, ::-1]
blue_res = blue_res[:, :, ::-1]
green_res = green_res[:, :, ::-1]
red_res = red_res[:, :, ::-1]
res = res[:, :, ::-1]
# mask 定义大小


# 部分6：显示图像
plt.figure(figsize=(14, 12))
plt.subplot(2, 2, 1), plt.title('original_image'), plt.imshow(frame)
plt.subplot(2, 2, 2), plt.imshow(blue_mask, cmap='gray')
plt.subplot(2, 2, 3), plt.imshow(green_mask, cmap='gray')
plt.subplot(2, 2, 4), plt.imshow(red_mask, cmap='gray')


plt.figure(figsize=(14, 12))
plt.subplot(2, 2, 1), plt.imshow(blue_res)
plt.subplot(2, 2, 2), plt.imshow(green_res)
plt.subplot(2, 2, 3), plt.imshow(red_res)
plt.subplot(2, 2, 4), plt.imshow(res)
plt.show()
plt.imsave("blue.jpg",blue_res)
plt.imsave("green.jpg",green_res)
plt.imsave("red.jpg",red_res)
plt.imsave("res.jpg",res)
