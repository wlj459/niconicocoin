# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class College(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    content = models.TextField(u'正文')
    url_name = models.CharField(u'url', editable=False, default='college', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'学院概况'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title

class Faculty(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='faculty', max_length=500)


    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'师资队伍'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class Recruit(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='recruit', max_length=500)


    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'招生动态'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class News(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='news', max_length=500)


    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'新闻动态'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class Notice(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='notice', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'通知公告'
        verbose_name = u'通知'

    def __unicode__(self):
        return u'%s' %self.title


class CourseWare(models.Model):
    title = models.CharField(u'课件名称', max_length=500)
    time = models.DateField(u'发布时间', auto_now_add=True)
    course = models.FileField(u'课件',upload_to='media')
    show = models.BooleanField(u'是否发布', default=False)
    author=models.ForeignKey(User,editable=False)
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='courseware', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'课件'
        verbose_name = u'课件'

    def __unicode__(self):
        return u'%s' %self.title


class International(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='communication', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'国际交流'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class Rule(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='rule', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'规章制度'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class Employment(models.Model):
    title = models.CharField(u'标题', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    content = models.TextField(u'正文')
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='employment', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'就业信息'
        verbose_name = u'文章'

    def __unicode__(self):
        return u'%s' %self.title


class Link(models.Model):
    title = models.CharField(u'标题', max_length=500)
    image = models.CharField(u'logo图片链接', max_length=500)
    url = models.CharField(u'链接', max_length=500)
    show = models.BooleanField(u'是否发布', default=False)
    time = models.DateField(u'发布时间', auto_now_add=True)
    click = models.IntegerField(u'点击次数', editable=False,default=0)
    url_name = models.CharField(u'url', editable=False, default='link', max_length=500)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = u'友情链接'
        verbose_name = u'链接'

    def __unicode__(self):
        return u'%s' %self.title