# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-20 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0006_auto_20190320_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='labeling',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='labeling',
            name='judge',
            field=models.BooleanField(default=False),
        ),
    ]