from django.http.response import HttpResponseBase, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Estado, Producto, Rol, Tienda, Usuario, Venta





import json


# Create your views here.
# Se crean vistas basadas en clases

class ViewUsuario(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            usuarios = list(Usuario.objects.filter(id_usuarios=id).values())
            if len(usuarios) > 0:
                usu = usuarios[0]
                datos = {'mensaje': " Exitoso", 'Usuarios': usu}
            else:
                datos = {'mensaje': "No se encontro el usuario"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'mensaje': " Exitoso", 'Usuarios': usuarios}
            else:
                datos = {'mensaje': "No se encontraron usuarios"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):
        print(request.body)
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuarios=id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id_usuarios=id)
            usuario.nombre = jd['nombre']
            usuario.apellido = jd['apellido']
            usuario.edad = jd['edad']
            usuario.genero = jd['genero']
            usuario.correo = jd['correo']
            usuario.telefono = jd['telefono']
            usuario.fecha_registro = jd['fecha_registro']
            usuario.tipo = jd['tipo']
            usuario.direccion = jd['direccion']
            usuario.password = jd['password']
            usuario.id_estado_id = jd['id_estado_id']
            usuario.id_rol_id = jd['id_rol_id']
            usuario.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el usuario"}
        return JsonResponse(datos)

    def delete(self, request):
        usuario = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuario) > 0:
            Usuario.objects.filter(id_usuario=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el usuario"}
        return JsonResponse(datos)


class ViewEstado(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id > 0):
            estados = list(Estado.objects.filter(id_estado=id).values())
            if len(estados) > 0:
                es = estados[0]
                datos = {'mensaje': " Exitoso", 'Estados': es}
            else:
                datos = {'mensaje': "No se encontro el estado"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            estados = list(Estado.objects.values())
            if len(estados) > 0:
                datos = {'mensaje': " Exitoso", 'Estados': estados}
            else:
                datos = {'mensaje': "No se encontraron Estados"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):

        jd = json.dumps(request.body.decode('utf-8'))

        # Estado.objects.create(id = jd['id_estado'], estado = jd['estado'])
        # Estado.objects.create(estado=jd['estado'])
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        estados = list(Estado.objects.filter(id_estado=id).values())
        if len(estados) > 0:
            estado = Estado.objects.get(id_estado=id)
            estado.id_estado = jd['id_estado']
            estado.estado = jd['estado']
            estado.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el estado"}
        return JsonResponse(datos)

    def delete(self, request):
        estado = list(Estado.objects.filter(id_estado=id).values())
        if len(estado) > 0:
            Estado.objects.filter(id_estado=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el estado"}
        return JsonResponse(datos)


class ViewProducto(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            productos = list(Producto.objects.filter(id_producto=id).values())
            if len(productos) > 0:
                pro = productos[0]
                datos = {'mensaje': " Exitoso", 'Productos': pro}
            else:
                datos = {'mensaje': "No se encontro el producto"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            productos = list(Producto.objects.values())
            if len(productos) > 0:
                datos = {'mensaje': " Exitoso", 'Productos': productos}
            else:
                datos = {'mensaje': "No se encontraron productos"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        productos = list(Producto.objects.filter(id_producto=id).values())
        if len(productos) > 0:
            producto = Producto.objects.get(id_producto=id)
            producto.nombre = jd['nombre']
            producto.precio = jd['precio']
            producto.seccion = jd['seccion']
            producto.id_tienda_id = jd['id_tienda_id']
            producto.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el producto"}
        return JsonResponse(datos)

    def delete(self, request):
        producto = list(Producto.objects.filter(id_producto=id).values())
        if len(producto) > 0:
            Producto.objects.filter(id_producto=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el producto"}
        return JsonResponse(datos)


class ViewRol(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id > 0):
            roles = list(Rol.objects.filter(id_rol=id).values())
            if len(roles) > 0:
                rol = roles[0]
                datos = {'mensaje': " Exitoso", 'Roles': rol}
            else:
                datos = {'mensaje': "No se encontro el rol"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            roles = list(Rol.objects.values())
            if len(roles) > 0:
                datos = {'mensaje': " Exitoso", 'Roles': roles}
            else:
                datos = {'mensaje': "No se encontraron roles"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        roles = list(Rol.objects.filter(id_rol=id).values())
        if len(roles) > 0:
            rol = Rol.objects.get(id_rol=id)
            rol.rol_usuario = jd['rol_usuario']
            rol.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el rol"}
        return JsonResponse(datos)

    def delete(self, request):
        rol = list(Rol.objects.filter(id_rol=id).values())
        if len(rol) > 0:
            Rol.objects.filter(id_rol=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro el rol"}
        return JsonResponse(datos)


class ViewTienda(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            tiendas = list(Tienda.objects.filter(id_tienda=id).values())
            if len(tiendas) > 0:
                tie = tiendas[0]
                datos = {'mensaje': " Exitoso", 'Tiendas': tie}
            else:
                datos = {'mensaje': "No se encontro la tienda"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            tiendas = list(Tienda.objects.values())
            if len(tiendas) > 0:
                datos = {'mensaje': " Exitoso", 'Tienda': tiendas}
            else:
                datos = {'mensaje': "No se encontraron tiendas"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        tiendas = list(Tienda.objects.filter(id_tienda=id).values())
        if len(tiendas) > 0:
            tienda = Tienda.objects.get(id_tienda=id)
            tienda.nombre = jd['nombre']
            tienda.direccion = jd['direccion']
            tienda.correo = jd['correo']
            tienda.telefono = jd['telefono']
            tienda.responsable = jd['responsable']
            tienda.password = jd['password']
            tienda.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro la tienda"}
        return JsonResponse(datos)

    def delete(self, request):
        tienda = list(Tienda.objects.filter(id_tienda=id).values())
        if len(tienda) > 0:
            Tienda.objects.filter(id_tienda=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro la tienda"}
        return JsonResponse(datos)


class ViewVenta(View):

    # Metodo que se ejecuta cada que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            ventas = list(Venta.objects.filter(id_venta=id).values())
            if len(ventas) > 0:
                ven = ventas[0]
                datos = {'mensaje': " Exitoso", 'Ventas': ven}
            else:
                datos = {'mensaje': "No se encontro la venta"}
            return JsonResponse(datos)
        else:
            # Utilizamos el ORM
            # Lista todo
            ventas = list(Venta.objects.values())
            if len(ventas) > 0:
                datos = {'mensaje': " Exitoso", 'Ventas': ventas}
            else:
                datos = {'mensaje': "No se encontraron ventas"}
            # retornamos un json
            return JsonResponse(datos)

    def post(self, request):
        datos = {'mensaje': " Exitoso"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        ventas = list(Venta.objects.filter(id_venta=id).values())
        if len(ventas) > 0:
            venta = Venta.objects.get(id_venta=id)
            venta.cantidad = jd['cantidad']
            venta.precio = jd['precio']
            venta.id_producto_id = jd['id_producto_id']
            venta.id_usuario_id = jd['id_usuario_id']
            venta.save()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro la venta"}
        return JsonResponse(datos)

    def delete(self, request, id):
        venta = list(Venta.objects.filter(id_venta=id).values())
        if len(venta) > 0:
            Venta.objects.filter(id_venta=id).delete()
            datos = {'mensaje': " Exitoso"}
        else:
            datos = {'mensaje': "No se encontro la venta"}
        return JsonResponse(datos)