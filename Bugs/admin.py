# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bug
# Register your models here.

class BugAdmin(admin.ModelAdmin):
  list_display = ('id',)
  ordering = ('id',)
  search_fields = ('id',)


admin.site.register(Bug, BugAdmin)
