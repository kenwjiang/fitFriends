# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0009_auto_20190627_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='def_gym',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_gym', to='login_and_registration.Gym'),
        ),
    ]
