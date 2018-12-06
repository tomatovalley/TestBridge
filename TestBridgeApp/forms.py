from django import forms 
from TestBridgeApp.models import tb_user
from django.db import models

class RegisterUserForm(forms.ModelForm):
  #password2 = forms.CharField(label='Confirm password',max_length=100)

  class Meta:
   model = tb_user
   fields = '__all__'
   exclude = ('creation_date','updated_date','enabled')
   

  # password validation
  #def clean_password(self):
  #  cd = self.cleaned_data
  #  if cd['password2'] != cd['password']:
  #     raise ValidacionError("Password don't match")
  #  return cd['password']