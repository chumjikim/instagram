# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_myuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('f', 'Female'), ('m', 'Male')], default='m', max_length=1),
        ),
    ]
