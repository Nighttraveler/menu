# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuchooser', '0011_auto_20161127_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomodel',
            name='Imagen',
            field=models.ImageField(blank=True, upload_to='/home/fernando/menu/tipos/'),
        ),
    ]
