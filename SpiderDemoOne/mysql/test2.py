from tkinter import *
from tkinter.messagebox import *
import pymysql
db = pymysql.connect("localhost","root","root","abc",charset='utf8')
root=Tk()
root.geometry('700x400')
root.resizable(width=True,height=True)
systitle='用户注册信息管理系统'
root.title(systitle)
pic=PhotoImage(file=r'u=837769845,2678223074&fm=27&gp=0.jpg')
label1=Label(image=pic)
label1.place(x=100,y=70)
mainframe=LabelFrame()
mainframe.pack()



def showall():
    global mainframe
    cu=db.cursor()
    cu.execute('select * from book')
    users=cu.fetchall()
    mainframe.destroy()
    if len(users)==0:
        showwarning(systitle,"当前无图书！")
    else:
        mainframe=LabelFrame(text='书库信息如下：')
        mainframe.pack(anchor=CENTER, pady=20, ipadx=5, ipady=5)
        mainframe.config(bg='')
        mainframe.columnconfigure(1,minsize=200)
        mainframe.columnconfigure(2,minsize=200)
        mainframe.columnconfigure(3, minsize=200)
        Label(mainframe, text='序号', font=('隶书', 15, 'bold'), bd=1, relief=SOLID).grid(row=1, column=1,
                                                                                       sticky=N + E + S + W)
        Label(mainframe,text='书名',font=('隶书',15,'bold'),bd=1,relief=SOLID).grid(row=1,column=2,sticky=N+E+S+W)
        Label(mainframe, text='价格', font=('隶书', 15, 'bold'), bd=1, relief=SOLID).grid(row=1, column=3,sticky=N + E + S + W)
        Label(mainframe, text='作者', font=('隶书', 15, 'bold'), bd=1, relief=SOLID).grid(row=1, column=4,sticky=N + E + S + W)
        rn=2
        for x in users:
            cn=1
            Label(mainframe,text=str(rn-1),font=('宋体',14),bd=1,relief=SOLID).grid(row=rn,column=cn,sticky=N+E+S+W)
            for a in x:
                cn+=1
                Label(mainframe,text=str(a),font=("宋体",14),bd=1,relief=SOLID).grid(row=rn,column=cn,sticky=N+E+S+W)
            rn+=1


def adduser():
    global mainframe
    mainframe.destroy()
    mainframe=LabelFrame(text='添加新用户：')
    mainframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)
    tf=Frame(mainframe)
    tf.pack()
    Label(tf,text='用户ID：',anchor=E).grid(row=1,column=1)
    userid=StringVar()
    txtuid=Entry(tf,textvariable=userid)
    txtuid.grid(row=1,column=2)
    Label(tf,text='密码：',anchor=E).grid(row=2,column=1,sticky=E)
    password=StringVar()
    txtpwd=Entry(tf,textvariable=password)
    txtpwd.grid(row=2,column=2)
    tf2=Frame(mainframe)
    tf2.pack()
    btclear=Button(tf2,text='重置')
    btclear.grid(row=1,column=1)
    btok=Button(tf2,text='保存')
    btok.grid(row=1,column=2)

    def clearall():
        userid.set("")
        password.set("")

    def savenew():
        uname=userid.get()
        pwd=password.get()
        if uname=="":
            showerror(systitle,'用户名输入无效！')
        else:
            if find(uname)==1:
                showerror(systitle,'你输入的用户名已经使用，请重新添加用户！')
                txtuid.focus()
            else:
                if pwd=="":
                    showerror(systitle,'登录密码输入无效！')
                else:
                    cn=conn.cursor()
                    cn.execute('insert into new_table1(userid,password) values (%s,%s)',(uname,pwd))
                    conn.commit()
                    showinfo(systitle,'已成功添加用户！')
    btclear.config(command=clearall)
    btok.config(command=savenew)


def find(namekey):
    cn=db.cursor()
    cn.execute('select * from new_table1 where userid=%s',(namekey,))
    user=cn.fetchall()
    if len(user)>0:
        n=1
    else:
        n=-1
    return n


def check_update():
    global mainframe
    mainframe.destroy()
    mainframe=LabelFrame(text='查找、修改或删除用户：')
    mainframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)
    tf=LabelFrame(mainframe,text='查找用户：')
    tf.pack(anchor=CENTER,pady=10,ipadx=5,ipady=5)
    Label(tf,text='请输入要查找的用户ID：',anchor=E).grid(row=1,column=1)
    userid=StringVar()
    txtuid=Entry(tf,textvariable=userid)
    txtuid.grid(row=1,column=2)
    btok=Button(tf,text='确定')
    btok.grid(row=1,column=3)
    editframe=LabelFrame(mainframe,text='删除或修改用户数据：')
    editframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)
    btdel=Button(editframe,text='删除用户',state=DISABLED)
    btdel.pack(anchor=NW)
    op=LabelFrame(editframe,text='修改用户：')
    op.pack(anchor=CENTER,pady=10,ipadx=5,ipady=5)
    Label(op,text='新用户ID：',anchor=E).grid(row=1,column=1)
    newuserid=StringVar()
    newtxtuid=Entry(op,textvariable=newuserid)
    newtxtuid.grid(row=1,column=2)
    Label(op,text='新密码：',anchor=E).grid(row=2,column=1,sticky=E)
    newpassword=StringVar()
    newtxtpwd=Entry(op,textvariable=newpassword)
    newtxtpwd.grid(row=2,column=2)
    bteditsave=Button(op,text='保存修改',state=DISABLED)
    bteditsave.grid(row=1,column=3,rowspan=2,sticky=N+E+S+W)
    def dofind():
        uname=userid.get()
        if find(uname)==-1:
            showinfo(systitle,'%s 还未注册！'%uname)
        else:
            btdel.config(state=NORMAL)
            bteditsave.config(state=NORMAL)
    def dodelete():
        uname=userid.get()
        if askokcancel('用户注册信息管理系统',"确认删除用户：%s?"%uname):
            cn=conn.cursor()
            cn.execute('delete from new_table1 where userid=%s',(uname,))
            conn.commit()
            showinfo(systitle,"成功删除用户：%s"%uname)
    def saveedit():
        uname=userid.get()
        newname=newuserid.get()
        if newname=="":
            showerror(systitle,'新的用户名输入错误：%s'%newname)
            newtxtuid.focus_set()
        else:
            if find(newname)==1:
                showerror(systitle,'你输入的用户名 %s已经使用：'%newname)
                newtxtuid.focus_set()
            else:
                pwd=newpassword.get()
                if pwd=="":
                    showerror(systitle,'你输入的密码无效！')
                    newtxtpwd.focus_set()
                else:
                    cn=conn.cursor()
                    cn.execute('update new_table1 set userid=%s,password=%s where userid=%s',(newname,pwd,uname))
                    conn.commit()
                    showinfo(systitle,'已成功修改用户数据！')
    btok.config(command=dofind)
    btdel.config(command=dodelete)
    bteditsave.config(command=saveedit)


def goexit():
    if askokcancel('用户注册信息管理系统',"确认退出系统？"):
        root.destroy()




menubar=Menu(root)
root.config(menu=menubar)
file=Menu(menubar,tearoff=0)
file.add_command(label='显示全部图书信息',command=showall)
file.add_command(label='查找/修改/删除用户信息',command=check_update)
file.add_command(label='添加新用户',command=adduser)
file.add_separator()
file.add_command(label='退出',command=goexit)
menubar.add_cascade(label='系统操作菜单',menu=file)
root.mainloop()

