from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=250, verbose_name="Оголошення")
    description = models.TextField(blank=True, verbose_name='Опис оголошення')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_announcement,
                            verbose_name="Фото")
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')
    sorting = models.PositiveIntegerField(blank=True, verbose_name='Сортування')


    def __str__(self):
            return self.title

    class Meta:
        verbose_name_plural = "Оголошення"
        verbose_name = "Оголошення"
        ordering = ["sorting"]
