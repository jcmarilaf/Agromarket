from typing import ClassVar
from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')

        user = self.model(username=username,
                             email=self.normalize_email(email),
                             first_name=first_name,
                             last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(email,
                                   username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user




class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100, default="")
    email = models.EmailField('Email', max_length=254, unique=True, default="")
    first_name = models.CharField('Nombre', max_length=70, null=False, default="")
    last_name = models.CharField('Apellido', max_length=70, null=False, default="")
    fono = models.CharField(max_length=12, blank=True, null=True,  verbose_name="Teléfono usuario")
    direccion = models.CharField(max_length=100, null= True,  verbose_name="Dirección usuario")
    descripcionPerfil = models.CharField(max_length=500, null= True,  verbose_name="Descripción perfil")
    fotoPerfil = models.ImageField(default="image_default.png",upload_to='perfil/', null=False, blank=False,  verbose_name="Foto de perfil")
    cantidadProductos = IntegerField(blank= True, null=True,  verbose_name="Cantidad de productos")

    tipo_usuario_opciones = (
        ('Cliente', 'Cliente'),
        ('Vendedor', 'Vendedor'),
        ('Cliente y vendedor', 'Cliente y vendedor'),
    )

    tipo_Usuario = models.CharField(max_length=30, choices=tipo_usuario_opciones, null= True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
