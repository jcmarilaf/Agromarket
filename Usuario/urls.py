from django.urls import path, include
from django.conf.urls import url
from .views import  UserList, SuccessLogin
from django.contrib.auth.views import login_required
from django.contrib.auth import views as auth_views
from .views import Registro, UserList


urlpatterns = [

    path('verPerfil', UserList.as_view(), name="verPerfil"),
    path('registro', Registro, name="registro"),



]

