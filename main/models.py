from django.db import models

from .utilites import *
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from photologue.models import Gallery
from sitecontent.models import *


# Create your models here.



class Rubric(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Найменування рубрики")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name='Автор')
    title = models.TextField(blank=True, verbose_name='Назва новини')

    text = models.TextField(blank=True, verbose_name='Текст новини')
    article_text = RichTextUploadingField(blank=True, verbose_name='Стаття розширена')
    tags = models.ManyToManyField('Tag', blank=True, related_name='articles')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення статті")
    video = models.FileField(blank=True, upload_to=get_timestamp_path_article_video, verbose_name="Відео до статті не більше 10 Мб")
    is_image_default = models.BooleanField(default=False, verbose_name='Стандартне зображення')
    is_video_article = models.BooleanField(default=False, verbose_name='Додати відео до статті')
    is_video_news = models.BooleanField(default=False, verbose_name='Відео новина')
    gallery = models.ForeignKey('photologue.Gallery', blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name='Галерея статті')
    add_image = models.ManyToManyField('ArticleToImage', blank=True, related_name='articles')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публікації')
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)
    
    
#    def delete(self, *args, **kwargs):
#        for ai in self.additionatolimage_set.all():
#            ai.delete()
#        super().delete(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новини'
        verbose_name = 'Новина'
        ordering = ["-published_date"]


class AdditionalImage(models.Model):
    title = models.CharField(blank=True, max_length=250)
    art_photo = models.ForeignKey(Article, on_delete=models.CASCADE,
                           verbose_name='Новини')
    image = models.ImageField(upload_to=get_timestamp_path_article_photo,
                    verbose_name='Зображення')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Додаткові зображення'
        verbose_name = 'Додаткове зображення'

class ArticleToImage(models.Model):
    title = models.CharField(blank=True, max_length=250)
    image = models.ImageField(upload_to=get_timestamp_path_article_photo,
                    verbose_name='Загальне Зображення')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Загальні додаткові зображення'
        verbose_name = 'Загальне додаткове зображення'



class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title



