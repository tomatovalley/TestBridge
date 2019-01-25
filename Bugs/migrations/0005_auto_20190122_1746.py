# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-23 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bugs', '0004_auto_20190115_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='screenshot',
            field=models.ImageField(blank=True, upload_to='screenshots/'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='test_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Tests.Test', verbose_name='Test'),
        ),
    ]
