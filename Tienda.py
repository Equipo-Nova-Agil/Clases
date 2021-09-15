
import Persona
import Producto
import Carro

class Tienda:


    def __init__(self, inventario = Carro(), facturas = [], caja = 0, nomina = []):
        self.inventario = inventario
        self.facturas = facturas
        self.caja = caja
        self.nomina = nomina

#########################################################################
# Getters y Setters
#########################################################################

    def getInventario(self):
        return self.inventario

    def setInventario(self, n):
        self.inventario = n

    def getFacturas(self):
        return self.facturas

    def setFacturas(self, n):
        self.facturas = n

    def getCaja(self):
        return self.caja

    def setCaja(self, n):
        self.caja = n

    def getNomina(self):
        return self.nomina

    def setNomina(self, n):
        self.nomina = n

#########################################################################
# Métodos
#########################################################################

    def agregarInventario(self, producto, cantidad = [1]):
        self.inventario.agregarProducto(producto, cantidad)


    def removerInventario(self, producto, cantidad = [1]):
        self.inventario.removerProducto(producto, cantidad)


