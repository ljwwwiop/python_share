import cv2
import numpy as np

a = cv2.imread('d.jpg', 1)
b = np.zeros(a.shape, dtype=np.uint8)
b[100:200, 200:250] = 255
# todo b表示的就是掩摸，在抠图的过程中，掩摸的制作往往是很重要且很难的
c = cv2.bitwise_and(a, b)
cv2.imwrite('br.jpg', b)
cv2.imwrite('cr.jpg', c)

cv2.imshow('a', a)
cv2.imshow('b', b)
cv2.imshow('c', c)
cv2.waitKey()
cv2.destroyAllWindows()

