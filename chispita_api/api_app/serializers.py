from rest_framework import serializers

from .models import modeloUsuario, modeloRol, modeloVenta, modeloEstado, modeloTienda, modeloProducto


class usuarioSerializers(serializers.ModelSerializer):
   class Meta:
       model = modeloUsuario
       fields = ('id_usuarios', 'nombre', 'apellido', 'edad',
                 'genero', 'correo', 'telefono', 'fecha_registro',
                 'tipo', 'direccion', 'password', 'id_rol', 'id_estado')


class rolSerializer(serializers.ModelSerializer):
   class Meta:
       model = modeloRol
       fields = ('id_rol', 'rol_usuario')


class estadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloEstado
        fields = ('id_estado', 'estado')


class tiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloTienda
        fields = ('id_tienda', 'nombre', 'direccion', 'correo',
                  'telefono', 'responsable', 'password')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloProducto
        fields = ('id_producto', 'id_tienda', 'nombre', 'precio',
                  'seccion')


class ventasSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloProducto
        fields = ('id_venta', 'id_usuario', 'id_producto', 'cantidad', 'precio')



