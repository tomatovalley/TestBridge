# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from Devices.models import Device
# Create your models here.
class Project(models.Model):

    TYPES_DEVELOPMENT = (
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
    )

    STATUS_PROJECT = (
        ('Active', 'Active'),
        ('Pause', 'Pause'),
        ('Inactive', 'Inactive'),
    )

    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    project=models.CharField(max_length=70)
    type=models.CharField(max_length=30, choices=TYPES_DEVELOPMENT)
    location=models.URLField(max_length=300)
    device=models.ManyToManyField(Device)
    features=models.CharField(max_length=400)
    budget=models.DecimalField(max_digits=10, decimal_places=2)
    payPerBug=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=50, choices=STATUS_PROJECT, default="Active")
    creationDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{}'.format(self.project)

    @staticmethod
    def device_list():
       return Project.device.all()