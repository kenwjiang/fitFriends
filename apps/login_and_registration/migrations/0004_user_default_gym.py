# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0003_auto_20190626_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_gym',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]