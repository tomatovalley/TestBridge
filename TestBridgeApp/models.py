
from __future__ import unicode_literals
from django.db import models
import datetime

USER_TYPE_CHOICES = (
     ('TESTER','Tester'),
     ('CLIENT','Client'),
 )

class page(models.Model):
  title = models.CharField(max_length=60)
  permalink = models.CharField(max_length=12, unique=True)
  update_date = models.DateTimeField('Last Updated')
  bodytext = models.TextField('Page Content', unique=True)

  class Meta:
      db_table = 'page'

  def __unicode__(self):
    return self.title


class tb_user(models.Model):
  username = models.CharField(max_length=100,unique=True)
  user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
  company = models.CharField(max_length=100, null=True, blank=True)
  phone_number = models.CharField(max_length=15)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30)
  country = models.CharField(max_length=30)
  creation_date = models.DateField(default=datetime.date.today)
  updated_date = models.DateField(default=datetime.date.today)

  class Meta:
      db_table = 'tb_user'
      ordering = ["username"]
      verbose_name_plural = "Users"

  def __unicode__(self):
    return self.username




