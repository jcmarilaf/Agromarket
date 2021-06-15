from django.db import models
from django.conf import settings

# Create your models here.

class Producto(models.Model):
    ''' Descripción de la clase '''
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    tipo_producto_opciones = (
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
    )
    tipo_producto = models.CharField(max_length=10, choices=tipo_producto_opciones)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=1000, null=True)
    descuento = models.PositiveIntegerField(null=True)

class Reporte(models.Model):
    ''' A '''
    codigo = models.CharField(max_length=10, unique=True)
    razon = models.CharField(max_length=100)
    evidencia = models.ImageField(null=True)
    producto = models.ForeignKey(Producto, related_name='reportes', on_delete=models.CASCADE)

class ListaDeseos(models.Model):
    ''' A '''
    codigo = models.CharField(max_length=10, unique=True)
    producto = models.ForeignKey(Producto, related_name='reportes', on_delete=models.CASCADE)


class Comunidad(models.Model):
    ''' A '''
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100, unique=True)


class Venta(models.Model):
    ''' A '''
    codigo = models.CharField(max_length=10, unique=True)
    monto_venta = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, related_name='reportes', on_delete=models.CASCADE)


class HistorialCompra(models.Model):
    ''' A '''
    codigo = models.CharField(max_length=10, unique=True)
    venta = models.ForeignKey(Venta, related_name='historial_de_compras', on_delete=models.CASCADE)
