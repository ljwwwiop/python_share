'''
    数据集生成器
    采集图片 采样
'''
import cv2

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier(r"D:\python\whl\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
i=0
# offset = 50  偏移 可用可不用
name=input('enter your id: ')
while True:
    ret, im =cam.read()
    # im = cv2.imread(r"D:\python\pycharm\Opencv3\recoginze\pic_data\AOBAMA\face-4.jpg")
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, 1.2,3)
    for(x,y,w,h) in faces:
        # 对象 起点 终点  颜色 粗细
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        i = i +1
        cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('im',im)
    if cv2.waitKey(20) == 27:
        break
    if i>=3:
       break

cam.release()
cv2.destroyAllWindows()


