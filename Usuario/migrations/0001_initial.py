# Generated by Django 3.2.4 on 2021-06-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='', max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(default='', max_length=70, verbose_name='Nombre')),
                ('last_name', models.CharField(default='', max_length=70, verbose_name='Apellido')),
                ('fono', models.CharField(blank=True, max_length=12, null=True, verbose_name='Teléfono usuario')),
                ('direccion', models.CharField(max_length=100, null=True, verbose_name='Dirección usuario')),
                ('descripcionPerfil', models.CharField(max_length=500, null=True, verbose_name='Descripción perfil')),
                ('fotoPerfil', models.ImageField(default='sinfoto.jpg', upload_to='perfil/', verbose_name='Foto de perfil')),
                ('cantidadProductos', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de productos')),
                ('tipo_Usuario', models.CharField(choices=[('Cliente', 'Cliente'), ('Vendedor', 'Vendedor'), ('Cliente y vendedor', 'Cliente y vendedor')], max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
