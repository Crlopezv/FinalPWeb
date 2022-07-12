import email
from mailbox import NoSuchMailboxError
from xml.sax.handler import property_declaration_handler
from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(max_length=150)
    nombre = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

    def str(self):
        return self.nombre

class Categoria(models.Model):
    nombre= models.CharField(max_length=20)

    def str(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=True, null=False)
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField(default='1')
    descripcion_producto = models.CharField(max_length=100)
    imagen = models.CharField(max_length=50, default= 'Sin_imagen')

    def str(self):
        return self.nombre_producto

class Disco(models.Model):
    nombre=models.CharField(max_length=50)
    año=models.CharField(max_length=4)
    descripcion=models.CharField(max_length=300)
    canciones=models.CharField(max_length=2)
    portada=models.CharField(max_length=50, default= 'Sin_imagen')

    def str(self):
        return self.nombre


