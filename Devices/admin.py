# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Devices.models import Device

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display=('device','category')

admin.site.register(Device,DeviceAdmin)