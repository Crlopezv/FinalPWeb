from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def discografia(request):
    return render(request,'discografia.html')

def productos(request):
    return render(request,'productos.html')

def usuarios(request):
    return render(request,'usuarios.html')

def perfil(request):
    return render(request,'perfil.html')


