from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery

# Create your models here.

class PartnersLogo(models.Model):
    title = models.CharField(max_length=250, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name='Опис')
    logo = models.ImageField(blank=True, upload_to=get_timestamp_path_logo_partners,
                            verbose_name="Логотип")
    website = models.URLField(max_length=250)
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')
    sorting = models.PositiveIntegerField(blank=True, verbose_name='Сортування')


    def __str__(self):
            return self.title

    class Meta:
        verbose_name_plural = "Корисні посилання - Партнери"
        verbose_name = "Партнер"
        ordering = ["sorting"]
