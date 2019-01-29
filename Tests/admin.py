# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test

# Register your models here.
class TestAdmin(admin.ModelAdmin):
  list_display = ('name',)
  ordering = ('id',)
  search_fields = ('name',)


admin.site.register(Test, TestAdmin)