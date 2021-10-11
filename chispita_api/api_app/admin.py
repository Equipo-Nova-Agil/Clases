from django.contrib import admin

from .models import modeloProducto
from .models import modeloUsuario
from .models import modeloRol
from .models import modeloTienda
from .models import modeloEstado
from .models import modeloVenta

# Register your models here.
admin.site.register(modeloProducto)
admin.site.register(modeloUsuario)
admin.site.register(modeloRol)
admin.site.register(modeloTienda)
admin.site.register(modeloEstado)
admin.site.register(modeloVenta)






