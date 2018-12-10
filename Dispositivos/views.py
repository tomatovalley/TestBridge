# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Dispositivos.models import Dispositivo
from Dispositivos.forms import DispositivoForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

# Create your views here.
def inicio(request):
    return render(request, template_name='Dispositivos/inicio.html')

def lista(request):
    dispositivos=Dispositivo.objects.all()
    return render(request, template_name='Dispositivos/dispositivos.html',context={'dispositivos':dispositivos})

def consulta(request, pk):
    dispositivo=Dispositivo.objects.get(id=pk)
    return render(request, template_name='Dispositivos/consultas.html',context={'dispositivo':dispositivo})

class AltaDispositivo(CreateView):
    model=Dispositivo
    form_class=DispositivoForm
    template_name='Dispositivos/altaDispositivo.html'

    def get_success_url(self):
        return reverse('dispositivos:lista')

class modificarDispositivo(UpdateView):
    model=Dispositivo
    form_class=DispositivoForm
    template_name='Dispositivos/modificarDispositivo.html'

    def get_success_url(self):
        return reverse('dispositivos:lista')

class eliminarDispositivo(DeleteView):
    model=Dispositivo
    form_class=DispositivoForm
    template_name='Dispositivos/eliminarDispositivo.html'

    def get_context_data(self, **kwargs):
        context_data = super(eliminarDispositivo, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        dispositivo=Dispositivo.objects.get(id=int(pk))
        return context_data

    def get_success_url(self):
        return reverse('dispositivos:lista')