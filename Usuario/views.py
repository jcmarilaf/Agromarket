from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django import forms
from django.contrib.auth import login, authenticate
from . import models
from .models import Usuario


# Create your views here.

def Registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form_registro = RegistroForm(request.POST)
        if form_registro.is_valid():
            user = form_registro.save()
            user.refresh_from_db()
            user.usuario.fono = form_registro.cleaned_data.get('fono')
            user.usuario.direccion = form_registro.cleaned_data.get('direccion')
            user.usuario.descripcionPerfil = form_registro.cleaned_data.get('descripcionPerfil')
            user.usuario.fotoPerfil = form_registro.cleaned_data.get('fotoPerfil')
            user.usuario.cantidadProductos = form_registro.cleaned_data.get('cantidadProductos')
            user.usuario.tipo_Usuario = form_registro.cleaned_data.get('tipp_Usuario')
            user.save()
            raw_password = form_registro.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    
    else:
        form_registro = RegistroForm()
    return render(request, 'Usuario/registrar.html', {'form_registro': form_registro})



 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/perfil.html'

class SuccessLogin(ListView):
    model = User
    template_name = 'Usuario/successLogin.html'
