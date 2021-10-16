from django.urls import path, include
from rest_framework import routers
from .views import viewUsuario, usuarioViewSet, rolViewSet, estadoViewSet, tiendaViewSet, productoViewSet, ventasViewSet

router = routers.DefaultRouter()
router.register(r'modeloUsuario', usuarioViewSet)
router.register(r'modeloRol', rolViewSet)
router.register(r'modeloEstado', estadoViewSet)
router.register(r'modeloTienda', tiendaViewSet)
router.register(r'modeloProducto', productoViewSet)
router.register(r'modeloVenta', ventasViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


