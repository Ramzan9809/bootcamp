# Generated by Django 5.1.6 on 2025-03-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_comments_email_replycomments_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='map',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на карту'),
        ),
    ]
