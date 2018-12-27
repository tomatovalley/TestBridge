from django import forms
from Devices.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model=Device
        fields='__all__'

        widgets={
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
            'version':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditDeviceForm(forms.ModelForm):
    class Meta:
        model=Device
        fields=['device','os','version']

        widgets={
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
            'version':forms.TextInput(attrs={'class':'form-control'}),
        }