from django.shortcuts import render_to_response,get_object_or_404
# get_object_or_404 3个参数 模型，条件
# Create your views here.
from .models import First

def index(request,first_demo_id):
    '''
    这是一个处理用户的request的方法，并且是一个对象
    :param request: 用户所有请求信息不是字节
    :return: 返回信息
    HttpResponse只能返回字符串
    '''
    # return HttpResponse("hello world")
    # return render(request,'文件名')
    # 自动找到模板路径下面的login.html文件,读取并且返回给用户
    # 模板路径的配置
    first = get_object_or_404(First,pk=first_demo_id)
    # first = First.objects.get(id = first_demo_id)
    context = {}
    context['first_obj'] = first
    return render_to_response('test2.html', context)

def content_list(request):
    # 用户界面显示 all 是全部内容 filter 过滤
    first = First.objects.filter(is_delete=False)
    context = {}
    context['first'] = first
    return render_to_response('test3.html', context)

