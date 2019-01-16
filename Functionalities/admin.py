# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Functionalities.models import Functionality

# Register your models here.
class FunctionAdmin(admin.ModelAdmin):
    list_display=('title','status')

admin.site.register(Functionality,FunctionAdmin)