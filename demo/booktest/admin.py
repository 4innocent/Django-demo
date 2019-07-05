from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo

# 修改后台管理页面显示
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ("id","btitle","bpub_date")


# 修改后台管理页面显示
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ("id","hname","hgender","hcomment")

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)  # 向后台管理页面注册表单
admin.site.register(HeroInfo,HeroInfoAdmin)