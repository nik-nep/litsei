from django.db import models

from main.utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery
from main.models import *

# Create your models here.


# content


class Content(models.Model):
    title = models.TextField(blank=True, verbose_name='Пункт Меню')
    slug_title = models.SlugField(max_length=150, verbose_name='Коротка назва')
    content_text = RichTextUploadingField(blank=True, verbose_name='Наповнення Сторінки')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення")
    video = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Відео до статті не більше 10 Мб")
    file_1 = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Додати файл 1")
    title_file_1 = models.TextField(blank=True, verbose_name='Назва файлу 1')
    file_2 = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Додати файл 2")
    title_file_2 = models.TextField(blank=True, verbose_name='Назва файлу 2')
    file_3 = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Додати файл 3")
    title_file_3 = models.TextField(blank=True, verbose_name='Назва файлу 3')
    file_4 = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Додати файл 4")
    title_file_4 = models.TextField(blank=True, verbose_name='Назва файлу 4')
    file_5 = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name="Додати файл 5")
    title_file_5 = models.TextField(blank=True, verbose_name='Назва файлу 5')
    gallery = models.ForeignKey('photologue.Gallery', blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name='Галерея статті')
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статті'
        verbose_name = 'Стаття'
