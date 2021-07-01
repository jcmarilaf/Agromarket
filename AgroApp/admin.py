from django.contrib import admin
from .models import Producto,Comunidad,ListaDeseos

# Register your models here.
admin.site.register(Producto)
admin.site.register(Comunidad)
admin.site.register(ListaDeseos)