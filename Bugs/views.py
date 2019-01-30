# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Bug
from .forms import BugForm, EditBugForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


def list(request):
    bugs = Bug.objects.filter(user=request.user)
    return render(request, template_name='Bugs/bugs.html',context={'bugs':bugs})

def query(request, pk):
    bug=Bug.objects.get(id=pk,user=request.user)
    return render(request, template_name='Bugs/read.html',context={'bug':bug})

class CreateBug(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model=Bug
    success_message = "The bug has been created"
    form_class=BugForm
    template_name='Bugs/create.html'

    def get_initial(self):
      return {'user': self.request.user }

    def get_success_url(self):
        return reverse('bugs:list')

class EditBug(SuccessMessageMixin, UpdateView):
    model=Bug
    success_message = "The bug has been modified"
    form_class=EditBugForm
    template_name='Bugs/update.html'

    def get_success_url(self):
        return reverse('bugs:list')

class DeleteBug(SuccessMessageMixin, DeleteView):
    model=Bug
    success_message = "The bug has been removed"
    form_class=BugForm
    template_name='Bugs/delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(DeleteBug, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        bug=Bug.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(DeleteBug, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('bugs:list')