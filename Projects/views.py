# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from Projects.models import Project, Functionality
from Projects.forms import ProjectForm, EditProjectForm
from django.forms import inlineformset_factory

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.forms.widgets import Textarea, TextInput, CheckboxInput

from rest_framework import generics, mixins
from Projects.serializers import ProjectsSerializer
from django.db.models import Q

# Create your views here.

def list(request):
    projects=Project.objects.filter(user=request.user)
    return render(request, template_name='Projects/projects.html',context={'projects':projects})

@login_required
def query(request, pk):
    project=Project.objects.get(id=pk,user=request.user)
    functionalities=Functionality.objects.filter(project=pk)
    device=Project.objects.get(pk=pk).device.all()
    return render(request, template_name='Projects/read.html',context={'projects':project, 'device':device, 'functionalities':functionalities})

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
        return reverse('projects:functionalities',args=(self.object.id,))

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
    template_name='Projects/delete.html'

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

def functionalities(request, project_id):
    project=Project.objects.get(pk=project_id)

    FunctionalityFormSet=inlineformset_factory(
        Project,
        Functionality,
        fields=('title','description','status',),
        widgets={
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'status': CheckboxInput(attrs={'class':'form-check form-check-inline'})
        },
        can_delete=True,
        extra=1
    )

    if request.method == 'POST':
        formset=FunctionalityFormSet(request.POST, instance=project)
        if formset.is_valid():
            formset.save()

    formset=FunctionalityFormSet(instance=project)
    return render(request, 'Projects/functionalities.html', {'formset':formset})

class ProjectApiCQ(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field            = 'pk'
    serializer_class        = ProjectsSerializer

    def get_queryset(self):
        qs = Project.objects.filter(user=self.request.user.id)
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

class ProjectApiRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Project.objects.all()