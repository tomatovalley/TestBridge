# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms 

class ContactForm(forms.Form):
  subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.EmailField(required=False,label='Your e-mail address',widget=forms.TextInput(attrs={'class':'form-control'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

