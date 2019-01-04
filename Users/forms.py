# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


from .models import Tb_user

USER_TYPE_CHOICES = (
     ('TESTER','Tester'),
     ('CLIENT','Client'),
 )

class UserCreateForm(UserCreationForm):
  email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
  user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control'}))
  password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label="Password confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ("username","first_name","last_name","email","password1","password2")
    
    widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }

  def __init__(self, *args, **kwargs):
    super(UserCreateForm, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None

  def save(self, commit=True):
    user=super(UserCreateForm,self).save(commit=False)
    user.email=self.cleaned_data["email"]
    user.first_name=self.cleaned_data["first_name"]
    user.last_name=self.cleaned_data["last_name"]
    if commit:
       user.save()
    return User


class UserEditForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('username','first_name','last_name','email')

    widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

  def __init__(self, *args, **kwargs):
    super(UserEditForm, self).__init__(*args, **kwargs)

    for fieldname in ['username']:
      self.fields[fieldname].help_text = None


class UserProfileForm(forms.ModelForm):

  class Meta:
    model = Tb_user
    fields = ('user_type','company','phone_number','address','city','state','country')

    widgets={
            'user_type':forms.Select(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
        }