from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from .forms import ContactForm

from Devices.models import Device
from Projects.models import Project, Functionality
from Bugs.models import Bug
from TestBridgeApp.models import ProjectsTester

from django.contrib.auth.models import User

def home(request):
  devices=Device.objects.filter(user=request.user.id).count()
  projects=Project.objects.filter(user=request.user.id).count()
  bugs=Bug.objects.filter(user=request.user.id).count()

  context={
    'devices':devices,
    'projects':projects,
    'bugs':bugs,
  }

  return render(request,"TestBridgeApp/home.html", context)

def projectsCustomers(request):
  projects=Project.objects.filter(type='Web').order_by('-creationDate')
  return render(request,"TestBridgeApp/projectsCustomers.html", {'projects':projects})

def query(request, pk):
    project=Project.objects.get(id=pk)
    functionalities=Functionality.objects.filter(project=pk)
    device=Project.objects.get(pk=pk).device.all()
    return render(request, template_name='TestBridgeApp/projectDetail.html',context={'projects':project, 'device':device, 'functionalities':functionalities})

def saveProject(request, pk):
  projects=ProjectsTester.objects.create(user=request.user, project_id=pk)
  return redirect('testbridgeapp:customers')

def start(request):
  return render(request,"TestBridgeApp/start_home.html")

def pricing(request):
  return render(request,"TestBridgeApp/start_Pricing.html")

def resources(request):
  return render(request,"TestBridgeApp/start_Resources.html")

def testingSolutions(request):
  return render(request,"TestBridgeApp/start_testingSolutions.html")

def testing(request):
  return render(request,"TestBridgeApp/testing.html")


def contact(request):
  submitted = False
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      con = get_connection('django.core.mail.backends.console.EmailBackend')
      send_mail(cd['subject'],
              cd['message'],
              cd.get('email','noreply@example.com'), ['siteowner@exmple.com'], connection=con)
      return HttpResponseRedirect('/contact?submitted=True')
  else:
    form = ContactForm()
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'TestBridgeApp/contact.html',{'form':form,'submitted': submitted})