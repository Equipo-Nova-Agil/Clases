# django-admin startproject chispita_api
# cd chispita_api
# python manage.py startapp api_app
# python manage.py makemigrations
# python manage.py migrate

from django.contrib import admin
from django.db import models as md

class modeloEstado(md.Model):
    id_estado = md.IntegerField(serialize=True, primary_key=True)
    estado = md.CharField(max_length=30)

class modeloRol(md.Model):
    id_rol = md.IntegerField(serialize=True, primary_key=True)
    rol_usuario = md.CharField(max_length=20)


class modeloUsuario(md.Model):
    id_usuarios = md.IntegerField(serialize=True, primary_key=True)
    nombre = md.CharField(max_length=45)
    apellido = md.CharField(max_length=45)
    edad = md.IntegerField(null=True)
    genero = md.CharField(max_length=1)
    correo = md.CharField(max_length=100, unique=True)
    telefono = md.CharField(max_length=20)
    fecha_registro = md.DateField()
    tipo = md.CharField(max_length=45)
    direccion = md.CharField(max_length=100)
    password = md.CharField(max_length=45)
    id_rol = md.OneToOneField(modeloRol,
                              on_delete= md.CASCADE)
    id_estado = md.OneToOneField(modeloEstado,
                                 on_delete= md.CASCADE)

class modeloTienda(md.Model):
    id_tienda = md.IntegerField(serialize=True, primary_key=True)
    nombre = md.CharField(max_length=45, unique=True)
    direccion = md.CharField(max_length=100)
    correo = md.CharField(max_length=100, unique=True)
    telefono = md.CharField(max_length=20)
    responsable = md.CharField(max_length=45)
    password = md.CharField(max_length=45)


class modeloProducto(md.Model):
    id_producto = md.IntegerField(serialize=True, primary_key=True)
    id_tienda = md.ForeignKey(modeloTienda, on_delete=md.CASCADE)
    nombre = md.CharField(max_length=45)
    precio = md.FloatField()
    seccion = md.CharField(max_length=45)


class modeloVenta(md.Model):
    id_venta = md.IntegerField(serialize=True, primary_key=True)
    id_usuario = md.ForeignKey(modeloUsuario, on_delete=md.CASCADE)
    id_producto = md.ForeignKey(modeloProducto, on_delete=md.CASCADE)
    cantidad = md.IntegerField()
    precio = md.FloatField()


