
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


    def verInventario(self):
        inventario = self.getInventario()
        inventario.verProducto()


    def calcularCostoInventario(self):
        c = self.getInventario()
        c.costoTotal()


    def consultarExistencia(self, carro):
        if isinstance(carro, Carro):
            L = carro.getLproductos()
            Len = len(L)
            LI = self.getInventario().getLproductos()
            LenI = len(LI)
            existe = []
            pos = []
            if Len > 0:
                for i in range(0, Len):
                    it = 0
                    for j in range(0, LenI):
                        if (L[i].getID() != LI[j].getID()):
                            it += 1
                        else:
                            existe.append(True)
                            pos.append(j)
                            break
                    if it == LenI:
                        existe.append(False)
                        pos.append(-1)
                return existe, pos
            else:
                print('El carro se encuentra vacío')
        else:
            print('El elemento ingresado no es valido')



    def consultarCantidad(self, carro):
        if isinstance(carro, Carro):
            L = carro.getLproductos()
            C = carro.getCantidades()
            CI = self.getInventario().getCantidades()
            C_disponible = []
            pos = []
            Len = len(L)
            if Len > 0:
                existe = self.consultarExistencia(carro)
                for i in range(0, Len):
                    if existe[0][i] == True:
                        if C[i] > CI[existe[1][i]]:
                            C_disponible.append(CI[existe[1][i]])
                            pos.append(i)
                Len_Cd = len(pos)
                if Len_Cd > 0:
                    print('Los siguientes productos no cuentan con las cantidades solicitadas en inventario\n')
                    print('Producto', '\t', 'Cant_solicitada', '\t', 'Cant_disponible')
                    for i in range(0, Len_Cd):
                        print(L[pos[i]].getNombre(), '\t', '\t', C[pos[i]], '\t', '\t', C_disponible[i])
                    print()
                    reemplazar = input('¿Desea reemplazar las cantidades indicadas? (Si o No): ')
                    if reemplazar == 'Si' or reemplazar == 'si' or reemplazar == 'SI':
                        for i in range(0, Len_Cd):
                            C[pos[i]] = C_disponible[i]
                        carro.setCantidades(C)
                        print('Se han actualizado correctamente las cantidades disponibles')
                else:
                    print('Todas las cantidades solicitadas se encuentran disponibles')
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
                print('Toy chiquito, vuelve más tarde')

            else:
                print('El carro se encuentra vacío')

        else:
            print('El elemento ingresado no es valido')

