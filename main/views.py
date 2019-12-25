from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import *


def home(request):
    articles = Article.objects.reverse()[:3]
    last_2_articles = Article.objects.reverse()[:2]
    context = {'articles': articles, 'last_2_articles': last_2_articles,
              }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')

def leadership(request):
    stafs = Staff.objects.all()
    return render(request, 'main/leadership.html', context={'stafs': stafs})


def newss_list(request):
    articles = Article.objects.all()
    last_2_articles = Article.objects.reverse()[:2]
    context = {'articles': articles, 'last_2_articles': last_2_articles}
    return render(request, 'main/news_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    last_3_articles = Article.objects.reverse()[0:3]
    last_2_articles = Article.objects.reverse()[:2]
    rubrics =  Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter().count()
    context = {'article': article, 'rubrics': rubrics,
              'totall_art': totall_art, 'tags': tags,
              'last_3_articles': last_3_articles,
              'last_2_articles': last_2_articles,
              }
    return render(request, 'main/article_detail.html', context)
