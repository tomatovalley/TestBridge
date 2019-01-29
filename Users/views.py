# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, Http404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserCreateForm, UserEditForm, UserProfileForm
from .models import Tb_user

class UserRegister(CreateView):
  template_name = 'Users/register.html'
  form_class = UserCreateForm
  success_url = reverse_lazy('usersapp:register_success')
  
  def form_valid(self, form):
    form.save()
    profile = Tb_user(username=form.cleaned_data['username'],user_type=form.cleaned_data['user_type'].upper())
    profile.save()
    return HttpResponseRedirect(self.success_url)

@login_required
def user_edit(request, username):
  submitted = False
  if request.method == 'POST':
    user_form = UserEditForm(request.POST,instance=User.objects.get(username=username))
    profile_form = UserProfileForm(request.POST,instance=Tb_user.objects.get(username=username))

    if all([user_form.is_valid(), profile_form.is_valid()]):
       user_form.save()
       profile_form.save()
       submitted = True
       return render(request,'Users/user_profile.html',{'user_form':user_form,'profile_form':profile_form,'submitted':submitted},)
  else:
    user_form = UserEditForm(instance=User.objects.get(username=username))
    profile_form = UserProfileForm(instance=Tb_user.objects.get(username=username))
  return render(request,'Users/user_profile.html',{'user_form':user_form,'profile_form':profile_form})

@login_required
def user_delete(request, username):
  try:
    user = User.objects.get(username=username)
    user.is_active = False
    user.save()
  except Exception as e:
     raise Http404
  return redirect('testbridgeapp:home')
