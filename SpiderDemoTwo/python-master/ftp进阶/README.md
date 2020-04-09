Ftp程序：

	测试账号: 
		caoy/123
		alex/123

	ftp服务功能：
		1. 用户密码通过md5进行加密传输
		2. 允许多用户同时登陆ftp服务
		3. 每个用户连接上ftpserver进入自己的家目录,不允许访问家目录上级的目录,但可以在家目录里面进行自由切换
		4. 每个家目录限制了不同的使用大小,如果文件超过配额的使用大小,对文件不进行操作直接返回结果
		5. 可以查看ftpserver端家目录下的任意文件,使用ls命令
		6. 可以查看ftpclient端下的任意文件,使用lls命令
		7. 对ftpclient端的目录进行任意切换,使用lcd命令
		8. 文件传输后会进行md5值对比,确保传输的内容相同
		9. 上传、下载的传输过程中会出现进度条
		10. 上传、下载文件支持断点续传

	ftp服务命令：
		ls	# 查看服务端文件
		cd	# 切换服务端目录 
		get	# 下载文件
		put	# 上传文件
		lls	# 查看本机客户端文件
		lcd	# 切换客户端目录

	ftp服务文件说明：
	.
	├── ftpclient  # 客户端代码
	│   ├── bin   # 执行目录
	│   │   ├── __init__.py
	│   │   └── main.py   # 主程序执行文件
	│   ├── conf  # 配置文件
	│   │   ├── __init__.py
	│   │   └── settings.py   # 编码对应的含义
	│   ├── core # 主程序目录
	│   │   ├── client.py   # 客户端主代码
	│   │   ├── __init__.py
	│   └── __init__.py
	├── ftpserver  # server端代码
	│   ├── bin  # 执行目录
	│   │   ├── __init__.py  
	│   │   └── main.py   # 主程序执行文件
	│   ├── conf  # 配置文件
	│   │   ├── __init__.py
	│   │   └── settings.py  # 编码对应的含义
	│   ├── core
	│   │   ├── __init__.py
	│   │   └── server.py   # server端主程序
	│   ├── db  # 数据目录
	│   │   ├── alex.json   # alex用户认证文件
	│   │   ├── caoy.json    # caoy用户认证文件
	│   │   └── data  # 家目录上级
	│   │       ├── alex  # alex家目录
	│   │       └── caoy  # caoy家目录
	│   │           └── test  # 家目录下的目录
	│   └── __init__.py
	└── __init__.py
