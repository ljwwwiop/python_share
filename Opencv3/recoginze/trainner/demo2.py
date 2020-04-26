'''
    加载人脸识别器
    加载 training中的 yml 训练文件
'''
import numpy as np
import cv2
from PIL import Image,ImageFont

# 导入
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("lianData.yml")
# 再来一个检测 奥巴马的
# recognizer2 = cv2.face.LBPHFaceRecognizer_create()
# recognizer2.read("AoBaMa.yml")

# 使用haar级联来创建一个用于人脸检测的级联分类器，假设你在同一个位置有级联文件
cascadePath = r"D:\python\whl\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
# 创建摄像头 捕获对象 r"D:\python\爬虫\video\小鲜肉拳击冠军,爱护肤自称吴彦祖.mp4"
cam = cv2.VideoCapture(0)
# 设置描述字体 python3 中 cv2.putText()
font = cv2.FONT_HERSHEY_SIMPLEX
# font = ImageFont.truetype(r'D:\python\pycharm\ziti\simhei.ttf',20)


# 开始循环
while True:
    ret ,frame = cam.read()
    # frame = cv2.imread(r"D:\python\pycharm\Opencv3\recoginze\pic_data\AOBAMA\face-1.jpg")
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.2,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w-15,y+h-15),(0,0,255),2)
        # 这个地方是和普通的人脸检测区别的地方
        # 用户ID和预测的置信度，我们在面部下方的屏幕中写入用户ID，即（x，y + h）坐标
        # recognizer.predict为预测函数

        # 这个时检测我的
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        # print(Id)
        print("ID：", Id ,"conf2 = " , conf)
        # 添加其他操作 conf 越小越精确
        if(conf < 50 ):
            # Id = "LianJiaWei" 根据Id 得到的结果判断
            if(Id ==23 ):
                Id = "LianJiaWei"
            elif(Id ==48):
                Id ="LianJiaWei"
            elif(Id == 41):
                Id="LianJiaWei"
        else:
            Id ="Unknown"
            # 图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
        cv2.putText(frame, str(Id), (x, y - 30), font,0.55, (0,255,0), 2)
    cv2.imshow("cam",frame)
    if cv2.waitKey(10) ==27:
        break

cam.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
