# django-admin startproject chispita_api
# cd chispita_api
# python manage.py startapp api_app
# python manage.py makemigrations
# python manage.py migrate

from django.contrib import admin
from django.db import models as md

class modeloPersona(models.Model):
    first_name = md.CharField(max_length=30)
    last_name = md.CharField(max_length=30)

    self.nombre = nombre
    self.genero = genero
    self.correo = correo
    self.tipoUsuario = tipoUsuario
    self.edad = edad
    self.telefono = telefono
    self.direccion = direccion
    self.ID = ID
    self.carro = Carro([], [])

class modeloProducto(md.Model):

    self.nombre = nombre
    self.precio = precio
    self.seccion = seccion
    self.ID = ID
    self.ID_tienda = ID_tienda

class modeloTienda(md.Model):
    self.nombre = nombre
    self.direccion = direccion
    self.telefono = telefono
    self.correo = correo
    self.responsable = responsable
    self.inventario = Carro([], [])
    self.caja = caja
    self.nomina = nomina

class modeloVenta(md.Model):

# de muchos a uno se usa md.ForeingKey

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

# de muchos a muchos

class Topping(models.Model):
    # ...
    pass
class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

# ejemplo manytomany con varias tablas
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# Relaciones uno a uno OnetoOneField
