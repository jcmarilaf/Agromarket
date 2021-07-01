from django import forms
from django.forms import fields
from .models import Producto, Reporte, ListaDeseos, HistorialCompra ,Comunidad, Venta
from AgroApp import models

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['usuario','nombre','tipo_producto','precio','descripcion','imagen']

class ComunidadForm(forms.ModelForm):
    class Meta:
       model = Comunidad
       fields = ['nombre','usuario','creador']