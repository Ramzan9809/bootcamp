# Generated by Django 5.1.6 on 2025-03-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_blog_cound_reviews_blog_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='address',
            field=models.CharField(blank=True, help_text='Пр. Ленина, 30', max_length=100, null=True, verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='data',
            name='email2',
            field=models.EmailField(blank=True, help_text='courses_kg@gmail.com', max_length=100, null=True, verbose_name='Email 2'),
        ),
        migrations.AddField(
            model_name='data',
            name='phone2',
            field=models.CharField(blank=True, help_text='+996 554977013', max_length=20, null=True, verbose_name='Номер телефона 2'),
        ),
        migrations.AlterField(
            model_name='data',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Логотип'),
        ),
    ]
