# Generated by Django 4.0.4 on 2022-07-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_maincarousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
    ]
