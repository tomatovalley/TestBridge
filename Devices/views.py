# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Devices.models import Device
from Devices.forms import DeviceForm, EditDeviceForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.

def list(request):
    devices=Device.objects.all()
    return render(request, template_name='Devices/Devices.html',context={'devices':devices})

def query(request, pk):
    devices=Device.objects.get(id=pk)
    return render(request, template_name='Devices/read.html',context={'devices':devices})

class CreateDevices(SuccessMessageMixin, CreateView):
    model=Device
    success_message = "The device %(device)s has been created"
    form_class=DeviceForm
    template_name='Devices/create.html'

    def get_success_url(self):
        return reverse('devices:list')

class EditDevices(SuccessMessageMixin, UpdateView):
    model=Device
    success_message = "The device %(device)s has been modified"
    form_class=EditDeviceForm
    template_name='Devices/update.html'

    def get_success_url(self):
        return reverse('devices:list')

class DeleteDevices(SuccessMessageMixin, DeleteView):
    model=Device
    success_message = "The device %(device)s has been removed"
    form_class=DeviceForm
    template_name='devices/delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(DeleteDevices, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        devices=Device.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(DeleteDevices, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('devices:list')