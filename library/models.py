from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Категорія")
    description = models.TextField(blank=True, verbose_name='Опис категорії')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категорії"
        verbose_name = "Категорія"
        ordering = ["name"]

class SectionCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True,
                                verbose_name="Розділ")
    description = models.TextField(blank=True, verbose_name='Опис розділу')
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT,
                                   verbose_name='Категорія')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = "Розділи"
        verbose_name = "Розділ"
        ordering = ["name"]

class FilterLetter(models.Model):
    filter_letter = models.CharField(max_length=1, verbose_name="Фільтрування за літерою:")

    def __str__(self):
            return self.filter_letter

    class Meta:
        verbose_name_plural = "Літери"
        verbose_name = "Літера"
        ordering = ["filter_letter"]

class PublishingHouse(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Видавництво")
    description = models.TextField(blank=True, verbose_name='Опис видавництва')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = "Видавництва"
        verbose_name = "Видавництво"
        ordering = ["name"]

class Author(models.Model):
    last_name = models.CharField(max_length = 255, verbose_name='Прізвище')
    first_name = models.CharField(max_length = 255, verbose_name="Ім'я")
    patronymic = models.CharField(blank=True, max_length = 255,
                    verbose_name='По батькові')
    description = models.TextField(blank=True, verbose_name='Опис')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_book_author,
                    verbose_name='Зображення')

    def __str__(self):
        ln = self.last_name
        fn = self.first_name
        pn = self.patronymic
        full_name = ln + " " + fn + " " + pn
        return full_name

    class Meta:
        verbose_name_plural = "Автори"
        verbose_name = "Автор"
        ordering = ["last_name"]


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва підручника або книги")
    subject = models.CharField(max_length=255, blank=True, verbose_name="Предмет")
    description = models.TextField(blank=True, verbose_name='Опис')
    filter_letter = models.ForeignKey(FilterLetter, null=True, blank=True, on_delete=models.PROTECT,
                               verbose_name='Фільтрування за літерою:')
    file = models.FileField(blank=True, upload_to=get_timestamp_path_book,
                            verbose_name="Завантажити підручник або книгу")
    file_url = models.CharField(max_length=255, blank=True, verbose_name="Посилання на файл в інтернет")
    cover = models.ImageField(blank=True, upload_to=get_timestamp_path_cover,
                            verbose_name="Обкладинка")
    is_cover_default = models.BooleanField(default=False, verbose_name='Стандартна обкладинка')
    year = models.PositiveSmallIntegerField(blank=True, default=2020, verbose_name="Дата видання")
    book_author = models.ManyToManyField(Author, blank=True, related_name='author')
    publishing_house = models.ForeignKey(PublishingHouse, null=True, blank=True, on_delete=models.PROTECT,
                               verbose_name='Видавництво')
    section_category = models.ManyToManyField(SectionCategory, blank=True, related_name='section_category')
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT,
                               verbose_name='Категорія')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = "Підручники або книги"
        verbose_name = "Підручник або книга"
        ordering = ["name"]
