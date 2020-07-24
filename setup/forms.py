from django.forms import ModelForm
from django import forms
from .models import UserInfo
from django.contrib.auth.models import User
class Register(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email')
class UserInfoForm(ModelForm):

     class Meta():
         model = UserInfo
         fields = ('title','blog','image')