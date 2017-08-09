# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20170808_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('P', 'Personal'), ('T', 'Topic')], default='T', max_length=1),
        ),
    ]
