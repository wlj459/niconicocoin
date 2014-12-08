#-*- coding:utf-8 -*-
from django.contrib import admin

from models import *


class ArticleAdmin(admin.ModelAdmin):#文章类admin后台显示以及tinymce
    list_display = ('title','show','time')
    fields=('title','show','content')
    class Media:
        js = (
        '/static/js/tinymce/tinymce.min.js',
        '/static/js/tinymce/config.js',
        )


class LinkAdmin(admin.ModelAdmin):#友情链接admin后台
    list_display = ('title','show','time')
    fields=('title','image','url','show')


class MyModelAdmin(admin.ModelAdmin):#课件下载admin重构
    list_display = ('title','show','time')
    fields=('title','show','course')
    def save_model(self, request, obj, form, change):#保存上传的admin账户
        if change:
            obj_original=self.model.objects.get(pk=obj.pk)
        else:
            obj_original=None

        obj.author=request.user
        obj.save()
    def get_queryset(self,request):#重构权限，非超级管理员只能看到自己编辑的文件
        qs=super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
admin.site.register(College,ArticleAdmin)
admin.site.register(Faculty,ArticleAdmin)
admin.site.register(Recruit,ArticleAdmin)
admin.site.register(News,ArticleAdmin)
admin.site.register(Notice,ArticleAdmin)
admin.site.register(CourseWare,MyModelAdmin)
admin.site.register(International,ArticleAdmin)
admin.site.register(Rule,ArticleAdmin)
admin.site.register(Employment,ArticleAdmin)
admin.site.register(Link,LinkAdmin)
