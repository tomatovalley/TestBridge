from django import forms
from Projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'

        widgets={
            'project':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'device':forms.Select(attrs={'class':'form-control'}),
            'features':forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'budget':forms.TextInput(attrs={'class':'form-control'}),
            'payPerBug':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['project','location','features','payPerBug']

        widgets={
            'project':forms.HiddenInput(),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'features':forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'payPerBug':forms.TextInput(attrs={'class':'form-control'}),
        }