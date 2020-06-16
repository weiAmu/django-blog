from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('article/', views.article, name = 'article'),
    path('read/', views.read, name='detail'),
    path('article/<cid>/', views.list, name = 'list'),
    path('read/<rid>/', views.read, name ='read'),
    path('index/', views.blog_index, name='blog_index'),
]