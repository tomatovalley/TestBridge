from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ContactForm, UserCreateForm, UserEditForm, UserProfileForm
from .models import tb_user

def home(request):
  return render(request,"TestBridgeApp/home.html")


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


class Register(CreateView):
  template_name = 'registration/register.html'
  form_class = UserCreateForm
  success_url = reverse_lazy('register-success')
  
  def form_valid(self, form):
    form.save()
    profile = tb_user(username=form.cleaned_data['username'],user_type=form.cleaned_data['user_type'].upper())
    print form.cleaned_data['username']
    print form.cleaned_data['user_type'].upper()
    print profile.username
    print profile.user_type.upper()
    profile.save()
    return HttpResponseRedirect(self.success_url)

@login_required
def user_edit(request, username):
  submitted = False
  if request.method == 'POST':
    user_form = UserEditForm(request.POST,instance=User.objects.get(username=username))
    profile_form = UserProfileForm(request.POST,instance=tb_user.objects.get(username=username))

    if all([user_form.is_valid(), profile_form.is_valid()]):
       user_form.save()
       profile_form.save()
       submitted = True
       return render(request,'TestBridgeApp/user_profile.html',{'user_form':user_form,'profile_form':profile_form,'submitted':submitted},)
  else:
    user_form = UserEditForm(instance=User.objects.get(username=username))
    profile_form = UserProfileForm(instance=tb_user.objects.get(username=username))
  return render(request,'TestBridgeApp/user_profile.html',{'user_form':user_form,'profile_form':profile_form})
