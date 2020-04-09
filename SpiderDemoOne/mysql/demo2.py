# -*- coding:UTF-8 -*-

import pymysql
from tkinter import *
from tkinter import messagebox

#全查询
def get_find():
    db = pymysql.connect("localhost","root","root","abc",charset='utf8')
    cursor = db.cursor()
    sql='select * from lesson where snum=%d'
    try:
        cursor.execute(sql % (a))
        r=cursor.fetchall()
        xian_shi(r)
        # for i in r:
        #     a=i[0]
        #     b=i[1]
        #     c=i[2]
        #     print(a,b,c)
    except Exception as e:
        db.rollback()
    finally:
        db.close()

#查学分
# def get_xuefen():
#     db = pymysql.connect("localhost","root","root","abc",charset='utf8')
#     cursor = db.cursor()
#     sql='select * from xuefen where snum=%d'
#     try:
#         cursor.execute(sql % (319))
#         r=cursor.fetchall()
#         xian_shi(r)
#         # for i in r:
#         #     a=i[0]
#         #     b=i[1]
#         #     c=i[2]
#         #     print(a,b,c)
#     except Exception as e:
#         db.rollback()
#     finally:
#         db.close()




master = Tk()
master.title('v1.0----mysql学生微助手')
master.geometry('600x500')
master.resizable(width=False,height=False)

root=Canvas(master,width=600,height=140,bg='white')

image_file=PhotoImage(file='u=837769845,2678223074&fm=27&gp=0.jpg')

root.create_image(125,35, anchor='nw', image=image_file)

root.pack(side='top')

label1=Label(master,text="学号",font=('GB2312D',18),fg='black',bg='white')
label1.place(x=0, y=152)

label2=Label(master,text="姓名",font=('GB2312D',18),fg='black',bg='white')
label2.place(x=300, y=152)

entry1=Entry(master,font=('GB2312D',18),width=18,bd=4,bg='lightgray')
entry1.place(x=50,y=152)

entry2=Entry(master,font=('GB2312D',18),width=18,bd=4,bg='lightgray')
entry2.place(x=350,y=152)

button1=Button(master,text='成绩',bd=4,activeforeground='gray',font=('GB2312D'),width=10,command=get_find)
button2=Button(master,text='学分',bd=4,activeforeground='gray',font=('GB2312D'),width=10)
button3=Button(master,text='排名',bd=4,activeforeground='gray',font=('GB2312D'),width=10)
button4=Button(master,text='查课',bd=4,activeforeground='gray',font=('GB2312D'),width=10)
button5=Button(master,text='修改',bd=4,activeforeground='gray',font=('GB2312D'),width=10)

button1.place(x=65,y=190)
button2.place(y=190,x=165)
button3.place(x=265,y=190)
button4.place(y=190,x=365)
button5.place(y=190,x=465)


def xian_shi(n):
    theLB = Listbox(master,selectmode=MULTIPLE,width=50,heigh=10)
    for i in n:
        theLB.insert(0,i)
    theLB.pack(side=LEFT)
    theButton = Button(master, text='删除', command=lambda x=theLB: x.delete(ACTIVE))
    theButton.pack(side=LEFT)

master.mainloop()