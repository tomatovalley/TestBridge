<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
  list_display = ('title','update_date')
  ordering = ('title',)
  search_fields = ('title',)


admin.site.register(Page, PageAdmin)
=======
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
>>>>>>> 1e76af9444df3aa6779f6bd26b224af9d9dea43c
