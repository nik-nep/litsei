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

def library(request):
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    books = Book.objects.all()
    letters = FilterLetter.objects.all()
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books_paginator = paginator.get_page(page)

    rubrics = Rubric.objects.annotate(Count('article'))
    category = Category.objects.annotate(Count('book'))
    section_category = SectionCategory.objects.all()
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()

    context = {'rubrics': rubrics, 'books': books, 'category': category,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            'section_category': section_category,
            'books_paginator': books_paginator,
            'letters': letters,
            }
    return render(request, 'library/library.html', context)


def category_books(request, pk):
    books = Book.objects.filter(category=pk)
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books_paginator = paginator.get_page(page)
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    category = Category.objects.annotate(Count('book'))
    category_name = get_object_or_404(Category, pk=pk)
    section_category = SectionCategory.objects.filter(category=pk)
    tags = Tag.objects.all()
    letters = FilterLetter.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    context = {'rubrics': rubrics, 'books': books, 'category': category,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            'section_category': section_category,
            'category_name': category_name, 'letters': letters,
            'books_paginator': books_paginator,
            }
    return render(request, 'library/library_category.html', context)


def rubric_books(request, pk):
    books = Book.objects.filter(section_category=pk)
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books_paginator = paginator.get_page(page)
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    category = Category.objects.annotate(Count('book'))
    section_category = SectionCategory.objects.all()
    section_name = get_object_or_404(SectionCategory, pk=pk)
    tags = Tag.objects.all()
    letters = FilterLetter.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    context = {'rubrics': rubrics, 'books': books, 'category': category,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            'section_category': section_category,
            'section_name': section_name, 'letters': letters,
            'books_paginator': books_paginator,
            }
    return render(request, 'library/library_section.html', context)


def filter_books(request, pk):
    books = Book.objects.filter(filter_letter=pk)
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books_paginator = paginator.get_page(page)
    last_3_articles = Article.objects.filter(is_active=True)[0:3]
    last_2_articles = Article.objects.filter(is_active=True)[:2]
    rubrics = Rubric.objects.annotate(Count('article'))
    category = Category.objects.annotate(Count('book'))
    letters = FilterLetter.objects.all()
    letter_name = get_object_or_404(FilterLetter, pk=pk)
    #section_category = SectionCategory.objects.all()
    #section_name = get_object_or_404(SectionCategory, pk=pk)
    tags = Tag.objects.all()
    totall_art = Article.objects.filter(is_active=True).count()
    context = {'rubrics': rubrics, 'books': books, 'category': category,
            'totall_art': totall_art, 'tags': tags,
            'last_3_articles': last_3_articles,
            'last_2_articles': last_2_articles,
            'letters': letters,
            'books_paginator': books_paginator,
            'letter_name': letter_name,
            }
    return render(request, 'library/filter_book.html', context)
