from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'id': 'password-field',
            'class': 'password-input',
        }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'id': 'password-field',
            'class': 'password-input',
        }))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'id': 'password-field',
            'class': 'password-input',
        }))
    

# forms.py

from django import forms

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
