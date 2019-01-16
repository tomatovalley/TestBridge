# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from Functionalities.models import Functionality
from Functionalities.forms import FuncionalityForm, EditFuncionalityForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

def list(request):
    functionalities=Functionality.objects.all()
    return render(request, template_name='Functionalities/functionalities.html',context={'functionalities':functionalities})

def query(request, pk):
    functionalities=Functionality.objects.get(id=pk)
    return render(request, template_name='Functionalities/read.html',context={'functionalities':functionalities})

class CreateFunctionality(SuccessMessageMixin, CreateView):
    model=Functionality
    form_class=FuncionalityForm
    template_name='Functionalities/create.html'

    def get_success_url(self):
        return reverse('functionalities:list')

class EditFunctionality(SuccessMessageMixin, UpdateView):
    model=Functionality
    form_class=EditFuncionalityForm
    template_name='Functionalities/update.html'

    def get_success_url(self):
        return reverse('functionalities:list')

class DeleteFunctionality(SuccessMessageMixin, DeleteView):
    model=Functionality
    form_class=FuncionalityForm
    template_name='Functionalities/delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(DeleteFunctionality, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        devices=Functionality.objects.get(id=int(pk))
        return context_data

    def get_success_url(self):
        return reverse('functionalities:list')