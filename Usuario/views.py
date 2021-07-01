from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.api import error, success
from django.shortcuts import get_object_or_404, redirect, render
from .forms import  RegistroForm, UserUpdateForm
from .models import Usuario


def registrar_usuarios(request):
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Registrado correctamente')
            return redirect("login")
        else:
            messages.error(request,'No se pudo registrar el usuario.')
            return redirect("registrar")
    else:
        form = RegistroForm()
        return render(request, "Usuario/registrar.html", {'form': form})

@login_required
def Usuario_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , request.FILES, instance= request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'¡Su perfil ha sido actualizado!',success)
            return redirect('perfil')
        else:
            messages.error(request, "Error, No se pudo realizar el cambio",error)
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance = request.user)
        
    context = {
        'u_from': u_form
    }
    return render(request,'Usuario/perfil.html', context)

def perfil_vendedor(request,username_id):
    data =  get_object_or_404(Usuario, username=username_id)
    return render(request,"Usuario/perfil_vendedor.html",{'data': data})