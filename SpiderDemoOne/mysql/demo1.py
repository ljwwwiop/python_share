# -*- coding:UTF-8 -*-
#!/usr/bin/python
#插入数据

import pymysql

db = pymysql.connect("localhost","root","root","liandb",charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql='select * from texta where id=%d'

try:
	cursor.execute(sql % (2))
	r=cursor.fetchall()   #这一条是将单个的查询后的数据保存起来，不过结果是列表结构
	print('id','no','name')
	for i in r :
		a=i[0]
		b=i[1]
		c=i[2]
		print(a,b,c)
	db.commit()
except Exception as e:
	db.rollback()
finally:
	db.close()
