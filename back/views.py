from django.shortcuts import render
from .models import Usuario, Categoria,Disco
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ProductoForm, DiscoForm
from .models import Producto
# Create your views here.
def sesion(request):
    return render(request,'iniciarSesion.html')

#---Registrar bdb->
def registrarUsuario(request):
    #obtiene datos desde el formulario en registro
    r_correo= request.POST.get('registroEmail')
    r_nombre= request.POST.get('registroNombre')
    r_pass1=request.POST.get('registroContraseña')
#Registra al usuario en la BBDD
    nuevo_usuario=Usuario()
    nuevo_usuario.email=r_correo
    nuevo_usuario.nombre=r_nombre
    nuevo_usuario.contraseña=r_pass1
    Usuario.save(nuevo_usuario)
    return redirect('/sesion')

def admin_productos(request):
    form = ProductoForm()
    producto = Producto.objects.all()
    datos={'producto':producto,'form':form}

    return render(request,'admin_productos.html',datos)

def admin_discografía(request):
    form = DiscoForm()
    disco = Disco.objects.all()
    datos={'disco':disco,'form':form}

    return render(request,'admin_discografía.html',datos)


def register(request):
    r_correo= request.POST.get('registroEmail')
    r_nombre= request.POST.get('registroNombre')
    r_apellido= request.POST.get('registroApellido')
    r_pass1=request.POST.get('passwordRegistro1')
    if len(r_correo)>0 and len(r_nombre)>0 and len(r_pass1)>0 and len(r_apellido):
        r_User = Usuario(email=r_correo,nombre=r_nombre,contraseña=r_pass1,apellidos=r_apellido)
        r_User.save()
        messages.success(request, 'La cuenta ha sido creada!')
        return HttpResponseRedirect('sesion')
    else:
        messages.error(request, 'La cuenta ya existe o hubo un error al ingresar los datos.')
        return HttpResponseRedirect('usuarios')

def validarusuario(request):
    v_correo = request.POST.get('loginEmail')
    v_pass = request.POST.get('loginPassword')
    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_correo,contraseña=v_pass)
        
        if usu:
            request.session['usuario'] = v_correo
            return redirect('/home')

    except:
        return redirect('/sesion')

#Esta funcion evita entrar a perfil directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/sesion')
    else:
        return render(request, 'perfil.html')

        #funcion cerrar sesion
def cerrar_sesion(request):
    if 'usuario' in request.session:
        logout(request)
        return redirect('/sesion')
    else:
        return redirect('/home')

#CRUD DE PRODUCTOS

def admin_edit(request):
    form = ProductoForm()
    producto = Producto.objects.all()
    datos={'producto':producto,'form':form}

    return render(request, 'admin_edit.html', datos)

def guardarProducto(request):
    #pasando la data a las variables
    v_categoria=request.POST.get('categoria')
    v_nombre_producto=request.POST.get('nombre_producto')
    v_precio_producto=request.POST.get('precio_producto')
    v_stock_producto=request.POST.get('stock_producto')
    v_descripcion_producto=request.POST.get('descripcion_producto')
    v_imagen=request.POST.get('imagen')
    
    nuevo=Producto()
    nuevo.categoria= Categoria.objects.get(id = request.POST['categoria'])
    nuevo.nombre_producto=v_nombre_producto
    nuevo.precio_producto=v_precio_producto
    nuevo.stock_producto=v_stock_producto
    nuevo.descripcion_producto=v_descripcion_producto
    nuevo.imagen= v_imagen

    #guarda la data del objeto
    Producto.save(nuevo)

    return redirect('/admin_productos')


#Buscar producto
def buscarProducto(request, p_id):
    buscado=Producto.objects.get(id=p_id)
    datos={'producto': buscado}
    return render(request, 'admin_edit.html', datos)


#modificar productos
def guardarProductoModificado(request):
    v_id=request.POST.get('id')
    v_categoria=request.POST.get('categoria')
    v_nombre_producto=request.POST.get('nombre_producto')
    v_precio_producto=request.POST.get('precio_producto')
    v_stock_producto=request.POST.get('stock_producto')
    v_descripcion_producto=request.POST.get('descripcion_producto')
    v_imagen=request.POST.get('imagen')
    
    buscado=Producto.objects.get(id=v_id)

    if(buscado):
        buscado.categoria_id=v_categoria
        buscado.nombre_producto=v_nombre_producto
        buscado.precio_producto=v_precio_producto
        buscado.descripcion_producto=v_descripcion_producto
        buscado.nombre_producto=v_nombre_producto
        buscado.imagen=v_imagen
        buscado.stock_producto=v_stock_producto

        Producto.save(buscado)
        return redirect('/admin_productos')


#eliminar productos
def eliminarProducto(request, p_id):
    buscado=Producto.objects.get(id=p_id)
    if(buscado):
        Producto.delete(buscado)
        return redirect('/admin_productos')


def guardarDisco(request):
    #pasando la data a las variables
    v_nombre_disco=request.POST.get('nombre')
    v_año_disco=request.POST.get('año')
    v_descripcion_disco=request.POST.get('descripcion')
    v_canciones=request.POST.get('canciones')
    v_portada=request.POST.get('portada')
    
    nuevo=Disco()
    nuevo.nombre= v_nombre_disco
    nuevo.año=v_año_disco
    nuevo.descripcion=v_descripcion_disco
    nuevo.canciones=v_canciones
    nuevo.portada=v_portada

    #guarda la data del objeto
    Disco.save(nuevo)

    return redirect('/admin_discografía')

def eliminarDisco(request, p_id):
    buscado=Disco.objects.get(id=p_id)
    if(buscado):
        Disco.delete(buscado)
        return redirect('/admin_discografía')


def buscarDisco(request, p_id):
    buscado=Disco.objects.get(id=p_id)
    datos={'disco': buscado}
    return render(request, 'admin_editdisco.html', datos)

def guardarDiscoModificado(request):
    v_id=request.POST.get('id')
    v_nombre_disco=request.POST.get('nombre')
    v_año_disco=request.POST.get('año')
    v_descripcion_disco=request.POST.get('descripcion')
    v_canciones=request.POST.get('canciones')
    v_portada=request.POST.get('portada')
    
    buscado=Disco.objects.get(id=v_id)

    if(buscado):
        buscado.id=v_id
        buscado.nombre=v_nombre_disco
        buscado.año=v_año_disco
        buscado.descripcion=v_descripcion_disco
        buscado.canciones=v_canciones
        buscado.portada=v_portada


        Disco.save(buscado)
        return redirect('/admin_discografía')
