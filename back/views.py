from django.shortcuts import render
from .models import Usuario, Categoria
from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def sesion(request):
    return render(request,'iniciarSesion.html')

#---Registrar bdb->
def registrarUsuario(request):
    #obtiene datos desde el formulario en registro
    r_correo = request.POST.get('registroEmail')
    r_nombre = request.POST.get('registroNombre')
    r_apellido = request.POST.get('registroApellido')
    r_pass1=request.POST.get('passwordRegistro1')
#Registra al usuario en la BBDD
    nuevo_usuario=Usuario()
    nuevo_usuario.email=r_correo
    nuevo_usuario.nombre=r_nombre
    nuevo_usuario.contraseña=r_pass1
    Usuario.save(nuevo_usuario)

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