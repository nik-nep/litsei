# Generated by Django 3.0 on 2020-01-29 20:32

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Тип заходу')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типи',
                'ordering': ['title'],
            },
        ),
        migrations.RenameField(
            model_name='events',
            old_name='event_date',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='title',
        ),
        migrations.AddField(
            model_name='events',
            name='event_date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Закінчення заходу'),
        ),
        migrations.AddField(
            model_name='events',
            name='event_date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Початок заходу'),
        ),
        migrations.AddField(
            model_name='events',
            name='invited',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Запрошені, для кого'),
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адреса проведення'),
        ),
        migrations.AddField(
            model_name='events',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва заходу, макс 255'),
        ),
        migrations.AddField(
            model_name='events',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='eventsapp.EventsType', verbose_name='Тип заходу'),
        ),
    ]