from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # agregar una producto  
    path('agregar_producto', views.agregar_producto, name="agregar_producto"),
    path('', views.lista_productos, name="inicio"),
    path('editar_producto/<int:producto_id>', views.editar_producto ,name="editar_producto"),
    path('mis_productos', views.listar_productos_usuario ,name="mis_productos"),
    path('borrar_producto/<int:producto_id>', views.borrar_producto, name="borrar_producto"),
    path('vista_producto/<int:producto_id>', views.vista_producto, name="vista_producto"),
    path('lista_deseos', views.lista_deseos, name="lista_deseos"),
    path('agregarDeseo', AgregarDeseo.as_view(), name="agregarDeseo"),
    path('borrar_deseo/<int:deseo_id>', views.borrar_deseo, name="borrar_deseo"),
    path('agregar_comunidad', views.agregar_comunidad, name="agregar_comunidad"),
    path('lista_comunidades', views.lista_comunidades, name="lista_comunidades"),
    path('borrar_comunidad/<int:comunidad_id>', views.borrar_comunidad, name="borrar_comunidad"),
    path('editar_comunidad/<int:comunidad_id>', views.editar_comunidad ,name="editar_comunidad"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)