from django.contrib.messages.api import error
from django.http import response, JsonResponse
from Usuario.models import Usuario
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from .forms import ComunidadForm, ProductosForm
from .models import Comunidad, ListaDeseos, Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def agregar_producto(request):
    if request.method == "POST":
        form = ProductosForm(request.POST, request.FILES, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto agregado correctamente')
            return redirect("inicio")
        else:
            messages.error(request,'No se pudo agregar el producto.')
            return redirect("agregar_producto")
    else:
        form = ProductosForm()
        return render(request, "Producto/agregar_productos.html", {'form': form})

def vista_producto(request,producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request,"Producto/producto.html",{'producto': producto})

def lista_productos(request):
    producto = Producto.objects.all()
    return render(request, "inicio.html", {'producto': producto})

def editar_producto(request,producto_id):
    # Recuperamos la instancia del producto
    producto = get_object_or_404(Producto, id=producto_id)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formulario = ProductosForm(request.POST, instance=producto, files=request.FILES)
        # Si el formulario es válido...
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'¡Producto editado correctamente!')
            return redirect('mis_productos')
        else:
            messages.error(request, "Error, No se pudo editar su Producto")
    else:
        formulario = ProductosForm(instance=producto)
    data = {
        'formulario':formulario
    }

    # Si llegamos al final renderizamos el formulario
    return render(request, "Producto/editar_producto.html",  data)

def listar_productos_usuario(request):
    productos = Producto.objects.all().filter(usuario=request.user)
    return render(request, "Producto/mis_productos.html", {'productos': productos})

def borrar_producto(request, producto_id):
    # Recuperamos la instancia de el producto y la borramos
    instancia = get_object_or_404(Producto, id=producto_id)
    messages.warning(request,"¿Seguro desea  eliminar el producto?" )
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('mis_productos')

def lista_deseos(request):
    lista = ListaDeseos.objects.all().filter(usuario=request.user)
    return render(request, "lista_deseos.html", {'lista': lista})

def borrar_deseo(request,deseo_id):
    instancia = get_object_or_404(ListaDeseos,id=deseo_id)
    instancia.delete()
    return redirect('lista_deseos')
    
class AgregarDeseo(CreateView):
    model = ListaDeseos
    success_url = reverse_lazy('lista_deseos')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            producto = Producto.objects.filter(id = request.POST.get('producto')).first()
            usuario = request.user
            if producto and usuario:
                agregar_deseo = self.model(
                    producto = producto,
                    usuario = usuario
                )
                agregar_deseo.save()
                mensaje = f'{self.model.__name__} registrado correctamente!.'
                error = 'No hay error!.'
                response = JsonResponse({'mensaje':mensaje, 'error':error, 'url':self.success_url})
                response.status_code = 201
                return response
        return redirect('lista_deseos')

def agregar_comunidad(request):
    if request.method == "POST":
        form = ComunidadForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Comunidad agregada correctamente')
            return redirect("inicio")
        else:
            messages.error(request,'No se pudo agregar la Comunidad.')
            return redirect("agregar_comunidad")
    else:
        form = ComunidadForm()
        return render(request, "Comunidad/agregar_comunidad.html", {'form': form})

def lista_comunidades(request):
    lista = Comunidad.objects.all()
    return render(request, "Comunidad/listar_comunidades.html", {'lista': lista})


def borrar_comunidad(request,comunidad_id):
    instancia = get_object_or_404(Comunidad,id=comunidad_id)
    instancia.delete()
    return redirect('lista_comunidades')

def editar_comunidad(request,comunidad_id):
    # Recuperamos la instancia del producto
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formulario = ComunidadForm(request.POST, instance=comunidad)
        # Si el formulario es válido...
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Comunidad editada correctamente!')
            return redirect('lista_comunidades')
        else:
            messages.error(request, "Error, No se pudo editar su comunidad")
    else:
        formulario = ComunidadForm(instance=comunidad)
    data = {
        'formulario':formulario,
        'comunidad':comunidad
    }

    # Si llegamos al final renderizamos el formulario
    return render(request, "Comunidad/editar_comunidad.html",  data)