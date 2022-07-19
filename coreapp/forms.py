import email
from django import forms
from django.contrib.auth.models import User
from coreapp.models import Restourant

class UserForm(forms.ModelForm):
     email=forms.CharField(required=True,max_length=100)
     password=forms.CharField(widget=forms.PasswordInput())
     class Meta:
        
        model=User
        fields =("username","password","first_name","last_name","email")
class RestourantForm(forms.ModelForm):
    class Meta:
        model=Restourant
        fields=("name", "phone","adress","logo")