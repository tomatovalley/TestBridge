# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from Projects.models import Project

# Create your models here.
class Functionality(models.Model):
    #project=models.ForeignKey(Project)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1500)
    creationDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title