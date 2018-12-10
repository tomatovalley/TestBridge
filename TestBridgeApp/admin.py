# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import tb_user, page



class PageAdmin(admin.ModelAdmin):
  list_display = ('title','update_date')
  ordering = ('title',)
  search_fields = ('title',)
  
admin.site.register(tb_user)
admin.site.register(page, PageAdmin)