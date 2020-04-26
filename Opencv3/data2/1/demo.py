'''
    模板匹配 是模式匹配里面最基础的一种方式
    从左到右 从上到下 计算图像与重叠子图的匹配度
    相关性 = 1 相似很高   相关性因子  平方
    积分图 在进行计算 速度提高很多
'''


import cv2 as cv
import numpy as np

def template_demo():
    #"target.png"  "timg (1).jpg"
    tpl = cv.imread("target.png")
    target = cv.imread("timg (1).jpg")
    cv.imshow("tpl",tpl)
    cv.imshow("target",target)
    # 选择方法 平方  相关性 相关性因子
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,max_loc,min_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)
        # 绘制矩形 图片 左上顶点  右下顶点2个  颜色红色  粗细
        cv.rectangle(target,tl,br,(0,0,255),2)
        # cv.imshow("match"+np.str(md),target)
        cv.imshow("result"+np.str(md),result)

img = cv.imread("timg (1).jpg")
print('创建成功')
# cv.imshow('ljw',img)
template_demo()

cv.waitKey(0)
cv.destroyAllWindows()