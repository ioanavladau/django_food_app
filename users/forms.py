from django import forms
from django.contrib.auth.models import User #User model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # meta class is a class that provides information about the class itself
    class Meta: # meta will hold information about the RegisterForm class
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
