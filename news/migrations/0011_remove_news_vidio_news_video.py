# Generated by Django 4.0.4 on 2022-06-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_news_vidio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='vidio',
        ),
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]