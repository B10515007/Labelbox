# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-20 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0005_auto_20190320_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['state']},
        ),
    ]
