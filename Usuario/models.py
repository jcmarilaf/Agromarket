from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver


class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True, verbose_name="Id de tipo de usuario")
    nombreTipoUsuario = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de tipo usuario")


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fono = models.CharField(max_length=12, blank=True, null=True,  verbose_name="Teléfono usuario")
    direccion = models.CharField(max_length=100, null= True,  verbose_name="Dirección usuario")
    descripcionPerfil = models.CharField(max_length=500, null= True,  verbose_name="Descripción perfil")
    fotoPerfil = models.ImageField(default="sinfoto.jpg", null=False, blank=False,  verbose_name="Foto de perfil")
    cantidadProductos = IntegerField(blank= True, null=True,  verbose_name="Cantidad de productos")
    #tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING)

    tipo_usuario_opciones = (
        ('Cliente', 'Cliente'),
        ('Vendedor', 'Vendedor'),
        ('Cliente y vendedor', 'Cliente y vendedor'),
    )
    tipo_Usuario = models.CharField(max_length=30, choices=tipo_usuario_opciones, null= True)

    def __str__(self):
        return str(self.fono)



@receiver(post_save, sender=User)
def update_user_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)
    instance.usuario.save()
