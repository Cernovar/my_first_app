# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20171118_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]