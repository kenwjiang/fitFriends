# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0010_auto_20190627_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='gym_id',
            new_name='place_id',
        ),
    ]
