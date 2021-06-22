from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms
from django.utils.regex_helper import Choice
from .models import Usuario

#class RegistroForm(UserCreationForm):
#
#    class Meta:
#        model = User
#        fields = [
 #               'username',
  #              'first_name',
   #             'last_name',
    #            'email',
     #       ]
      #  labels = {
       #         'username': 'Nombre de usuario',
        #        'first_name': 'Nombre',
         #       'last_name': 'Apellidos',
          #      'email': 'Correo',
       # }


class RegistroForm(UserCreationForm):

    fono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)
    descripcionPerfil = forms.CharField(max_length=200)
    fotoPerfil = forms.ImageField()
    cantidadProductos = forms.IntegerField()
    #tipo_usuario_opciones = (
    #    ('Cliente', 'Cliente'),
    #    ('Vendedor', 'Vendedor'),
    #    ('Cliente y vendedor', 'Cliente y vendedor'),
    #)
    #tipo_Usuario = forms.CharField(choice=tipo_usuario_opciones)

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("Para registrarse debe ingresar sus nombres")
        return first_name.strip()

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise forms.ValidationError("Para registrarse debe ingresar sus apellidos")
        return last_name.strip()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Para registrarse debe ingresar su correo electrónico")
        return email.strip()

    def clean_repetir_password(self):
        password = self.cleaned_data.get("password")
        repetir_password = self.cleaned_data.get("repetir_password")
        if not repetir_password:
            raise forms.ValidationError("Debe volver a ingresar la misma contraseña")
        if repetir_password != password:
            raise forms.ValidationError("Las dos contraseña ingresadas deben coincidir")
        return repetir_password.strip()
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'fono',
            'direccion',
            'descripcionPerfil',
            'fotoPerfil',
            'cantidadProductos',
            #'tipo_Usuario  ',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'fono': 'Teléfono',
            'direccion': 'Dirección',
            'descripcionPerfil': 'Descripcion de perfil',
            'fotoPerfil': 'Foto de perfil',
            'cantidadProductos': 'Cantidad de productos',
            #'tipo_Usuario': 'Tipo de usuario',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'fono': forms. TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcionPerfil': forms.TextInput(attrs={'class': 'form-control'}),
        }