# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0002_auto_20171112_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='answers',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='replies',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='stdintxn',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'managed': False},
        ),
    ]
