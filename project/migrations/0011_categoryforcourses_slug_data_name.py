# Generated by Django 5.1.6 on 2025-03-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryforcourses',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название сайта'),
        ),
    ]
