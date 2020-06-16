from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from mdeditor.fields import MDTextField

import markdown
import re

class Category(models.Model):
    name = models.CharField('文章分类', max_length=20)
    index = models.IntegerField(default=99, verbose_name='文章排序', unique=True)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tui(models.Model):
    name = models.CharField('推荐位', max_length=20)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    #文章默认缩略图
    IMG_LINK = '/static/image/inroad.jpg'

    title = models.CharField('文章标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=230, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类', blank=True, null=True)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='文章标签', blank=True)
    img = models.ImageField(upload_to="article_img/%Y/%m/%d/", default=IMG_LINK, verbose_name='文章图片', blank=True, null=True)
    body = MDTextField()

    '''
    body = UEditorField('文章内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', blank=False, null=False)
    views = models.PositiveIntegerField('阅读量', default=0)
    loves = models.PositiveIntegerField('点赞量', default=0)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100, default='#')
    is_active = models.BooleanField("是否展示", default=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info

class Link(models.Model):
    name = models.CharField('网站名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)
    description = models.CharField('网站描述', max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to="link_logo/%Y/%m/%d/", verbose_name='网站logo', blank=True, null=True)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class About(models.Model):
    alias = models.CharField('艺名', max_length=20, blank=False, null=False)
    addr = models.CharField('地址', max_length=50, blank=True, null=True)
    mail = models.EmailField('邮箱', max_length=50)
    qqnum = models.CharField('QQ号', max_length=11, blank=False, null=False)
    sign = models.CharField('个性签名', max_length=20, blank=True, null=True)
    body = UEditorField('文章内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )

    class Meta:
        verbose_name = '站长信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.alias

'''
class Comments(models.Model):
    article = models.ForeignKey()
'''