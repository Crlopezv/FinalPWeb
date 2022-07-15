from django.shortcuts import render
from back.models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')

def discografia(request):
    return render(request,'discografia.html')

def productos(request):
    producto = Producto.objects.filter(categoria_id=1)
    datos = {'producto':producto}
    return render(request,'productos.html',datos)

def usuarios(request):
    return render(request,'usuarios.html')

def perfil(request):
    return render(request,'perfil.html')
    

