# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import menuchooser.models


class Migration(migrations.Migration):

    dependencies = [
        ('menuchooser', '0014_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=menuchooser.models.get_user_folder),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='bio',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
