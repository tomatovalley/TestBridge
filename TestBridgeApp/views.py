from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.views.generic.edit import CreateView

from .forms import ContactForm, UserCreateForm
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
    p1 = tb_user(username=form.cleaned_data.get('username'))
    p1.save()
    return HttpResponseRedirect(self.success_url)



