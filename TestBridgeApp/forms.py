from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import tb_user
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
  email = forms.EmailField(required=True)
  user_type = forms.CharField(required=True)

  class Meta:
    model = User
    fields = ("username","first_name","last_name","email","password1","password2")

  def __init__(self, *args, **kwargs):
    super(UserCreateForm, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None

  def save(self, commit=True):
    user=super(UserCreateForm,self).save(commit=False)
    user.email=self.cleaned_data["email"]
    user.first_name=self.cleaned_data["first_name"]
    user.last_name=self.cleaned_data["last_name"]
    if commit:
       user.save()
    return User


class ContactForm(forms.Form):
  subject = forms.CharField(max_length=100)
  email = forms.EmailField(required=False,label='Your e-mail address')
  message = forms.CharField(widget=forms.Textarea)

class UserEditForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('username','first_name','last_name','email')

class UserProfileForm(forms.ModelForm):

  class Meta:
    model = tb_user
    fields = ('user_type','company','phone_number','address','city','state','country')
