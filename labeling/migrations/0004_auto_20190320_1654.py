# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-20 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0003_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('l', 'labeling'), ('c', 'checking')], max_length=20),
        ),
    ]
