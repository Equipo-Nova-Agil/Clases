
from Persona import Persona
from Producto import Producto
from Carro import Carro

class Tienda:


    def __init__(self, nombre, caja = 0, nomina = []):
        self.nombre = nombre
        self.inventario = Carro([], [])
        #self.facturas = facturas
        self.caja = caja
        self.nomina = nomina

#########################################################################
# Getters y Setters
#########################################################################

    def getInventario(self):
        return self.inventario

    def setInventario(self, n):
        self.inventario = n

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

    def agregarInventario(self, pn, q =1):
        if isinstance(pn, Producto) or isinstance(pn, list):
            # usamos c para guardar el carro
            inventario = self.getInventario()
            # llamamos el método agregando la cantidad y producto ingresados
            inventario.agregarProducto(pn, q)
            # Actualizamos el carro
            self.setInventario(inventario)


    def removerInventario(self, pn, q =1):
        if isinstance(pn, Producto) or isinstance(pn, list):
            # usamos c para guardar el carro
            inventario = self.getInventario()
            # llamamos el método agregando la cantidad y producto ingresados
            inventario.removerProducto(pn, q)
            # Actualizamos el carro
            self.setInventario(inventario)


    def calcularCostoInventario(self):
        c = self.getInventario()
        c.costoTotal()


    def consultarExistencia(self, carro):
        if isinstance(carro, Carro):
            L = carro.getLproductos()
            C = carro.getCantidades()
            Len = len(L)
            LI = self.getInventario().getLproductos()
            CI = self.getInventario().getCantidades()
            LenI = len(LI)
            existe = []
            if Len > 0:
                for i in range(0, Len):
                    for j in range(0, LenI):
                        if (L[i].getID() == LI[j].getID()):
                            if (CI[j] >= C[i]):
                                existe.append(True)
                                print()




            else:
                print('El carro se encuentra vacío')
        else:
            print('El elemento ingresado no es valido')


    def vender(self, carro):
        if isinstance(carro, Carro):
            L = carro.getLproductos()
            C = carro.getCantidades()
            Len = len(L)
            if Len > 0:

            else:
                print('El carro se encuentra vacío')

        else:
            print('El elemento ingresado no es valido')