# Generated by Django 3.0 on 2019-12-25 23:43

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191209_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='PravilaPryiomu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Назва')),
                ('text', models.TextField(blank=True, db_index=True, verbose_name='Опис')),
                ('format_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Опис розширено')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публікації')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Правила прийому',
                'verbose_name_plural': 'Правило прийому',
                'ordering': ['-published_date'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Стаття розширена'),
        ),
    ]