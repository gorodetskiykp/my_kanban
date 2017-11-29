# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_panel', '0002_auto_20171129_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasknote',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasknote',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
