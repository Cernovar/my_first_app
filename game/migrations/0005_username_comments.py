# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_username_hard_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='comments',
            field=models.TextField(default=None, max_length=1000, null=True),
        ),
    ]
