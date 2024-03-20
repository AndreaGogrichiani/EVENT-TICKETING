from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("role", 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    model = User
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'location', 'date', 'cost')