# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-16 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.Device'),
        ),
    ]