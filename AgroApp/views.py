from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductosForm
from .models import Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def agregar_producto(request):
    if request.method == "POST":
        form = ProductosForm(request.POST, request.FILES, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto agregado correctamente', 'success')
            return redirect("inicio")
        else:
            messages.error(request,'No se pudo agregar el producto.','error')
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
    instancia = Producto.objects.get(id=producto_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('mis_productos')