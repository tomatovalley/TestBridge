# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Proyectos.models import Proyecto
from Proyectos.forms import ProyectoForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

# Create your views here.
def inicio(request):
    return render(request, template_name='Proyectos/inicio.html')

def lista(request):
    proyectos=Proyecto.objects.all()
    return render(request, template_name='Proyectos/proyectos.html',context={'proyectos':proyectos})

def consulta(request, pk):
    proyecto=Proyecto.objects.get(id=pk)
    return render(request, template_name='Proyectos/consultas.html',context={'proyecto':proyecto})

class AltaProyecto(CreateView):
    model=Proyecto
    form_class=ProyectoForm
    template_name='Proyectos/altaProyecto.html'

    def get_success_url(self):
        return reverse('proyectos:lista')

class modificarProyecto(UpdateView):
    model=Proyecto
    form_class=ProyectoForm
    template_name='Proyectos/modificacionProyecto.html'

    def get_success_url(self):
        return reverse('proyectos:lista')

class eliminarProyecto(DeleteView):
    model=Proyecto
    form_class=ProyectoForm
    template_name='Proyectos/eliminarProyecto.html'

    def get_context_data(self, **kwargs):
        context_data = super(eliminarProyecto, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        proyecto=Proyecto.objects.get(id=int(pk))
        return context_data

    def get_success_url(self):
        return reverse('proyectos:lista')