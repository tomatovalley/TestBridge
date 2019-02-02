# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 02:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Devices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Test Decription')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation Date')),
                ('updated_date', models.DateField(default=datetime.date.today, verbose_name='Updated Date')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('device_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Devices.Device', verbose_name='Device')),
                ('functionality_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Projects.Functionality', verbose_name='Functionality')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'test',
                'verbose_name_plural': 'Tests',
            },
        ),
    ]