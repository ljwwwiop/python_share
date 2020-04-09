from django.contrib import admin
from .models import BlogType,Blog

# Register your models here.
# 注册
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','content','title','author','get_read_num','create_time','last_update_time','is_delete')



