'''
    训练人脸识别器
    HARR 与 LBP区别
    ① HAAR特征是浮点数计算，LBP特征是整数计算；
    ② LBP训练需要的样本数量比HAAR大；
    ③ LBP的速度一般比HAAR快；
    ④ 同样的样本HAAR训练出来的检测结果要比LBP准确；
    ⑤ 扩大LBP的样本数据可达到HAAR的训练效果。
    Opencv3.0 样本训练集  基于LBP 特征提取   类似于局部定位  映射象素到直方图
    一中心位置为圆心  值为半斤画圆  小于半径值得全部为0  大于的全部为1  01111100
    写成2进制字符串  之后转化为10进制
'''
import cv2 as cv
import os
import numpy as np
from PIL import Image

# 初始化
# recognizer = cv.createLBPHFaceRecognizer()  这是py2 方式
recognizer = cv.face.LBPHFaceRecognizer_create()
detector = cv.CascadeClassifier(r"D:\python\whl\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
path = r'D:\python\pycharm\Opencv3\recoginze\test\dataSet\getBAMA'

# 加载图片
def getImageAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    # face
    faces = []
    # id
    ids = []
    for imagepath in imagePaths:
        # 把图片导入进来 L 为灰度图片
        pilImage = Image.open(imagepath).convert('L')
        imageNp = np.array(pilImage,'uint8')
        Id = int(os.path.split(imagepath)[-1].split(".")[0])
        # Id = int(os.path.split(imagepath)[-1].split(".")[0].split("_")[-2])
        print(Id,imageNp.shape)
        # 把 自己定义的 faces 加入 到xml中 x,y,w,h
        '''
        两种方式都可以
        一种(x,y,w,h) in face 
        另一种 直接 ids.append(Id) faces.append(imageNp)
        '''
        face = detector.detectMultiScale(imageNp)
        for (x,y,w,h) in face:
            faces.append(imageNp[y:y + h, x:x + w])
            ids.append(Id)
            cv.imshow("training",imageNp)
        cv.waitKey(10)
        # 返回值
    return ids,faces

getImageAndLabels(path)
id , faces =getImageAndLabels(path)
recognizer.train(faces,np.array(id))
recognizer.save(r'D:\python\pycharm\Opencv3\recoginze\trainner2\AoBaMa.yml')
cv.destroyAllWindows()


