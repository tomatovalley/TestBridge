# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=('project','type')

admin.site.register(Project,ProjectAdmin)