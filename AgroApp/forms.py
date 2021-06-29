from django import forms
from django.forms import fields
from .models import Producto, Reporte, ListaDeseos, HistorialCompra ,Comunidad, Venta

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['usuario','nombre','tipo_producto','precio','descripcion','imagen']
