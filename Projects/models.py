# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):

    TYPES_DEVELOPMENT = (
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
    )

    DEVICES_TEST = (
        ('Computer', 'Computer'),
        ('Smartphone', 'Smartphone'),
    )

    project=models.CharField(max_length=70)
    type=models.CharField(max_length=30, choices=TYPES_DEVELOPMENT)
    location=models.URLField(max_length=300)
    device=models.CharField(max_length=50, choices=DEVICES_TEST)
    features=models.CharField(max_length=400)
    budget=models.DecimalField(max_digits=10, decimal_places=2)
    payPerBug=models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'{}'.format(self.project)