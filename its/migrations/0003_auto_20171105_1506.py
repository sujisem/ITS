# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0002_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'managed': False},
        ),
    ]