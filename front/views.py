from django.shortcuts import render
from back.models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')

def discografia(request):
    buscado=Disco.objects.get(id=id)
    datos={'disco': buscado}
    return render(request, 'discografía.html', datos)

def productos(request):
    producto = Producto.objects.filter(categoria_id=1)
    datos = {'producto':producto}
    return render(request,'productos.html',datos)   

def usuarios(request):
    return render(request,'usuarios.html')

def perfil(request):
    return render(request,'perfil.html')
    

