# Generated by Django 3.0 on 2020-02-07 11:47

from django.db import migrations, models
import main.utilites


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200207_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, upload_to=main.utilites.get_timestamp_path_article_video, verbose_name='Відео до статті не більше 10 Мб'),
        ),
    ]