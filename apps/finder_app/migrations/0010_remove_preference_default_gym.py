# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder_app', '0009_auto_20190627_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='default_gym',
        ),
    ]