# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dispositivo(models.Model):

    CATEGORIA_EQUIPO = (
        ('Computadora', 'Computadora'),
        ('Smartphone', 'Smartphone'),
    )

    SO_DISPOSITIVO = (
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac', 'Mac'),
        ('Android', 'Android'),
        ('IOS', 'IOS'),
    )

    nombreDelDispositivo=models.CharField(max_length=200)
    categoria=models.CharField(max_length=30, choices=CATEGORIA_EQUIPO)
    sistemaOperativo=models.CharField(max_length=50, choices=SO_DISPOSITIVO)
    version=models.CharField(max_length=200)

    def __unicode__(self):
        return u'{}'.format(self.nombreDelDispositivo)