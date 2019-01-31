# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.
class Device(models.Model):

    CATEGORY_DEVICE = (
        ('Computer', 'Computer'),
        ('Smartphone', 'Smartphone'),
    )

    OS_DEVICE = (
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac OS', 'Mac OS'),
        ('Android', 'Android'),
        ('IOS', 'IOS'),
    )

    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    device=models.CharField(max_length=200)
    category=models.CharField(max_length=30, choices=CATEGORY_DEVICE)
    os=models.CharField(max_length=50, choices=OS_DEVICE)
    version=models.CharField(max_length=200)
    creationDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)

    class Meta:
      db_table = 'device'

    def __str__(self):
        return self.device