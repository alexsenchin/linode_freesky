# Generated by Django 4.0.4 on 2022-06-04 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_category_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
