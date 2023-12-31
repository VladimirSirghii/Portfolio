from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    # Adauga campuri suplimentare daca este necesar
    extra_field = forms.CharField()


class RegistrationForm(UserCreationForm):
    # Adauga campuri suplimentare daca este necesar
    extra_field = forms.CharField()
