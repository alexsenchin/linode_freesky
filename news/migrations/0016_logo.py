# Generated by Django 4.0.4 on 2022-07-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_donation_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
