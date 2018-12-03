# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from TestBridgeApp.forms import RegUserForm

def RegUser(request):
  if request.method == 'POST':
    form = RegUserForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
	  # hacer algo aqui
      return HttpResponseRedirect('/register/ok/')
  else:
    form = RegUserForm()
  return render(request, 'register-user.html', {'form':form})
