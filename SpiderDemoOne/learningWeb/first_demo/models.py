from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
    定义模型  python manage.py makemigrations 迁移文件
    python manage.py migrate 数据库 应用上文件了

'''
class First(models.Model):
    # Char 类型 最大长度30
    title = models.CharField(max_length=30)
    # 内容 类型Text
    content = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后跟新时间
    last_update_time = models.DateTimeField(auto_now=True)
    # 制作者模型 delete不做操作
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    # 标记 是否删除
    is_delete = models.BooleanField(default=False)
    # 阅读数量
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return "<First:%s>"%self.title


