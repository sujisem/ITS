# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0006_auto_20171122_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.CharField(db_column='Id', max_length=50, primary_key=True, serialize=False),
        ),
    ]
