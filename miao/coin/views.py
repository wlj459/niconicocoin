# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response,HttpResponse
from django.core.servers.basehttp import  FileWrapper
import mimetypes
import os
from itertools import chain

from miao import settings
from adm.models import *


def index(request):#首页
    news = News.objects.order_by('-id').filter(show=True)[:5]
    notices = Notice.objects.order_by('-id').filter(show=True)[:5]
    return render_to_response('index.html', {'news': news, 'notices': notices})


def college(request):#学院概况
    news = College.objects.order_by('-id').filter(show=True)[:1]
    for i in news:

        i.click += 1
        i.save()

        return render_to_response('content-text.html', {'obj': u'学院概况', 'article': i,'url_name':'college'})
    return render_to_response('content-text.html', {'obj': u'学院概况','url_name':'college'})#概况为空时

def faculty(request):#师资队伍
    ID = request.GET.get('ID')
    pagenum = request.GET.get('pagenum')
    if ID is None:#列表
        if pagenum is not None:
            pagenum = int(pagenum)
        else:
            return render_to_response('content-list.html', {'obj': u'师资队伍','url_name':faculty})#为空
        news = Faculty.objects.order_by('-id').filter(show=True)

        len_num = len(news)#页码处理
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num /10
        nums = []

        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'师资队伍',
                                                        'lists': news[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums': nums,
                                                        'url_name': 'faculty'})
    else:#访问文章
        news = Faculty.objects.get(id=ID)

        news.click += 1#点击次数
        news.save()

        return render_to_response('content-text.html', {'obj': u'师资队伍', 'article': news,'url_name':'faculty'})


def recruit(request):#招生动态
    ID=request.GET.get('ID')
    pagenum=request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum = int(pagenum)
        else:
            return render_to_response('content-list.html', {'obj': u'招生动态','url_name':'recruit'})

        news = Recruit.objects.order_by('-id').filter(show=True)
        len_num = len(news)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num /10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'招生动态',
                                                        'lists': news[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums': nums,
                                                        'url_name': 'recruit'})
    else:
        news = Recruit.objects.get(id=ID)

        news.click+=1
        news.save()

        return render_to_response('content-text.html', {'obj': u'招生动态', 'article': news,'url_name':'recruit'})


def news(request):#新闻动态
    ID=request.GET.get('ID')
    pagenum = request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum = int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'新闻动态','url_name':'news'})

        news = News.objects.order_by('-id').filter(show=True)
        len_num = len(news)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num /10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'新闻动态',
                                                        'lists': news[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums': nums,
                                                        'url_name': 'news'})
    else:
        news = News.objects.get(id=ID)

        news.click += 1
        news.save()

        return render_to_response('content-text.html', {'obj': u'新闻动态', 'article': news,'url_name':'news'})


def notice(request):#通知
    ID = request.GET.get('ID')
    pagenum = request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum = int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'通知公告','url_name':'notice'})

        notices = Notice.objects.order_by('-id').filter(show=True)
        len_num = len(notices)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num / 10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'通知公告',
                                                        'lists': notices[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums':nums,
                                                        'url_name': 'notice'})
    else:
        news = Notice.objects.get(id=ID)

        news.click+=1
        news.save()

        return render_to_response('content-text.html', {'obj': u'通知公告', 'article': news,'url_name':'notice'})


def courseware(request):#课件下载
    ID = request.GET.get('ID')
    pagenum = request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum = int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'通知公告','url_name':'notice'})

        coursewares = CourseWare.objects.order_by('-id').filter(show=True)
        len_num = len(coursewares)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num /10

        return render_to_response('content-list.html', {'obj':u'课件下载',
                                                            'lists': coursewares[(pagenum-1) * 10: min(pagenum * 10, len_num)],
                                                            'pagenum': num,
                                                            'url_name':'courseware'})
    # else:
    #     filepath = os.path.join(settings.MEDIA_ROOT,CourseWare.objects.get(id=ID).title)#需要改
    #     wrapper = FileWrapper(open(filepath, 'rb'))
    #     content_type = mimetypes.guess_type(filepath)[0]
    #     response = HttpResponse(wrapper,mimetypes='content_type')
    #     response['Content-Disposition'] = 'attachment; filename=%s' % CourseWare.objects.get(id=ID).title
    # # article={'content':'后台程序媛回家生猴子了'}
    # return render_to_response('content-text.html',{'obj': u'课件下载','article':article,'url_name':'courseware'} )
