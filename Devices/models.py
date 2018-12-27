# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    device=models.CharField(max_length=200)
    category=models.CharField(max_length=30, choices=CATEGORY_DEVICE)
    os=models.CharField(max_length=50, choices=OS_DEVICE)
    version=models.CharField(max_length=200)

    def __str__(self):
        return self.device