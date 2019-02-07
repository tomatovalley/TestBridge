# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from Projects.models import Project

class Page(models.Model):
  title = models.CharField(max_length=60)
  permalink = models.CharField(max_length=12, unique=True)
  update_date = models.DateTimeField('Last Updated')
  bodytext = models.TextField('Page Content', unique=True)

  class Meta:
      db_table = 'page'

  def __unicode__(self):
    return self.title

class ProjectsTester(models.Model):
  user=models.ForeignKey(settings.AUTH_USER_MODEL)
  project=models.ForeignKey(Project,on_delete=models.CASCADE)

