from django.shortcuts import render, reverse, redirect
from .models import Category, Article, Tag, About, Link
import markdown

def index(request):
    hots = Article.objects.order_by('-views')[0:3]
    message = About.objects.get()
    context = {
        'hots': hots,
        'message': message,
    }
    return render(request, 'index.html', context)


def article(request):
    allcategory = Category.objects.all()
    allarticle = Article.objects.all().order_by('-created_time')
    title = "所有文章"
    hotarticle = Article.objects.order_by('-views')[0:8]
    tuiarticle = Article.objects.filter(tui__id=1)[0:6]

    context = {
        'allcategory': allcategory,
        'allarticle': allarticle,
        'hotarticle': hotarticle,
        'tuiarticle': tuiarticle,
        'title': title,
    }
    return render(request, 'article.html', context)

def list(request,cid):
    allcategory = Category.objects.all()
    allarticle = Article.objects.filter(category_id=cid).order_by('-created_time')
    title = Category.objects.get(id=cid).name
    hotarticle = Article.objects.order_by('-views')[0:8]
    tuiarticle = Article.objects.filter(tui__id=1)[0:6]

    context = {
        'allcategory': allcategory,
        'allarticle': allarticle,
        'hotarticle': hotarticle,
        'tuiarticle': tuiarticle,
        'title': title,
    }
    return render(request, 'article.html', context)

def read(request, rid):
    article = Article.objects.get(id=rid)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    print(article.body)
    context = {
        'article': article,
    }
    return render(request, 'read.html', context)

def link(request):
    message = About.objects.get()
    links = Link.objects.all()

    context = {
        'message': message,
        'links': links,
    }

    return render(request, 'link.html', context)

def about(request):
    message = About.objects.get()
    context = {
        'message': message,
    }
    return render(request, 'about.html', context)

def archive(request):
    articles = Article.objects.order_by('-created_time')
    context = {
        'articles': articles,
    }
    return render(request,'archive.html', context)

def exploit(request):
    context = {

    }
    return render(request, 'exploit.html', context)

def blog_index(request):
    return redirect(reverse('index'))

def test(request):
    article = Article.objects.get(id=6)

    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    context = {
        'article': article
    }

    return render(request, 'test.html', context)