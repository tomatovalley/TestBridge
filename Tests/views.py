# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Test
from .forms import TestForm, EditTestForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def list(request):
    tests = Test.objects.filter(user=request.user)
    return render(request, template_name='Tests/tests.html',context={'tests':tests})

def query(request, pk):
    test=Test.objects.get(id=pk,user=request.user)
    return render(request, template_name='Tests/read.html',context={'test':test})

class CreateTest(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model=Test
    success_message = "The test has been created"
    form_class=TestForm
    template_name='Tests/create.html'

    def get_initial(self):
      return { 'user': self.request.user }

    def get_success_url(self):
        return reverse('tests:list')

class EditTest(SuccessMessageMixin, UpdateView):
    model=Test
    success_message = "The test has been modified"
    form_class=EditTestForm
    template_name='Tests/update.html'

    def get_success_url(self):
        return reverse('tests:list')

class DeleteTest(SuccessMessageMixin, DeleteView):
    model=Test
    success_message = "The test  has been removed"
    form_class=TestForm
    template_name='Tests/delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(DeleteTest, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        test=Test.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(DeleteTest, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tests:list')