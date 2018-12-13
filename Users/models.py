# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

USER_TYPE_CHOICES = (
     ('TESTER','Tester'),
     ('CLIENT','Client'),
 )

class Tb_user(models.Model):
  username = models.CharField(max_length=100,unique=True, verbose_name='Username')
  user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES, verbose_name='User Type')
  company = models.CharField(max_length=100, null=True, blank=True, verbose_name='Company')
  phone_number = models.CharField(max_length=10, verbose_name='Phone Number')
  address = models.CharField(max_length=200, verbose_name='Address')
  city = models.CharField(max_length=30, verbose_name='City')
  state = models.CharField(max_length=30, verbose_name='State')
  country = models.CharField(max_length=30,verbose_name='Country')
  creation_date = models.DateField(default=datetime.date.today,verbose_name='Creation Date')
  updated_date = models.DateField(default=datetime.date.today,verbose_name='Updated Date')

  class Meta:
      db_table = 'tb_user'
      ordering = ["username"]
      verbose_name_plural = "Users"

  def __unicode__(self):
    return self.username

