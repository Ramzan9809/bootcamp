# Generated by Django 5.1.6 on 2025-03-11 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_courses_instructors_remove_instructors_social_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinks',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='project.instructors'),
        ),
    ]
