# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class tb_user(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  password = models.CharField(max_length=30)
  username = models.CharField(max_length=30, null=True, blank=True)
  user_type = models.CharField(max_length=30)
  company = models.CharField(max_length=100, null=True, blank=True)
  phone_number = models.CharField(max_length=15)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30)
  country = models.CharField(max_length=30)
  creation_date = models.DateField()
  updated_date = models.DateField()
  enabled = models.IntegerField()
  
  def __unicode__(self):
    return self.email
	
  class Meta:
        db_table = 'tb_user'