import cv2 as cv
import numpy as np

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
cv.waitKey(0)
cv.destroyAllWindows()



