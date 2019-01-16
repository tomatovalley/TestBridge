# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Devices.models import Device
import datetime

# Create your models here.
class Test(models.Model):
  name = models.CharField(max_length=50, verbose_name='Test Decription')
  functionality_id = models.IntegerField(verbose_name='Functionality ID') 
  device_id = models.ForeignKey('Devices.Device', default=0)
  creation_date = models.DateField(default=datetime.date.today,verbose_name='Creation Date')
  updated_date = models.DateField(default=datetime.date.today,verbose_name='Updated Date')
  enabled = models.BooleanField(default=True, verbose_name='Enabled')

  class Meta:
    db_table = 'test'
    ordering = ["id"]
    verbose_name_plural = "Tests"

  def __unicode__(self):
    return self.name