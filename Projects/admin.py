<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Projects.models import Project, Functionality

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=('project','type')

class FunctionalitiesAdmin(admin.ModelAdmin):
    list_display=('title','status')

admin.site.register(Project,ProjectAdmin)
=======
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Projects.models import Project, Functionality

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=('project','type')

class FunctionalitiesAdmin(admin.ModelAdmin):
    list_display=('title','status')

admin.site.register(Project,ProjectAdmin)
>>>>>>> 1e76af9444df3aa6779f6bd26b224af9d9dea43c
admin.site.register(Functionality,FunctionalitiesAdmin)