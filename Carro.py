from Producto import Producto


class Carro:

    def __init__(self, car_ID, Lproductos, Cantidad):
        self.car_ID = car_ID
        self.Lproductos = Lproductos
        self.cantidades = Cantidad

    def getLproductos(self):
        return self.Lproductos

    def setLproductos(self, n):
        self.Lproductos = n

    def getCantidades(self):
        return self.cantidades

    def setCantidades(self, n):
        self.cantidades = n

    def agregarProducto(self, producto, cantidad=[1]):
        if isinstance(cantidad, int):
            cantidad = [cantidad]

        L = self.getLproductos()
        C = self.getCantidades()
        Len = len(L)
        if (isinstance(producto, Producto)):
            IDnp = producto.getID()
            it = 0
            if (Len > 0):
                for i in range(0, Len, 1):
                    if (IDnp != L[i].getID()):
                        it += 1
                    else:
                        C[i] = C[i] + cantidad[0]
                        print(f'Se ha sumado {cantidad[0]} a {producto.getNombre()}')
                        self.setCantidades(C)
                        break
                if (it == Len):
                    L.append(producto)
                    C.append(cantidad[0])
                    self.setLproductos(L)
                    self.setCantidades(C)
                    print(f'Se ha agregado {cantidad[0]} {producto.getNombre()} al carro')
            else:
                L.append(producto)
                C.append(cantidad[0])
                self.setLproductos(L)
                self.setCantidades(C)
                print(f'Se ha agregado {cantidad[0]} {producto.getNombre()} al carro')
        else:
            if (isinstance(producto, list)):
                lenP = len(producto)
                lenC = len(cantidad)
                IDnp = ''
                if (lenP != lenC):
                    cantidad = cantidad * lenP

                for i in range(0, lenP, 1):
                    IDnp = producto[i].getID()
                    it = 0
                    if (Len > 0):
                        for j in range(0, Len, 1):
                            if (IDnp != L[j].getID()):
                                it += 1
                            else:
                                C[j] = C[j] + cantidad[i]
                                print(f'Se han sumado {cantidad[i]} a  {producto[i].getNombre()}')
                                self.setCantidades(C)
                                break

                        if (it == Len):
                            L.append(producto[i])
                            C.append(cantidad[i])
                            self.setLproductos(L)
                            self.setCantidades(C)
                            print(f'Se ha agregado {cantidad[i]} {producto[i].getNombre()} al carro')

                    else:
                        L.append(producto[i])
                        C.append(cantidad[i])
                        self.setLproductos(L)
                        self.setCantidades(C)
                        print(f'Se ha agregado {cantidad[i]} {producto[i].getNombre()} al carro')

    def removerProducto(self, producto, cantidad=1):
        if (isinstance(cantidad, int)):
            cantidad = [cantidad]

        L = self.getLproductos()
        C = self.getCantidades()
        Len = len(L)
        IDnp = 0
        if (Len > 0):
            if (isinstance(producto, Producto)):
                IDnp = producto.getID()
                for i in range(0, Len, 1):
                    if (IDnp == L[i].getID()):
                        C[i] = C[i] - cantidad[0]
                        if (C[i] <= 0):
                            L.pop(i)
                            C.pop(i)
                            self.setLproductos(L)
                            self.setCantidades(C)
                            print(f'Se ha removido {producto.getNombre()} del carro')
                            break
                        else:
                            self.setCantidades(C)
                            print(f'Se han restado {cantidad[0]} de {producto[i].getNombre()}')
                            break

            else:
                if (isinstance(producto, list)):
                    lenP = len(producto)
                    lenC = len(cantidad)
                    IDnp = 0

                    if (lenP != lenC):
                        cantidad = cantidad*lenP

                    Ci = 0
                    for i in range(0, lenP, 1):
                        IDnp = producto[i].getID()
                        Ci = cantidad[i]
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
                                        print(f'Se han restado {cantidad[0]} de {producto[i].getNombre()}')
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


