#########################################################################
# La clase producto se crea para poder organizar y apilar cada producto
# con sus respectivos datos
#########################################################################

class Producto:

#########################################################################
# Atributos
#########################################################################

    def __init__(self, nombre, precio, seccion, ID, ID_tienda):
        self.nombre = nombre
        self.precio = precio
        self.seccion = seccion
        self.ID = ID
        self.ID_tienda = ID_tienda

#########################################################################
# Getters y Setters
#########################################################################

    def getNombre(self):
        return self.nombre

    def setNombre(self, n):
        self.nombre = n

    def getPrecio(self):
        return self.precio

    def setPrecio(self, n):
        self.precio = n

    def getSeccion(self):
        return self.seccion

    def setSeccion(self, n):
        self.seccion = n

    def getID(self):
        return self.ID

    def setID(self, n):
        self.ID = n


    def getIDTienda(self):
        return self.ID_tienda

    def setIDTienda(self, n):
        self.ID_tienda = n