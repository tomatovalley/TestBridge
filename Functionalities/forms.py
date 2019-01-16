from django import forms
from Functionalities.models import Functionality

class FuncionalityForm(forms.ModelForm):
    class Meta:
        model=Functionality
        fields=['title','description']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditFuncionalityForm(forms.ModelForm):
    class Meta:
        model=Functionality
        fields=['title','description','status']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(attrs={'class':'form-control'}),
        }