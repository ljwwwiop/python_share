from django.shortcuts import render_to_response,get_object_or_404,render
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import read_statistics_once_read
from comment.models import Comment
from comment.forms import CommentForm

'''
    Ctrl + R 全文件搜索
    truncatechars:20 过滤 content 的内容显示数字
    truncatewords:20 过滤英文单词  truncatewords_html
    循环 for 
    条件 if ,ifequal,ifnotequal,
    链接 url
    模板嵌套 block,extends,include
    注释 {# #}
    filter(title__contains='django')
    filter(title__in=[1,2,3,4,5])
    filter(title__range=(1,4))
    exclude(pk=3) 排除3以外的
'''

def get_blog_list_common_data(request,blogs_all_list):
    paginator = Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER) # 10页进行分页
    page_num = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number #获取当前页码
    page_range = list(range(max(current_page_num -2,1),current_page_num)) + \
                 list(range(current_page_num,min(current_page_num+2,paginator.num_pages) +1))
    # 中间加上省略号
    if page_range[0] -1 >=2:
        page_range.insert(0,"...")
    if paginator.num_pages - page_range[-1] >=2 :
        page_range.append("...")

    # 添加首尾
    if page_range[0] !=1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类的对应博客数量
    #BlogType.objects.annotate(blog_count = Count('blog'))
    '''
    blog_types = BlogType.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type = blog_type).count()
        blog_types_list.append(blog_type)
    '''
    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('create_time','month',order="DESC").annotate(blog_count = Count('create_time'))
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(create_time__year = blog_date.year,create_time__month = blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['page_range'] = page_range
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.annotate(blog_count = Count('blog'))
    context['blogs_count'] = Blog.objects.all().count()
    context['blog_dates'] = blog_dates_dict
    return context

# Create your views here.
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request,blogs_all_list)
    return render(request,'blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request,blog)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id = blog.pk)

    context = {}
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    context['blog'] = blog
    context['comments'] = comments

    context['comment_form'] = CommentForm(initial={'content_type':blog_content_type.model,'object_id':blog_pk})
    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie(read_cookie_key,'true') # 阅读cookie的标记
    return response

def blogs_with_type(request,blog_type_pk):

    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type

    return render(request,'blog/blogs_with_type.html',context)


def blogs_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(create_time__year=year,create_time__month=month)

    context = get_blog_list_common_data(request,blogs_all_list)
    context['blogs_with_date'] = '%s年%s月'%(year,month)

    return render(request,'blog/blogs_with_date.html',context)