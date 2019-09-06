from django.urls import path
from . import views

urlpatterns = [
    # 在include那边urls写入过了这边的path就可以省略  localhost:8000/blog/1
    # path('<int:first_demo_id>', views.index, name='first_name'),
    # path('list', views.content_list, name='content_list'),
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name="blogs_with_type"),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date'),
]