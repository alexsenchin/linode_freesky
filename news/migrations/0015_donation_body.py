# Generated by Django 4.0.4 on 2022-06-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_donation_image_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='body',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
