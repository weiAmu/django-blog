from django.contrib import admin
from .models import Article, Tui, Tag,  Category, Link, Banner, About

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time', )
    list_per_page = 50
    ordering = ('-created_time', )
    list_display_links = ('id', 'title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')
    list_display_links = ('id', 'text_info')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
    list_display_links = ('id', 'name')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_url', 'description')
    list_display_links = ('id', 'name', 'link_url')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'addr', 'mail', 'sign')
    list_display_links = ('id', 'alias')