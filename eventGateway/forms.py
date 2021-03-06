from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    admissionNumber = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'admissionNumber', 'email', 'password1', 'password2']