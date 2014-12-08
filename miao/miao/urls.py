#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls),name='admin'),#admin管理后台
    url(r'^$','coin.views.index',name='index'),#首页
    url(r'^college/$','coin.views.college',name='college'),#学院概况
    url(r'^faculties/$','coin.views.faculty',name='faculty'),#师资队伍
    url(r'^recruits/$','coin.views.recruit',name='recruit'),#招生动态
    url(r'^news/$','coin.views.news',name='news'),#新闻
    url(r'^notices/$','coin.views.notice',name='notice'),#通知
    url(r'^courseware/$','coin.views.courseware',name='courseware'),#课件下载
    url(r'^communications/$','coin.views.communication',name='communication'),#国际交流
    url(r'^rules/$','coin.views.rule',name='rule'),#规章制度
    url(r'^employments/$','coin.views.employment',name='employment'),#就业信息
    url(r'^links/$','coin.views.link',name='link'),#友情链接
    url(r'^menu/$','coin.views.menu',name='menu'),#iframe菜单
    url(r'^connection/$','coin.views.connection',name='connection'),#联系我们
    url(r'^media/media/(?P<path>.*)$','django.views.static.serve',\
        {'document_root':settings.MEDIA_ROOT+'media'}),#课件下载文件连接
    url(r'^search/$','coin.views.search',name='search'),#搜索
    )