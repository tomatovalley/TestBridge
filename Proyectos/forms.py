from django import forms
from Proyectos.models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model=Proyecto
        fields='__all__'

        widgets={
            'nombreDelProyecto':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            'ubicacion':forms.TextInput(attrs={'class':'form-control'}),
            'dispositivo':forms.Select(attrs={'class':'form-control'}),
            'caracteristicas':forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
            'topePresupuestal':forms.TextInput(attrs={'class':'form-control'}),
            'pagoPorBug':forms.TextInput(attrs={'class':'form-control'}),
        }