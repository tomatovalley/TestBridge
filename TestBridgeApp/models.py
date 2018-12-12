# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Page(models.Model):
  title = models.CharField(max_length=60)
  permalink = models.CharField(max_length=12, unique=True)
  update_date = models.DateTimeField('Last Updated')
  bodytext = models.TextField('Page Content', unique=True)

  class Meta:
      db_table = 'page'

  def __unicode__(self):
    return self.title






