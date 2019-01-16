# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Projects.models import Project
from Projects.forms import ProjectForm, EditProjectForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    projects=Project.objects.filter(user=request.user)
    return render(request, template_name='Projects/projects.html',context={'projects':projects})

@login_required
def query(request, pk):
    project=Project.objects.get(id=pk)
    device=Project.objects.get(pk=pk).device.all()
    return render(request, template_name='Projects/read.html',context={'projects':project, 'device':device})

class CreateProject(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model=Project
    success_message = "The project %(project)s has been created"
    form_class=ProjectForm
    template_name='Projects/create.html'

    def get_initial(self):
        return {
             'user': self.request.user
        }

    def get_success_url(self):
        return reverse('projects:list')

class EditProject(SuccessMessageMixin, UpdateView):
    model=Project
    success_message = "The project %(project)s has been modified"
    form_class=EditProjectForm
    template_name='Projects/update.html'

    def get_success_url(self):
        return reverse('projects:list')

class DeleteProject(SuccessMessageMixin, DeleteView):
    model=Project
    success_message = "The project %(project)s has been removed"
    form_class=ProjectForm
    template_name='delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(DeleteProject, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        proyecto=Project.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(DeleteProject, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('projects:list')