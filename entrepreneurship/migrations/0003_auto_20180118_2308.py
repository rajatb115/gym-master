# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurship', '0002_auto_20180118_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='featured_image',
        ),
    ]
