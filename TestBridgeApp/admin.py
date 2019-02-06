# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page, ProjectsTester


class PageAdmin(admin.ModelAdmin):
  list_display = ('title','update_date')
  ordering = ('title',)
  search_fields = ('title',)

class ProjectsTesterAdmin(admin.ModelAdmin):
    list_display=('user','project')

admin.site.register(Page, PageAdmin)
admin.site.register(ProjectsTester)