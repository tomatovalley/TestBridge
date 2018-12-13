from django import forms
from Dispositivos.models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model=Dispositivo
        fields='__all__'

        widgets={
            'nombreDelDispositivo':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'sistemaOperativo':forms.Select(attrs={'class':'form-control'}),
            'version':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditarDispositivoForm(forms.ModelForm):
    class Meta:
        model=Dispositivo
        fields=['nombreDelDispositivo','sistemaOperativo','version']

        widgets={
            'nombreDelDispositivo':forms.TextInput(attrs={'class':'form-control'}),
            'sistemaOperativo':forms.Select(attrs={'class':'form-control'}),
            'version':forms.TextInput(attrs={'class':'form-control'}),
        }