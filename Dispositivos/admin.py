# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Dispositivos.models import Dispositivo
# Register your models here.
class DispositivoAdmin(admin.ModelAdmin):
    list_display=('nombreDelDispositivo','categoria')

admin.site.register(Dispositivo,DispositivoAdmin)