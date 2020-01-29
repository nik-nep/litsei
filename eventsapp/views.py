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

def events(request):
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    events = Events.objects.filter(is_active=True)
    context = {'rubrics': rubrics, 'events': events,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            }
    return render(request, 'eventsapp/events.html', context)
