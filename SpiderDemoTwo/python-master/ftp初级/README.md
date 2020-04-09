简单ftp程序实现
测试账号: caoy
测试密码: 123

ftp
├── client.py  客户端执行程序
├── db
│   ├── auth   用户名密码目录
│   └── caoy   测试用户家目录
└── server.py  服务端执行程序

1.开启ftp服务端(python server.py)
2.ftp客户端连接(python client.py localhost 21)
3.用户名密码登陆，验证不通过可循环输入
3.不同用户家目录不同，不能切换到其他目录
4.可通过lcd切换本地路径
5.可通过lls查看本地路径当前目录下的文件
6.通过get filename对文件进行下载，下载路径为当前本地路径
7.通过put filename对本地文件进行上传，上传路径为家目录
8.通过ls -l命令查看家目录下的文件
9.输入q退出连接
