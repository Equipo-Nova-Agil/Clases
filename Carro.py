from Producto import Producto


class Carro:

    def __init__(self, car_ID, Lproductos, Cantidad):
        self.car_ID = car_ID
        self.Lproductos = Lproductos
        self.cantidades = Cantidad

#########################################################################
# Getters y Setters
#########################################################################

    def getLproductos(self):
        return self.Lproductos

    def setLproductos(self, n):
        self.Lproductos = n

    def getCantidades(self):
        return self.cantidades

    def setCantidades(self, n):
        self.cantidades = n

#########################################################################
# Métodos
#########################################################################

    # agregarProducto() busca si el producto en cuestión
    # existe, si existe suma la cantidad indicada
    # si no existe se agrega al carro con su respectiva cantidad
    def agregarProducto(self, producto, cantidad=[1]):
        # si la cantidad ingresada es un entero se aloja en una lista
        if isinstance(cantidad, int):
            cantidad = [cantidad]
        # Guardamos la lista de productos en L con su método get
        # Guardamos la lista de cantidades en C con su método get
        L = self.getLproductos()
        C = self.getCantidades()
        # Len es la longitud de la lista de productos
        Len = len(L)
        # Los productos se pueden agregar uno a uno o en listas
        # Esta primera rama se sigue el caso cuando es un Producto
        if (isinstance(producto, Producto)):
            # Como el identificador debe ser único, guardamos este en IDnp
            IDnp = producto.getID()
            # creamos un iterador en 0
            it = 0
            # Si la lista no está vacia se busca en ella el producto
            # en caso contrario simplemente se agrega
            if (Len > 0):
                for i in range(0, Len, 1):
                    # cada que los ID sean diferentes se suma al iterador
                    if (IDnp != L[i].getID()):
                        it += 1
                    # en caso contrario se suma la cantidad y se actualiza a C
                    else:
                        C[i] = C[i] + cantidad[0]
                        print(f'Se ha sumado {cantidad[0]} a {producto.getNombre()}')
                        self.setCantidades(C)
                        break
                # Si el iterador llega a ser igual a Len se agregan y actualizan ambas listas
                if (it == Len):
                    L.append(producto)
                    C.append(cantidad[0])
                    self.setLproductos(L)
                    self.setCantidades(C)
                    print(f'Se ha agregado {cantidad[0]} {producto.getNombre()} al carro')
            # Cuando la lista esta vacía simplemente se agrega
            else:
                L.append(producto)
                C.append(cantidad[0])
                self.setLproductos(L)
                self.setCantidades(C)
                print(f'Se ha agregado {cantidad[0]} {producto.getNombre()} al carro')
        # En esta segunda rama se sigue el caso cuando es una lista de Productos
        else:
            if (isinstance(producto, list)):
                # cuando es una lista, lo primero se comparar si la distancia es la misma
                lenP = len(producto)
                lenC = len(cantidad)
                IDnp = ''
                # en caso de que no lo sea, haremos que la distancia de las cantidades sea
                # igual o mayor para que siempre esté dentro de los límites a iterar
                if (lenP != lenC):
                    cantidad = cantidad * lenP

                # primero para un i tan grande como la lista de productos a agregar
                for i in range(0, lenP, 1):
                    IDnp = producto[i].getID()
                    it = 0
                    # Si la lista de productos no está vacía
                    if (Len > 0):
                        # Se compara con cada producto en la lista y se sigue el mismo iterador
                        for j in range(0, Len, 1):
                            if (IDnp != L[j].getID()):
                                it += 1
                            # Si se encuentra el ID se suma la cantidad indicada
                            else:
                                C[j] = C[j] + cantidad[i]
                                print(f'Se han sumado {cantidad[i]} a  {producto[i].getNombre()}')
                                self.setCantidades(C)
                                break

                        # Si el iterador llega a ser igual a Len se agregan y actualizan ambas listas
                        if (it == Len):
                            L.append(producto[i])
                            C.append(cantidad[i])
                            self.setLproductos(L)
                            self.setCantidades(C)
                            print(f'Se ha agregado {cantidad[i]} {producto[i].getNombre()} al carro')

                    # Cuando la lista esta vacía simplemente se agrega
                    else:
                        L.append(producto[i])
                        C.append(cantidad[i])
                        self.setLproductos(L)
                        self.setCantidades(C)
                        print(f'Se ha agregado {cantidad[i]} {producto[i].getNombre()} al carro')

    # removerProducto busca y resta la cantidad indicada por el ID
    def removerProducto(self, producto, cantidad=1):

        # si la cantidad ingresada es un entero se aloja en una lista
        if (isinstance(cantidad, int)):
            cantidad = [cantidad]
        # Guardamos la lista de productos en L con su método get
        # Guardamos la lista de cantidades en C con su método get
        L = self.getLproductos()
        C = self.getCantidades()
        # Len es la longitud de la lista de productos
        Len = len(L)
        IDnp = 0
        # si la lista esta vacía no ejecuta la busqueda
        if (Len > 0):
            # Los productos se pueden remover uno a uno o en listas
            # Esta primera rama se sigue el caso cuando es un Producto
            if (isinstance(producto, Producto)):
                IDnp = producto.getID()
                # se compara el ID del nuevo producto con todos en la lista
                for i in range(0, Len, 1):
                    # cuando son iguales resta  la cantidad indicada
                    if (IDnp == L[i].getID()):
                        C[i] = C[i] - cantidad[0]
                        # si la cantidad llega a ser menor o igual a cero
                        # remueve el producto de la lista
                        if (C[i] <= 0):
                            L.pop(i)
                            C.pop(i)
                            self.setLproductos(L)
                            self.setCantidades(C)
                            print(f'Se ha removido {producto.getNombre()} del carro')
                            break
                        # en caso de ser mayor que cero simplemente se actualiza la cantidad
                        else:
                            self.setCantidades(C)
                            print(f'Se han restado {cantidad[0]} de {producto.getNombre()}')
                            break

            else:
                # El caso cuando se agrega una lista de Productos
                if (isinstance(producto, list)):
                    # primero se compara la longitud de ambas listas
                    lenP = len(producto)
                    lenC = len(cantidad)
                    IDnp = 0

                    # en caso de que no lo sea, haremos que la distancia de las cantidades sea
                    # igual o mayor para que siempre esté dentro de los límites a iterar
                    if (lenP != lenC):
                        cantidad = cantidad*lenP
                    # Ci contendra la cantidad de turno en el ciclo
                    Ci = 0
                    for i in range(0, lenP, 1):
                        IDnp = producto[i].getID()
                        Ci = cantidad[i]
                        # en cada pasada se deben modificar L y C, pues se pueden actualizar con remover
                        L = self.getLproductos()
                        C = self.getCantidades()
                        Len = len(L)
                        if (Len > 0):
                            for j in range(0, Len, 1):
                                if (IDnp == L[j].getID()):
                                    C[j] = C[j] - Ci
                                    if (C[j] <= 0):
                                        L.pop(j)
                                        C.pop(j)
                                        self.setLproductos(L)
                                        self.setCantidades(C)
                                        print(f'Se ha removido {producto[i].getNombre()} del carro')
                                        break


                                    else:
                                        self.setCantidades(C)
                                        print(f'Se han restado {cantidad[i]} de {producto[i].getNombre()}')
                                        break

        else:
            print('El carro se encuentra vacío')

    def verProducto(self):

        L = self.getLproductos()
        C = self.getCantidades()
        Len = len(L)
        if (Len > 0):
            print('Nombre', '\t', 'Precio', '\t', 'Cantidad')
            for i in range(0, Len, 1):
                print(L[i].getNombre(), '\t', L[i].getPrecio(), '\t', C[i])
        else:
            print('El carro se encuentra vacío')