class Department(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Департамент")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Департаменти"
        verbose_name = "Департамент"
        ordering = ["name"]

class Educationlevel(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Освітньо-кваліфікаційний рівень")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Освітньо-кваліфікаційні рівні"
        verbose_name = "Освітньо-кваліфікаційний рівень"
        ordering = ["name"]

class Qualification(models.Model):
    name = models.CharField(max_length=255, db_index=True,
    verbose_name="Кваліфікаційна категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Кваліфікаційні категорії"
        verbose_name = "Кваліфікаційна категорія"
        ordering = ["name"]


class Staff(models.Model):
    last_name = models.CharField(max_length = 255, verbose_name='Прізвище')
    first_name = models.CharField(max_length = 255, verbose_name="Ім'я")
    patronymic = models.CharField(blank=True, max_length = 255,
        verbose_name='По батькові')
    position = models.CharField(blank=True, max_length = 255, verbose_name='Посада')
    position_abb = models.CharField(blank=True, max_length = 255, verbose_name='Посада скороченно')
    education = models.CharField(blank=True, max_length = 255, verbose_name='Освіта')
    specialty= models.CharField(blank=True, max_length = 255, verbose_name='Фах')
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
    title = models.CharField(max_length=255)
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
    title = models.CharField(max_length = 255, verbose_name='Назва')
    text = models.TextField(blank=True, verbose_name='Опис')
    format_text = RichTextUploadingField(blank=True, verbose_name='Опис розширено')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                                  verbose_name="Зображення Правил")
    file = models.FileField(blank=True, upload_to='materials', verbose_name="Файл Правил")
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

class ZvitDirector(models.Model):
    zvit_title = models.TextField(blank=True, verbose_name='Назва Звіту')
    zvit_text = RichTextUploadingField(blank=True, verbose_name='Текст Звіту')
    zvit_image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення Звіту")
    zvit_active = models.BooleanField(default=True, verbose_name='Опубліковано')

    def delete(self, *args, **kwargs):
        for up_file in self.uploadfile_set.all():
            up_file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.zvit_title

    class Meta:
        verbose_name_plural = 'Звіти Директора'
        verbose_name = 'Звіт Директора'


class UploadFile(models.Model):
    title = models.CharField(max_length=255)
    up_file = models.ForeignKey(ZvitDirector, on_delete=models.CASCADE,
                                   verbose_name='Оберіть Звіт')
    file = models.FileField(upload_to='materials',
                        verbose_name="Файл Звіту")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Файли Звіту'
        verbose_name = 'Файл Звіту'

class PeriodPlans(models.Model):
    name = models.CharField(max_length=100, db_index=True,
    verbose_name="План роботи за:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Період планів"
        verbose_name = "Період Плану"
        ordering = ["-name"]

class PlanRoboty(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='План роботи')
    text = models.TextField(blank=True, verbose_name='Текст')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення")
    is_image_default = models.BooleanField(default=False, verbose_name='Стандартне зображення')
    file = models.FileField(upload_to='plans', verbose_name="Плани роботи")
    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публікації')
    period = models.ForeignKey('PeriodPlans', null=True,
                               on_delete=models.CASCADE, verbose_name='Період планів')
    is_active = models.BooleanField(default=False, verbose_name='Активний план')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Плани роботи'
        verbose_name = 'План роботи'
        ordering = ["-published_date"]


class Professions(models.Model):
    TYPEPROF = (
                (None, 'Виберіть тип професії'),
                ('b', 'первинна професійна підготовка'),
                ('c', 'професійно-технічне навчання (курсова підготовка)'),
    )
    position_nimber = models.PositiveIntegerField(blank=True, verbose_name='Позиція в таблиці')
    type_prof = models.CharField(max_length=1, choices=TYPEPROF)
    table_number = models.PositiveIntegerField(blank=True, verbose_name='Номер таблиці')
    code_prof = models.CharField(blank=True, max_length=25, verbose_name='Код професії')
    name_prof = models.CharField(blank=True, max_length=255, verbose_name='Назва професії')
    license_amount = models.PositiveIntegerField(blank=True, verbose_name='Ліцензований обсяг')
    term_of_study_9 = models.CharField(blank=True, max_length=50, verbose_name='Термін навчання на базі 9 класів')
    term_of_study_11 = models.CharField(blank=True, max_length=50, verbose_name='Термін навчання на базі 11 класів')

    def __str__(self):
        return self.name_prof

    class Meta:
        verbose_name_plural = 'Професія'
        verbose_name = 'Професії'
        ordering = ["position_nimber"]


class TrainingCenter(models.Model):
    title = models.CharField(max_length=255, db_index=True,
    verbose_name="Найменування НЦ")
    tc_text = RichTextUploadingField(blank=True, verbose_name='Опис НЦ')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення НЦ")
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    tc_sort = models.PositiveIntegerField(blank=True, verbose_name='Сортування')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Навчальні центри"
        verbose_name = "Навчальний центр"
        ordering = ["tc_sort"]

class ResourcesCenter(models.Model):
    title = models.TextField(blank=True, verbose_name='Назва ресурсу')
    text = RichTextUploadingField(blank=True, verbose_name='Опис ресурсу')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path_article,
                              verbose_name="Зображення ресурсу")
    is_image_default = models.BooleanField(default=False, verbose_name='Стандартне зображення')
    gallery = models.ForeignKey('photologue.Gallery', blank=True, null=True,
                              on_delete=models.PROTECT, verbose_name='Галерея статті')
    created_date = models.DateTimeField(default=timezone.now)
    training_center = models.ForeignKey('TrainingCenter', null=True,
                               on_delete=models.PROTECT, verbose_name='Навчальний центр')
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ресурси'
        verbose_name = 'Ресурс'
        ordering = ["-created_date"]


class Navchild(models.Model):
    title = models.CharField(blank=True, max_length=250, verbose_name="Найменування пункту меню")
    position_number = models.PositiveIntegerField(blank=True, verbose_name='Позиція у меню')
    file = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name='Файл до меню')
    navchild_url = models.CharField(max_length=255, blank=True, verbose_name="Посилання для меню")
    is_url_active = models.BooleanField(default=False, verbose_name='Активне посилання')
    is_file_active = models.BooleanField(default=False, verbose_name='Активне посилання на файл')
    child_content = models.OneToOneField('sitecontent.Content', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Наповнення рубріки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Пункти дочірнього меню'
        verbose_name = 'Пункт дочірнього меню'
        ordering = ["title"]

class Navmenu(models.Model):
    title = models.TextField(blank=True, verbose_name='Назва меню')
    menu_content = models.OneToOneField('sitecontent.Content', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Наповнення')
    navmenu_url = models.CharField(max_length=255, blank=True, verbose_name="Посилання для меню")
    is_url_active = models.BooleanField(default=False, verbose_name='Активне посилання')
    file_menu = models.FileField(blank=True, upload_to=get_timestamp_path_navmenu, verbose_name='Файл до меню')
    is_file_active = models.BooleanField(default=False, verbose_name='Активне посилання на файл')
    navchild = models.ManyToManyField('Navchild', blank=True, related_name='navmenu')
    is_active = models.BooleanField(default=True, verbose_name='Опубліковано')
    position_number = models.PositiveIntegerField(blank=True, verbose_name='Позиція меню')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Загальне Меню'
        verbose_name = 'Загальне Меню'
        ordering = ["position_number"]


# class GroupLitsei(models.Model):
#     title_group = models.CharField(blank=True, max_length=255, verbose_name='Групи')
#     plan = models.ManyToManyField('Plans', blank=True, related_name='plans')
#
#     def __str__(self):
#         return self.title_group
#
#     class Meta:
#         verbose_name_plural = 'Назви груп'
#         verbose_name = 'Назва групи'
#
# class Plans(models.Model):
#     position_nimber = models.PositiveIntegerField(blank=True, verbose_name='Позиція в таблиці')
#     title = models.CharField(max_length=255)
#     period = models.CharField(max_length=255)
#
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name_plural = "Плани навчання"
#         verbose_name = "План навчання"
#         ordering = ["position_nimber"]

# class Student(models.Model):
#     last_name = models.CharField(max_length = 255, verbose_name='Прізвище')
#     first_name = models.CharField(max_length = 255, verbose_name="Ім'я")
#     patronymic = models.CharField(blank=True, max_length = 255,
#         verbose_name='По батькові')
#     group = models.ForeignKey('GroupLitsei', on_delete=models.PROTECT,
#                                verbose_name='Оберіть групу')
#     birthday = models.DateField(blank=True, null=True, verbose_name='Дата народження')
#     start_studying = models.DateField(blank=True, null=True, verbose_name='Дата зарахування')
#     end_studying = models.DateField(blank=True, null=True, verbose_name='Дата випуску')
#     email = models.EmailField(blank=True, max_length = 255, verbose_name='Електронна адреса')
#     phone = models.CharField(max_length=20)
#
#     image = models.ImageField(blank=True, upload_to='students',
#                                verbose_name="Фото")
#
#
#     def __str__(self):
#         ln = self.last_name
#         fn = self.first_name
#         pn = self.patronymic
#         full_name = ln + " " + fn + " " + pn
#         return full_name
#
#     class Meta:
#         verbose_name_plural = "Студенти"
#         verbose_name = "Студент"
