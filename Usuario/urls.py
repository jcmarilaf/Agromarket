from django.urls import path, include
from . import views
from .views import  registrar_usuarios, Usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('perfil', views.Usuario , name='perfil'),
    path('registrar',  views.registrar_usuarios, name='registrar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)