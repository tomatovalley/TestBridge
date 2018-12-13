# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-10 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestBridgeApp', '0009_auto_20181205_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
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
        migrations.AlterModelOptions(
            name='tb_user',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name_plural': 'Users'},
        ),
    ]
