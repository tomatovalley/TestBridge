# -*- coding: utf-8 -*-
from django import forms
from .models import Test


class TestForm(forms.ModelForm):

    class Meta:
        model=Test
        fields= ['user','name','functionality_id','device_id']

        widgets={
            'user':forms.HiddenInput(),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'functionality_id': forms.Select(attrs={'class':'form-control'}),
            'device_id':forms.Select(attrs={'class':'form-control'}),
        }

class EditTestForm(forms.ModelForm):

    class Meta:
        model=Test
        fields=['name','functionality_id','device_id']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'functionality_id':forms.Select(attrs={'class':'form-control'}),
            'device_id':forms.Select(attrs={'class':'form-control'}),
        }