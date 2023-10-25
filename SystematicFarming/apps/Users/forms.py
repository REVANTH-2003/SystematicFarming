from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required',
            'name': 'email',
            'type':'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Enter your password',
            'required': 'required',
            'name': 'password',
        })
    )

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password', 'profile')
        widgets = {
        'fullname': forms.TextInput(attrs={
            'placeholder': 'Enter your Fullname',
            'required': 'required',
            'name': 'fullname',
            'type':'text'
        }),
        'email': forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required',
            'name': 'email',
            'type':'email'
        }),

        'password': forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Enter your password',
            'required': 'required',
            'name': 'password',
        }),

        'profile' :forms.FileInput(attrs = { 
        'id':'formFile',
        'name':'profile',
        'required':'required'
        })
        }