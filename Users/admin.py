# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tb_user


class UserAdmin(admin.ModelAdmin):
  list_display = ('username',)
  ordering = ('username',)
  search_fields = ('username',)


admin.site.register(Tb_user, UserAdmin)
