
from __future__ import unicode_literals

from django.shortcuts import render


from django.http.response import HttpResponseForbidden
from django.views.generic import CreateView
from TestBridgeApp.forms import RegisterUserForm
from django.http import HttpResponse

class RegisterUserView(CreateView):
  form_class = RegisterUserForm
  template_name = "TestBridgeApp/register-user.html"

  def dispatch(self, request,*args,**kwargs):
    if request.user.is_authenticated():
      return HttpResponseForbidden()
    return super(RegisterUserView, self).dispatch(request,*args,**kwargs)

  def form_valid(self, form):
    user = form.save(commit=False)
    user.save()

    return HttpResponse('User registered')

