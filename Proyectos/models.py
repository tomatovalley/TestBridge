# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proyecto(models.Model):

    TIPOS_DESARROLLO = (
        ('Web', 'Web'),
        ('Movil', 'Movil'),
    )

    DISPOSITIVOS_TEST = (
        ('Computadora', 'Computadora'),
        ('Smartphone', 'Smartphone'),
    )

    nombreDelProyecto=models.CharField(max_length=70)
    tipo=models.CharField(max_length=30, choices=TIPOS_DESARROLLO)
    ubicacion=models.URLField(max_length=300)
    dispositivo=models.CharField(max_length=50, choices=DISPOSITIVOS_TEST)
    caracteristicas=models.CharField(max_length=400)
    topePresupuestal=models.DecimalField(max_digits=10, decimal_places=2)
    pagoPorBug=models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'{}'.format(self.nombreDelProyecto)