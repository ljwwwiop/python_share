#!/usr/bin/env python
import os
import sys
'''  
    账户 ljw 密码 lianjiawei123
    
    python manage.py makemigrations 编译数据库 1
    python manage.py migrate 跟新数据库 2
    启动  对当前django程序所有操作可以基于 python manage.py
        - setting.py django配置文件
        - url.py 路由系统 url - 函数
        - wsgi.pu 用于定义django用socket,wsgiref,uwsgi
        
    创建 project
    配置:
     template 目录
     template 模板路劲配置
     static 目录
     staticFILES 静态文件配置
     
    url 对应的关系
    get请求 --  只有request.get有值
    post请求  --  requests.get和requests.post都有值
    requests.get  -- 请求体
    requests.post  -- 请求头中的url中
    requests.method
'''

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learningWeb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
