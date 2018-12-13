# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Proyectos.models import Proyecto
from Proyectos.forms import ProyectoForm, ModificarProyectoForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, template_name='Proyectos/inicio.html')

def lista(request):
    proyectos=Proyecto.objects.all()
    return render(request, template_name='Proyectos/proyectos.html',context={'proyectos':proyectos})

def consulta(request, pk):
    proyecto=Proyecto.objects.get(id=pk)
    return render(request, template_name='Proyectos/consultas.html',context={'proyecto':proyecto})

class AltaProyecto(SuccessMessageMixin, CreateView):
    model=Proyecto
    success_url = '/lista/'
    success_message = "%(nombreDelProyecto)s ha sido agregado"
    form_class=ProyectoForm
    template_name='Proyectos/altaProyecto.html'

    def get_success_url(self):
        return reverse('proyectos:lista')

class modificarProyecto(SuccessMessageMixin, UpdateView):
    model=Proyecto
    success_url = '/lista/'
    success_message = "%(nombreDelProyecto)s ha sido modificado"
    form_class=ModificarProyectoForm
    template_name='Proyectos/modificacionProyecto.html'

    def get_success_url(self):
        return reverse('proyectos:lista')

class eliminarProyecto(SuccessMessageMixin, DeleteView):
    model=Proyecto
    success_url = '/lista/'
    success_message = "%(nombreDelProyecto)s ha sido eliminado"
    form_class=ProyectoForm
    template_name='Proyectos/eliminarProyecto.html'

    def get_context_data(self, **kwargs):
        context_data = super(eliminarProyecto, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        proyecto=Proyecto.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(eliminarProyecto, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('proyectos:lista')