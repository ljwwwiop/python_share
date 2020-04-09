from django.contrib import admin
from .models import First

# Register your models here.

@admin.register(First)
class FirstAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","author","create_time","last_update_time","read_num","is_delete")

    # id 降序
    ordering = ("id",)


# admin.site.register(First,FirstAdmin)


