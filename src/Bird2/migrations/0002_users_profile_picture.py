# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bird2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
