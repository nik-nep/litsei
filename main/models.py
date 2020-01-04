from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery


# Create your models here.



class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True,
    verbose_name="Найменування рубрики")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name="Автор")
    title = models.CharField(max_length = 250, verbose_name='Назва новини, максимально - 250')

    text = models.TextField(blank=True, verbose_name='Текст новини')
    article_text = RichTextUploadingField(blank=True, verbose_name='Стаття розширена')
    tags = models.ManyToManyField('Tag', blank=True, related_name='articles')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення статті")
    is_image_default = models.BooleanField(default=False, verbose_name='Стандартне зображення')
    is_video_news = models.BooleanField(default=False, verbose_name='Відео новина')
    gallery = models.ForeignKey('photologue.Gallery', blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name='Галерея статті')
    add_image = models.ManyToManyField('ArticleToImage', blank=True, related_name='articles')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публікації')
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name="Рубрика")
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)
    def delete(self, *args, **kwargs):
        for ai in self.additionatolimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статті'
        verbose_name = 'Стаття'
        ordering = ["-published_date"]


class AdditionalImage(models.Model):
    art_photo = models.ForeignKey(Article, on_delete=models.CASCADE,
                           verbose_name='Новини')
    image = models.ImageField(upload_to=get_timestamp_path_article_photo,
                    verbose_name="Зображення")
    class Meta:
        verbose_name_plural = 'Додаткові зображення'
        verbose_name = 'Додаткове зображення'

class ArticleToImage(models.Model):
    image = models.ImageField(upload_to=get_timestamp_path_article_photo,
                    verbose_name="Загальне Зображення")
    class Meta:
        verbose_name_plural = 'Загальні додаткові зображення'
        verbose_name = 'Загальне додаткове зображення'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title



class Department(models.Model):
    name = models.CharField(max_length=50, db_index=True,
    verbose_name="Департамент")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Департаменти"
        verbose_name = "Департамент"
        ordering = ["name"]

class Educationlevel(models.Model):
    name = models.CharField(max_length=100, db_index=True,
    verbose_name="Освітньо-кваліфікаційний рівень")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Освітньо-кваліфікаційні рівні"
        verbose_name = "Освітньо-кваліфікаційний рівень"
        ordering = ["name"]

class Qualification(models.Model):
    name = models.CharField(max_length=100, db_index=True,
    verbose_name="Кваліфікаційна категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Кваліфікаційні категорії"
        verbose_name = "Кваліфікаційна категорія"
        ordering = ["name"]


class Staff(models.Model):
    last_name = models.CharField(max_length = 50, verbose_name='Прізвище')
    first_name = models.CharField(max_length = 50, verbose_name="Ім'я")
    patronymic = models.CharField(blank=True, max_length = 50,
        verbose_name='По батькові')
    position = models.CharField(blank=True, max_length = 100, verbose_name='Посада')
    position_abb = models.CharField(blank=True, max_length = 50, verbose_name='Посада скороченно')
    education = models.CharField(blank=True, max_length = 100, verbose_name='Освіта')
    specialty= models.CharField(blank=True, max_length = 50, verbose_name='Фах')
    level = models.ForeignKey('Educationlevel', null=True, blank=True,
        on_delete=models.PROTECT, verbose_name="Освітньо-кваліфікаційний рівень")
    qualification = models.ForeignKey('Qualification', null=True, blank=True,
        on_delete=models.PROTECT, verbose_name="Кваліфікаційна категорія")

    experience = models.PositiveIntegerField(blank=True, null=True, verbose_name='Стаж')
    department = models.ForeignKey('Department', null=True,
        on_delete=models.PROTECT, verbose_name="Департамент")

    content = models.TextField(blank=True, verbose_name='Резюме')
    methodical_dev = models.TextField(blank=True,
        verbose_name='Методичнi розробки')

    image = models.ImageField(blank=True, upload_to='staff',
                               verbose_name="Фото співробітника")

    adding_date = models.DateTimeField(auto_now_add=True, db_index=True,
    verbose_name='Дата додавання')
    sort_staff = models.PositiveIntegerField(blank=True, verbose_name='Сортування')

    def delete(self, *args, **kwargs):
        for mf in self.metodikfile_set.all():
            mf.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        ln = self.last_name
        fn = self.first_name
        pn = self.patronymic
        full_name = ln + " " + fn + " " + pn
        return full_name

    class Meta:
        verbose_name_plural = "Працівники"
        verbose_name = "Працівник"
        ordering = ["sort_staff"]

class Metodikfile(models.Model):
    title = models.CharField(max_length=50)
    mf = models.ForeignKey(Staff, on_delete=models.CASCADE,
                               verbose_name='Оберіть працівника')
    file = models.FileField(upload_to='materials',
                    verbose_name="Додаткові файли")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Додаткові файли'
        verbose_name = 'Додатковий файл'

class PravilaPryiomu(models.Model):
    title = models.CharField(max_length = 200, verbose_name='Назва')
    text = models.TextField(blank=True, verbose_name='Опис')
    format_text = RichTextUploadingField(blank=True, verbose_name='Опис розширено')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публікації')
    is_active = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Правила прийому'
        verbose_name = 'Правила прийому'
        ordering = ["-published_date"]
