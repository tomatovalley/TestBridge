# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Functionalities', '0003_functionality_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='functionality',
            old_name='device',
            new_name='title',
        ),
    ]
