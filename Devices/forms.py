<<<<<<< HEAD
from django import forms
from Devices.models import Device

class DeviceForm(forms.ModelForm):
    version=forms.CharField(label="OS Version",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Device
        fields='__all__'

        widgets={
            'user':forms.HiddenInput(),
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
        }

class EditDeviceForm(forms.ModelForm):
    version=forms.CharField(label="OS Version",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Device
        fields=['device','os','version']

        widgets={
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
=======
from django import forms
from Devices.models import Device

class DeviceForm(forms.ModelForm):
    version=forms.CharField(label="OS Version",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Device
        fields='__all__'

        widgets={
            'user':forms.HiddenInput(),
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
        }

class EditDeviceForm(forms.ModelForm):
    version=forms.CharField(label="OS Version",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Device
        fields=['device','os','version']

        widgets={
            'device':forms.TextInput(attrs={'class':'form-control'}),
            'os':forms.Select(attrs={'class':'form-control'}),
>>>>>>> 1e76af9444df3aa6779f6bd26b224af9d9dea43c
        }