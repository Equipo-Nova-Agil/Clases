from django.shortcuts import render


#from Persona import Persona
#from Producto import Producto
#from Carro import Carro
#from Tienda import Tienda

from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets
import json
from .models import modeloUsuario, modeloRol, modeloVenta, modeloTienda, modeloEstado, modeloProducto
from .serializers import usuarioSerializers, rolSerializer, estadoSerializer, tiendaSerializer, productoSerializer, ventasSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#@method_decorator(csrf_exempt, name='dispatch')


class viewUsuario(View):

    def post(self, request):

        data = json.loads(request.body.decode('utf-8'))

        id = data.get('id_usuarios')
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        edad  = data.get('edad')
        genero = data.get('genero')
        correo = data.get('correo')
        telefono = data.get('telefono')
        fecha_registro = data.get('fecha_registro')
        tipo = data.get('tipo')
        direccion = data.get('direccion')
        password = data.get('password')
        id_rol = data.get('id_rol')
        id_estado = data.get('id_estado')

        datos_usuario = {
            'id_usuarios': id,
            'nombre': nombre,
            'apellido': apellido,
            'edad' : edad,
            'genero' : genero,
            'correo' : correo,
            'telefono' : telefono,
            'fecha_registro' : fecha_registro,
            'tipo' : tipo,
            'direccion' : direccion,
            'passrowd' : password,
            'id_rol' : id_rol,
            'id_estado' : id_estado,
        }

        user = M.modeloUsuario.objects.create(**datos_usuario)

        data = {
            "message": f"{user.nombre} {user.apellido} ha sido agregado como nuevo usuario"
        }
        return JsonResponse(data, status=201)







# Viewsets


class usuarioViewSet(viewsets.ModelViewSet):
   queryset = modeloUsuario.objects.all()
   serializer_class = usuarioSerializers


class rolViewSet(viewsets.ModelViewSet):
   queryset = modeloRol.objects.all()
   serializer_class = rolSerializer


class estadoViewSet(viewsets.ModelViewSet):
   queryset = modeloEstado.objects.all()
   serializer_class = estadoSerializer

class productoViewSet(viewsets.ModelViewSet):
   queryset = modeloProducto.objects.all()
   serializer_class = productoSerializer

class tiendaViewSet(viewsets.ModelViewSet):
   queryset = modeloTienda.objects.all()
   serializer_class = tiendaSerializer

class ventasViewSet(viewsets.ModelViewSet):
   queryset = modeloVenta.objects.all()
   serializer_class = ventasSerializer


