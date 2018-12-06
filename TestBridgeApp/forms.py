from django import forms 
from TestBridgeApp.models import tb_user

class RegisterUserForm(forms.ModelForm):
  class Meta:
   model = tb_user
   fields = '__all__'
   exclude = ('creation_date','updated_date','enabled')
