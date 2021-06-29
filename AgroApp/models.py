from django.db import models
from django.conf import settings
from Usuario.models import Usuario

# Create your models here.

class Producto(models.Model):
    ''' Dentro de esta clase podemos encontrar atributos tales como id_producto, nombre_producto, 
    tipo_producto, precio_producto los cuales son obligatorios, y también algunos opcionales como 
    descripción_producto y descuento_producto. Todo esto para lograr un correcto funcionamiento 
    con todo lo relacionado a Producto '''
    nombre = models.CharField(max_length=200)
    tipo_producto_opciones = (
        ('VERDURA', 'VERDURA'),
        ('FRUTA', 'FRUTA'),
        ('CARNE', 'CARNE'),
        ('CEREALES', 'CEREALES'),
        ('LIQUIDOS', 'LIQUIDOS'),
    )
    tipo_producto = models.CharField(max_length=10, choices=tipo_producto_opciones)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=1000, null=True)
    descuento = models.PositiveIntegerField(null=True)
    imagen = models.ImageField(upload_to='producto/', default="",null=False, blank=False, verbose_name="Foto de producto")
    usuario = models.ForeignKey(Usuario , related_name='productos', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f' {self.nombre}'

class Reporte(models.Model):
    ''' Aquí podemos ver atributos como id_reporte, razón_reporte y evidencia_reporte como opcional, 
    de este modo el usuario al momento de utilizar la página podrá utilizar la opción de reportar. '''
    razon = models.CharField(max_length=100)
    evidencia = models.ImageField(null=True)
    producto = models.ForeignKey(Producto, related_name='reportes', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return f'{self.razon}'

class ListaDeseos(models.Model):
    ''' En lista de deseos se encuentran los atributos id_lista e id_producto, 
    pero este último es opcional, ya que cada usuario tiene acceso a una lista de deseos, 
    pero no necesariamente deben tener productos agregados. '''
    producto = models.ForeignKey(Producto, related_name='lista_deseos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='lista_deseos', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Listas de deseos'

    def __str__(self):
        return f'{self.usuario}'


class Comunidad(models.Model):
    ''' Los atributos que podemos visualizar en esta clase son id_comunidad y 
    nombre_comunidad, los cuales serán necesarios para que el vendedor 
    pueda crear de forma correcta una comunidad entre sus clientes. '''
    nombre = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey(Usuario, related_name='comunidades', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comunidades'

    def __str__(self):
        return f'{self.nombre}'


class Venta(models.Model):
    ''' Dentro de esta clase podemos encontrar atributos que están relacionados al momento en 
    que se realiza una venta de un producto y sus atributos para el correcto funcionamiento 
    los cuales son id_venta, id_producto y monto_venta. '''
    monto_venta = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, related_name='ventas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='ventas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f'{self.producto}'

class HistorialCompra(models.Model):
    ''' Los atributos que incluye esta clase son id_historial e id_venta, 
    y su finalidad es crear un historial de compra para el usuario en caso de
    que este haya realizado alguna en algún momento. '''
    venta = models.ForeignKey(Venta, related_name='historial_de_compras', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Historiales de compra'

    def __str__(self):
        return f'{self.venta}'
