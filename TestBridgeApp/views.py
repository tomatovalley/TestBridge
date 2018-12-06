
from __future__ import unicode_literals

from django.shortcuts import render
from TestBridgeApp.forms import RegisterUserForm

def RegisterUser(request):
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
    form.save()
  context = {'form':form}

  return render(request,'TestBridgeApp/register-user.html',context)

