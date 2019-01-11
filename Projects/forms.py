from django import forms
from Projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'

        widgets={
            'user':forms.HiddenInput(),
            'project':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'device':forms.SelectMultiple(attrs={'class':'form-control'}),
            'features':forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'budget':forms.TextInput(attrs={'class':'form-control'}),
            'payPerBug':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.HiddenInput(),
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['project','status','location','features','payPerBug']

        widgets={
            'project':forms.HiddenInput(),
            'status':forms.Select(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'features':forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'payPerBug':forms.TextInput(attrs={'class':'form-control'}),
        }