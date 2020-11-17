from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from .models import *
from main.models import *
from photologue.models import Photo, Gallery
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.



def sitecontent(request, pk):
    content = get_object_or_404(Content, pk=pk)
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    tags = Tag.objects.all()
    totall_art = Article.objects.filter().count()
    navmenus = Navmenu.objects.all()
    try:
        queryset = Gallery.objects.on_site().is_public().filter(pk=content.gallery.pk)
    except:
        queryset = []
    context = {'rubrics': rubrics,
        'totall_art': totall_art, 'tags': tags,
        'last_3_articles': last_3_articles,
        'last_2_articles': last_2_articles, 'content': content,
        'navmenus': navmenus, 'queryset': queryset,
        }
    return render(request, 'sitecontent/content.html', context)
