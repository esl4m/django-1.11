# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bird2', '0002_users_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
