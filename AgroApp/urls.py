from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # agregar una producto  
    path('agregar_producto', views.agregar_producto, name="agregar_producto"),
    path('', views.lista_productos, name="inicio"),
    path('editar_producto/<int:producto_id>', views.editar_producto ,name="editar_producto"),
    path('mis_productos', views.listar_productos_usuario ,name="mis_productos"),
    path('borrar_producto/<int:producto_id>', views.borrar_producto, name="borrar_producto"),
    path('vista_producto/<int:producto_id>', views.vista_producto, name="vista_producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)