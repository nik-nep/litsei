# Generated by Django 3.0 on 2020-01-29 19:20

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_number', models.PositiveIntegerField(blank=True, verbose_name='Порядковий номер (сортування)')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Назва заходу')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Опис заходу')),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True, verbose_name='Опубліковано')),
                ('image', models.ImageField(blank=True, upload_to='events', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Захід',
                'verbose_name_plural': 'Заходи',
                'ordering': ['s_number'],
            },
        ),
    ]