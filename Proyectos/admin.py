# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Proyectos.models import Proyecto
# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    list_display=('nombreDelProyecto','tipo','dispositivo')

admin.site.register(Proyecto,ProyectoAdmin)