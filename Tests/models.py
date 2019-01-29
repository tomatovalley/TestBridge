# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from Devices.models import Device
from Projects.models import Functionality
import datetime

# Create your models here.
class Test(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
  name = models.CharField(max_length=50, verbose_name='Test Decription')
  functionality_id = models.ForeignKey('Projects.Functionality', default=0,verbose_name='Functionality')
  device_id = models.ForeignKey('Devices.Device', default=0, verbose_name='Device')
  creation_date = models.DateField(default=datetime.date.today,verbose_name='Creation Date')
  updated_date = models.DateField(default=datetime.date.today,verbose_name='Updated Date')
  enabled = models.BooleanField(default=True, verbose_name='Enabled')

  class Meta:
    db_table = 'test'
    ordering = ["id"]
    verbose_name_plural = "Tests"

  def __unicode__(self):
    return self.name