# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Devices.models import Device
from Devices.forms import DeviceForm, EditDeviceForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from rest_framework import generics, mixins
from Devices.serializers import DevicesSerializer
from django.db.models import Q
# Create your views here.s

def list(request):
    devices=Device.objects.filter(user=request.user)
    return render(request, template_name='Devices/devices.html',context={'devices':devices})

def query(request, pk):
    devices=Device.objects.get(id=pk,user=request.user)
    return render(request, template_name='Devices/read.html',context={'devices':devices})

class CreateDevices(SuccessMessageMixin, CreateView):
    model=Device
    success_message = "The device %(device)s has been created"
    form_class=DeviceForm
    template_name='Devices/create.html'

    def get_initial(self):
        return {
             'user': self.request.user
        }

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
    template_name='Devices/delete.html'

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

class DeviceApiCQ(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field            = 'pk'
    serializer_class        = DevicesSerializer

    def get_queryset(self):
        qs = Device.objects.filter(user=self.request.user.id)
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class DeviceApiRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class = DevicesSerializer

    def get_queryset(self):
        return Device.objects.all()
