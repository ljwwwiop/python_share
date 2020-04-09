import requests
import re
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
# 学会的如何tkinter 上面显示图片

def Fonts(event):
    # 330,22，313，901，364
    # 这个函数传入参数必须要有这个event 参数
    choose = comvalueBox.get()
    choose = choose.strip()
    f = get_num()
    f(choose)



# 闭包解决问题了
def get_num():
    def parge_demo(choose):
        data = {
            "黑体":'330',
            "连笔手写字":'22',
            "仿宋":'313',
            "明星手写体":'901',
            "艺术体":'364',
            "亲笔设计+Q1206957838":'901',
        }
        a = data.get("{}".format(choose)).strip()
        print(a)
        return a
    return parge_demo


def get_sign(t):
    starturl = 'http://www.jiqie.com/a/14.htm'
    name = entry.get()
    name = name.strip()
    temp = str(t)
    print("temp:%s"%temp)
    if name =="":
        messagebox.showinfo("提示","请输入正确的姓名")
    else:
        # fontsIndex = Fonts()
        data = {
            'id': name,
            'idi': 'jiqie',
            'id1': temp,#'330'  # 传入字体参数
            'id2':  '#FCFCFC',
            'id3':'',
            'id4':  '# FF0000',
            'id5':'',
            'id6':  '#DEDE4A'
        }

        result = requests.post(starturl,data=data)
        result.encoding='utf-8'
        html = result.text
        # print(html)

        pat = re.findall('<img src="(.*?)">',html)
        for i in pat:
            pic = requests.get(i)
            with open("{}.jpg".format(name),'wb') as f:
                f.write(pic.content)
                f.close()
        img = Image.open('{}.jpg'.format(name))
        img_jpg = ImageTk.PhotoImage(img)
        Finally(img_jpg)



def Finally(img_jpg):
    # img = Image.open('1.jpg')
    # img_jpg = ImageTk.PhotoImage(img)
    label = Label(root,image=img_jpg)
    label.image = img_jpg
    label.place(x=50,y=50)
    # label.grid(row=2,column=1)
    # canvas = Canvas(root,width=400,height=500)
    # # canvas.pack()
    # IMG = img
    # canvas.create_image(0,20,image = IMG)

# GUI 代码部分
if __name__ =='__main__':
    root = Tk()

    root.title("签名设计----v1.0")
    root.geometry("550x400")
    # 初始化位置
    root.geometry("+350+150")
    label = Label(root,text = "输入内容",font=("微软雅黑",20),fg = 'black')
    label.grid(row=0,column=0)
    entry = Entry(root,font=("宋体",25),width=10)
    entry.grid(row=0,column=1)

    # 选择字体
    label = Label(root,text="字体",font=("微软雅黑",10),fg='red')
    label.grid(row=0,column=6,sticky=W)
    comvalue = StringVar() # 窗体文本对象 自带的
    comvalueBox = ttk.Combobox(root,textvariable=comvalue ) # 初始化
    comvalueBox["values"] = ("黑体","连笔手写字","仿宋","明星手写体","艺术体","亲笔设计+Q1206957838")
    # 330,22，313，901，364
    comvalueBox.current(0) # 选择第一个
    comvalueBox.bind("<<ComboboxSelected>>",Fonts) # 绑定事件 Fonts 函数
    comvalueBox.grid(row=0,column=7,sticky=W)

    button = Button(root,text="立即设计",font=("微软雅黑",10),command = get_sign,fg='red')
    button.grid(row=0,column=8,sticky=E)

    root.mainloop()