def communication(request):#国际交流
    ID=request.GET.get('ID')
    pagenum=request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum=int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'国际交流','url_name':'communication'})

        notices = International.objects.order_by('-id').filter(show=True)
        len_num = len(notices)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num / 10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'国际交流',
                                                        'lists': notices[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums':nums,
                                                        'url_name': 'communication'})
    else:
        news = International.objects.get(id=ID)

        news.click+=1
        news.save()

        return render_to_response('content-text.html', {'obj': u'国际交流', 'article': news,'url_name':'communication'})



def rule(request):#规章制度
    ID=request.GET.get('ID')
    pagenum=request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum=int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'规章制度','url_name':'rule'})

        notices = Rule.objects.order_by('-id').filter(show=True)
        len_num = len(notices)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num / 10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'规章制度',
                                                        'lists': notices[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums':nums,
                                                        'url_name': 'rule'})
    else:
        news = Rule.objects.get(id=ID)

        news.click+=1
        news.save()

        return render_to_response('content-text.html', {'obj': u'规章制度', 'article': news,'url_name': 'rule'})


def employment(request):#就业信息
    ID=request.GET.get('ID')
    pagenum=request.GET.get('pagenum')
    if ID is None:
        if pagenum is not None:
            pagenum=int(pagenum)
        else:
            return render_to_response('content-list.html',{'obj': u'就业信息','url_name': 'employment'})

        notices = Employment.objects.order_by('-id').filter(show=True)
        len_num = len(notices)
        if len_num % 10>0:
            num = len_num / 10 +1
        else:
            num = len_num / 10
        nums = []
        for i in range(0,num):
            nums.append(i+1)

        return render_to_response('content-list.html', {'obj': u'就业信息',
                                                        'lists': notices[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums': nums,
                                                        'url_name': 'employment'})

    else:
        news = Employment.objects.get(id=ID)

        news.click+=1
        news.save()

        return render_to_response('content-text.html', {'obj': u'就业信息', 'article': news,'url_name': 'employment'})


def link(request):#友情链接
    links=Link.objects.order_by('-id').filter(show=True)[:8]
    return render_to_response('content-link.html',{'lists': links,'url_name': 'link'})


def menu(request):#iframe框架
    return render_to_response('menu.html')


def connection(erquest):#联系我们
    return render_to_response('call me maybe.html')


def search(request):#搜索
    content = request.GET.get('content')
    if content is not None:
        content = content.encode('utf-8')
    pagenum = request.GET.get('pagenum')
    if pagenum is None:
        pagenum = 1
    else:
        pagenum = int(pagenum)
#搜索+合并
    lists = News.objects.filter(title__icontains=content)
    lists = chain(lists, News.objects.filter(content__icontains=content))
    lists = chain(lists, (CourseWare.objects.filter(title__icontains=content)))
    lists = chain(lists, Faculty.objects.filter(title__icontains=content))
    lists = chain(lists, Faculty.objects.filter(content__icontains=content))
    lists = chain(lists, Recruit.objects.filter(title__icontains=content))
    lists = chain(lists, Recruit.objects.filter(content__icontains=content))
    lists = chain(lists, Notice.objects.filter(title__icontains=content))
    lists = chain(lists, Notice.objects.filter(content__icontains=content))
    lists = chain(lists, International.objects.filter(title__icontains=content))
    lists = chain(lists, International.objects.filter(content__icontains=content))
    lists = chain(lists, Rule.objects.filter(title__icontains=content))
    lists = chain(lists, Rule.objects.filter(content__icontains=content))
    lists = chain(lists, Employment.objects.filter(title__icontains=content))
    lists = chain(lists, Employment.objects.filter(content__icontains=content))

    lists = sorted(lists, reverse = True, key = lambda x: (x.id))#排序

    len_num = len(lists)#页码
    if len_num % 10 > 0:
        num = len_num / 10 + 1
    else:
        num = len_num / 10
    nums = []
    for i in range(0,num):
        nums.append(i+1)

    return render_to_response('content-list.html', {'obj': u'搜索',
                                                    'lists': lists[(pagenum-1) * 10: min(pagenum * 10, len_num)],'pagenums':nums,
                                                    'url_name': 'search',
                                                    'content': content})
