# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-26 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='default_gym',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
