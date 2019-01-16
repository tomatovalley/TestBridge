# -*- coding: utf-8 -*-
from django import forms
from .models import Bug
from django.forms.widgets import FileInput

class BugForm(forms.ModelForm):

    class Meta:
        model=Bug
        fields='__all__'

        widgets={
            'test_id':forms.Select(attrs={'class':'form-control'}),
            'error_found':forms.TextInput(attrs={'class':'form-control'}),
            'steps':forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 8}),
        }

class EditBugForm(forms.ModelForm):

    class Meta:
        model=Bug
        fields=['error_found','steps','screenshot']

        widgets={
            'error_found':forms.TextInput(attrs={'class':'form-control'}),
            'steps':forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 8}),
        }