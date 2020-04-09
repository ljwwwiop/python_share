# Welcome to Caoy Home

login.py 
	流程说明：(测试用户'caoy':"123456",'admin':'123456')
		1. 执行方法：python login.py
		2. 输入用户名密码
		3. 查看lockfile文件中输入的用户名是否存在
		4. 存在lockfile文件中的用户直接退出
		5. 不存在lockfile文件中的用户进入用户名密码验证环节
		6. 用户名密码验证通过打印Welcom并退出
		7. 用户名或密码未通过进入循环重新输入用户名密码
		8. 用户名密码通过转入第6步
		9. 用户名密码未通过并输错3次，用户拉入lockfile文件
	
		
博客地址：http://www.cnblogs.com/sshcy/p/7754594.html