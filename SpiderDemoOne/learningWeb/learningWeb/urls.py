"""learningWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    # 总路由
"""
from django.contrib import admin
from django.urls import path,include
from first_demo.views import index,content_list
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import HttpResponse,render,redirect



def good(request):

    # return HttpResponse("<input type='text'/>")
    if request.method =='GET':
        return render(request,'test.html')
    # post 请求走这里
    else:
        # 用户POST请求提交的东西 request.POST 生成一个字典
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        print(u,p)
        if u =='root' and p =='123456':
            # 登录成功后 redirect 跳转, 也可以直接url中的写入
            # return redirect('https://www.taobao.com')
            return redirect('/index/')
        else:
            # json 流数据出入 传出
            # 失败后 {'msg':''} 在html标签中写入{{msg}} 传入键值, name.0 取列表值,user_dict.k1 取字典
            return render(request,'test.html',
                          {
                              'msg':'用户名密码错误!',
                              'name':['撒比','的水平','啊大苏打'],
                              'user_dict':{'k1':'v1','k2':'v2'},
                              'user_list':[{'id':1,'name':'alex','email':'@qq.com'},
                                           {'id': 2, 'name': 'kitty', 'email': '@qq.com'},
                                           {'id': 3, 'name': 'ben', 'email': '@qq.com'}
                                           ]
                                               })



# 路由关系
urlpatterns = [
    path('',views.home,name='home'),

    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('blog/',include('blog.urls')),
    path('comment/',include('comment.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('well/',good),
    # path('index/',include('first_demo.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )
