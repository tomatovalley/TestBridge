
from __future__ import unicode_literals
from django.db import models
import datetime

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
  creation_date = models.DateField(default=datetime.date.today)
  updated_date = models.DateField(default=datetime.date.today)
  enabled = models.IntegerField(default=1)

  class Meta:
      db_table = 'tb_user'
      ordering = ["last_name","first_name"]
      verbose_name_plural = "Users"

  def __unicode__(self):
    return '%s %s' % (self.last_name,self.first_name)

  def full_name(self):
    "Return full name of the User."
    return '%s %s' % (self.last_name, self.first_name)


