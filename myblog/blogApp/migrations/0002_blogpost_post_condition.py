# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_condition',
            field=models.BooleanField(default=False),
        ),
    ]