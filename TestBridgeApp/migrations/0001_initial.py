# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-06 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(unique=True, verbose_name='Page Content')),
            ],
            options={
                'db_table': 'page',
            },
        ),
    ]
