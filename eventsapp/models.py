from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery

# Create your models here.

class EventsType(models.Model):
    title = models.CharField(max_length=255, db_index=True,
    verbose_name="Тип заходу")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Типи"
        verbose_name = "Тип"
        ordering = ["title"]


class Events(models.Model):
    s_number = models.PositiveIntegerField(blank=True, verbose_name='Порядковий номер (сортування)')
    name = models.CharField(blank=True, max_length=255, verbose_name="Назва заходу, макс 255")
    invited = RichTextUploadingField(blank=True, verbose_name='Запрошені, для кого')
    location = models.CharField(blank=True, max_length=255, verbose_name="Адреса проведення")
    description = RichTextUploadingField(blank=True, verbose_name='Опис заходу')
    event_date_start = models.DateTimeField(null=True, blank=True, verbose_name='Початок заходу')
    event_date_end = models.DateTimeField(null=True, blank=True, verbose_name='Закінчення заходу')
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')
    image = models.ImageField(blank=True, upload_to='events', verbose_name="Зображення")
    event_type = models.ForeignKey('EventsType', null=True, on_delete=models.PROTECT, verbose_name='Тип заходу')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Заходи"
        verbose_name = "Захід"
        ordering = ["s_number"]
