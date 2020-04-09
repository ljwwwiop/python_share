有以下员工信息表
staff_id	name	age	phone	dept	enroll_date	
1	Alex Li	22	13651054608	Market	2013-04-01	
2	Jack Wang	30	13304320533	Market	2015-05-03	
3	Rain Liu	25	13832355322	Sales	2916-04-22	
4	Mack Cao	40	13561453436	HR	2009-03-01	
现需要对这个员工信息文件，实现增删改查操作

可进行模糊查询,不区分selec、from、where等关键字的大小写,通过各种条件进行查找:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面显示查到的条数 
可创建新员工纪录，以phone做唯一键不能与以有的phone相同，staff_id需自增不可更改
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"

代码结构
staff_info
	core
		main.py       ---》函数主入口
		change.py     ---》update/select获取变量值
		handle.py     ---》update/select找出满足条件的语句
		file.py       ---》文件处理函数
		select.py     ---》select语句主函数
		update.py     ---》update语句主函数
		addition.py   ---》添加员工信息函数
		uninstall.py  ---》删除函数
		staff_table   ---》员工信息表
		
		
		
		
