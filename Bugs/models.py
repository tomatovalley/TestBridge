# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import datetime

# Create your models here.
class Bug(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    test_id = models.ForeignKey('Tests.Test', default=0, verbose_name='Test')
    error_found = models.CharField(max_length=500, verbose_name='Error Found')
    steps= models.CharField(max_length=2000, verbose_name='Steps')
    screenshot = models.ImageField(upload_to= 'screenshots/', blank=True)
    creation_date = models.DateField(default=datetime.date.today,verbose_name='Creation Date')
    updated_date = models.DateField(default=datetime.date.today,verbose_name='Updated Date')
    enabled = models.BooleanField(default=True, verbose_name='Enabled')

    class Meta:
      db_table = 'bug'
      ordering = ["test_id"]
      verbose_name_plural = "Bugs"


