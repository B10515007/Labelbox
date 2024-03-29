# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-20 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0009_auto_20190320_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labeling',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('L', 'LABELING'), ('C', 'CHECKING'), ('R', 'RELABELING'), ('F', 'FINISH')], max_length=20),
        ),
    ]
