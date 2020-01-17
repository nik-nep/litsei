from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from .models import *

from photologue.models import Photo, Gallery

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# from photologue.models import *


def draft(request):
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    context = {'rubrics': rubrics,
        'totall_art': totall_art, 'tags': tags,
        'last_3_articles': last_3_articles,
        'last_2_articles': last_2_articles,
        }
    return render(request, 'main/draft_page.html', context)

def home(request):
    articles = Article.objects.filter(is_active=True)[:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    context = {'articles': articles, 'last_2_articles': last_2_articles,
                'rubrics': rubrics,
              }
    return render(request, 'main/index.html', context)

#
# def gallery(request):
#     photo = Photo.objects.all()
#     context = {'photo ': photo}
#     return render(request, 'base.html', context)

def about(request):
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    tags = Tag.objects.all()
    totall_art = Article.objects.filter().count()
    context = {'rubrics': rubrics,
        'totall_art': totall_art, 'tags': tags,
        'last_3_articles': last_3_articles,
        'last_2_articles': last_2_articles,
        }
    return render(request, 'main/about.html', context)

def leadership(request):
    stafs = Staff.objects.all()
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    context = {'stafs': stafs, 'last_2_articles': last_2_articles,
                'rubrics': rubrics,
                }
    return render(request, 'main/leadership.html', context)

def public(request):
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    context = {'last_2_articles': last_2_articles,
                'rubrics': rubrics,
                }
    return render(request, 'main/public.html', context)


def newss_list(request):
    articles = Article.objects.filter(is_active=True)
    last_2_articles = Article.objects.filter(is_active=True)[:2]

    paginator = Paginator(articles, 4)
    rubrics = Rubric.objects.annotate(Count('article'))
    page = request.GET.get('page')
    articles_paginator = paginator.get_page(page)
    context = {'articles': articles, 'last_2_articles': last_2_articles,
              'articles_paginator': articles_paginator,
              'rubrics': rubrics,
              }
    return render(request, 'main/news_list.html', context)

def rubric_newss_list(request, pk):
    articles = Article.objects.filter(rubric=pk, is_active=True)
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    paginator = Paginator(articles, 4)
    rubric = get_object_or_404(Rubric, pk=pk)
    page = request.GET.get('page')
    articles_paginator = paginator.get_page(page)
    context = {'articles': articles, 'last_2_articles': last_2_articles,
              'articles_paginator': articles_paginator,
              'rubric': rubric, 'rubrics': rubrics,
              }
    return render(request, 'main/rubric_news_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articles = Article.objects.filter(is_active=True)
    article_to_image = ArticleToImage.objects.all()
    try:
        queryset = Gallery.objects.on_site().is_public().filter(pk=article.gallery.pk)
    except:
        queryset = []


    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    #rubrics = Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    rubrics = Rubric.objects.annotate(Count('article'))
    context = {'article': article, 'rubrics': rubrics,
              'totall_art': totall_art, 'tags': tags,
              'last_3_articles': last_3_articles,
              'last_2_articles': last_2_articles,
              'articles': articles, 'article_to_image': article_to_image,
              'queryset': queryset,
              }
    return render(request, 'main/article_detail.html', context)

def pravyla_pryiomu(request):
    pravyla = PravilaPryiomu.objects.reverse()[0:1]
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter().count()
    context = {'pravyla': pravyla, 'rubrics': rubrics,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            }
    return render(request, 'main/pravyla_pryiomu.html', context)

def contact(request):
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    context = {'last_2_articles': last_2_articles,
                'rubrics': rubrics,
                }
    return render(request, 'main/contact.html', context)

def zvit_director(request):
    zvit = ZvitDirector.objects.filter(zvit_active=True)
    zvit_file = UploadFile.objects.all()
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    rubrics = Rubric.objects.annotate(Count('article'))
    context = {'rubrics': rubrics,
              'totall_art': totall_art, 'tags': tags,
              'last_3_articles': last_3_articles,
              'last_2_articles': last_2_articles,
              'zvit': zvit, 'zvit_file': zvit_file
              }
    return render(request, 'main/zvit.html', context)

def plans(request):
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    old_plans = PeriodPlans.objects.all()
    plan_active = PlanRoboty.objects.filter(is_active=True)
    rubrics = Rubric.objects.annotate(Count('article'))
    tags = Tag.objects.all()
    totall_art = Article.objects.filter().count()
    context = {'rubrics': rubrics, 'old_plans': old_plans,
        'totall_art': totall_art, 'tags': tags,
        'last_3_articles': last_3_articles,
        'last_2_articles': last_2_articles,
        'plan_active': plan_active,
        }
    return render(request, 'main/plans.html', context)

def old_plans_list(request, pk):
    plans = PlanRoboty.objects.filter(period=pk, is_active=False)
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    old_plans = PeriodPlans.objects.all()
    period = get_object_or_404(PeriodPlans, pk=pk)
    context = {'plans': plans, 'last_2_articles': last_2_articles,
              'period': period, 'rubrics': rubrics,
              'old_plans': old_plans,
              }
    return render(request, 'main/old_plans_list.html', context)

def profession(request):
    prof = Professions.objects.all()
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    context = {'rubrics': rubrics, 'prof': prof,
        'totall_art': totall_art, 'tags': tags,
        'last_3_articles': last_3_articles,
        'last_2_articles': last_2_articles,
        }
    return render(request, 'main/profession.html', context)
