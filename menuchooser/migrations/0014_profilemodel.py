# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 02:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import menuchooser.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menuchooser', '0013_auto_20161201_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, upload_to=menuchooser.models.get_user_image_folder)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]