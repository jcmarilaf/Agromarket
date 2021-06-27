from django.shortcuts import render, redirect
from .forms import ProductosForm
from .models import Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def agregar_producto(request):
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            model_instance = form
            model_instance.save()
            return redirect("inicio")
    else:
        form = ProductosForm()
        return render(request, "Producto/agregar_productos.html", {'form': form})