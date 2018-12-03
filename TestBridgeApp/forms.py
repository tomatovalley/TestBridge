from django import forms

class RegUserForm(forms.Form):
  firt_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput())
  username = forms.CharField()
  user_type = forms.CharField()
  company = forms.CharField(required=False)
  phone_number = forms.CharField()
  address = forms.CharField()
  city = forms.CharField()
  state = forms.CharField()
  country = forms.CharField()
