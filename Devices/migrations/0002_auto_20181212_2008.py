# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-13 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(choices=[('Windows', 'Windows'), ('Linux', 'Linux'), ('Mac OS', 'Mac OS'), ('Android', 'Android'), ('IOS', 'IOS')], max_length=50),
        ),
    ]
