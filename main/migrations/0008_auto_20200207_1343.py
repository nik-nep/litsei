# Generated by Django 3.0 on 2020-02-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_resourcescenter_trainingcenter'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_video_article',
            field=models.BooleanField(default=False, verbose_name='Додати відео до статті'),
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, upload_to='video', verbose_name='Відео до статті не більше 10 Мб'),
        ),
    ]