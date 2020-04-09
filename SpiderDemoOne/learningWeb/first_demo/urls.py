
from django.urls import path
from . import views

urlpatterns = [
    # 在include那边urls写入过了这边的path就可以省略  localhost:8000/
    path('<int:first_demo_id>', views.index, name='first_name'),
    path('list', views.content_list, name='content_list'),
]