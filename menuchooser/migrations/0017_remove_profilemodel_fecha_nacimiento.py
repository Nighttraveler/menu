# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-18 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuchooser', '0016_auto_20161215_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='fecha_nacimiento',
        ),
    ]
