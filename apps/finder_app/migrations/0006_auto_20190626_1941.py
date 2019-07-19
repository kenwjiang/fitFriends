# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder_app', '0005_auto_20190626_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='cardio',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='endurance',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='flexibility',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='genFit',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='muscle',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='strength',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='weightLoss',
        ),
        migrations.AddField(
            model_name='preference',
            name='categories',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='friHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='monHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='satHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sunHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='thuHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='tuesHour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='wedHour',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
