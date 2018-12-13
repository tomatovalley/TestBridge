# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Dispositivos.models import Dispositivo
from Dispositivos.forms import DispositivoForm, EditarDispositivoForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, template_name='Dispositivos/inicio.html')

def lista(request):
    dispositivos=Dispositivo.objects.all()
    return render(request, template_name='Dispositivos/dispositivos.html',context={'dispositivos':dispositivos})

def consulta(request, pk):
    dispositivo=Dispositivo.objects.get(id=pk)
    return render(request, template_name='Dispositivos/consultas.html',context={'dispositivo':dispositivo})

class AltaDispositivo(SuccessMessageMixin, CreateView):
    model=Dispositivo
    success_url = '/lista/'
    success_message = "%(nombreDelDispositivo)s ha sido agregado"
    form_class=DispositivoForm
    template_name='Dispositivos/altaDispositivo.html'

    def get_success_url(self):
        return reverse('dispositivos:lista')

class modificarDispositivo(SuccessMessageMixin, UpdateView):
    model=Dispositivo
    success_url = '/lista/'
    success_message = "%(nombreDelDispositivo)s ha sido modificado"
    form_class=EditarDispositivoForm
    template_name='Dispositivos/modificarDispositivo.html'

    def get_success_url(self):
        return reverse('dispositivos:lista')

class eliminarDispositivo(SuccessMessageMixin, DeleteView):
    model=Dispositivo
    success_url = '/lista/'
    success_message = "%(nombreDelDispositivo)s ha sido eliminado"
    form_class=DispositivoForm
    template_name='Dispositivos/eliminarDispositivo.html'

    def get_context_data(self, **kwargs):
        context_data = super(eliminarDispositivo, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        dispositivo=Dispositivo.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(eliminarDispositivo, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('dispositivos:lista')