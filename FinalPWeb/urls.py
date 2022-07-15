"""FinalPWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from back.views import perfil
from front.views import *
from back.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    path('home', home),

    path('',home),

    path('sesion',sesion),

    path('usuarios',usuarios),

    path('discografia',discografia),

    path('productos',productos),

    path('perfil',perfil),

      #Cierra sesion
    path('cerrar_sesion', cerrar_sesion),

    
    #valida el usuario url funcion
    path('validarusuario',validarusuario),


    path('registrarUsuario',registrarUsuario),

    #Administracion de productos
    path('admin_productos', admin_productos),

    #Editar un producto
    path('admin_edit', admin_edit),

    path('guardarProducto',guardarProducto),

    path('modificarProducto/<p_id>', buscarProducto),

    #eliminar producto
    path('eliminarProducto/<p_id>', eliminarProducto),

    #eliminar producto
    path('guardarProductoModificado/', guardarProductoModificado),


]


