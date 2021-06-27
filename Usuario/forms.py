from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class RegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'fono',
            'direccion',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'fotoPerfil',
            'fono',
            'direccion',
            'descripcionPerfil',
        ]