from django import forms
from .models import Lg ,Register
import bleach
from django.contrib.auth.hashers import make_password
from django.utils.html import escape
from django.utils.safestring import mark_safe
from bleach import clean

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Lg
        fields = ['name', 'password']

    def clean_name(self):
        name = self.cleaned_data['name']
        return bleach.clean(name, strip=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Register
        fields = ['name', 'email', 'password']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(len(name)) 
        return clean(name,strip=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = clean(email, strip=True)
        email = escape(email)
        print(len(email)) 
        return mark_safe(email)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        print(len(password))
        return password