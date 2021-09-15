from Producto import Producto
from Carro import Carro


class Persona:

    def __init__(self, nombre, genero, edad, telefono, direccion, ID, ):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.ID = ID
        self.carro = Carro(ID, [], [])

    def getNombre(self):
        return self.nombre

    def setNombre(self, n):
        self.nombre = n

    def getGenero(self):
        return self.genero

    def setGenero(self, n):
        self.genero = n

    def getEdad(self):
        return self.edad

    def setEdad(self, n):
        self.edad = n

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, n):
        self.telefono = n

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, n):
        self.direccion = n

    def getID(self):
        return self.ID

    def setID(self, n):
        self.ID = n

    def getCarro(self):
        return self.carro

    def setCarro(self, n):
        if (isinstance(n, Carro)):
            self.carro = n

    def Saludar(self):
        print(f'Hola mi gente soy {self.nombre}')

    def agregarCarro(self, pn, q=1):
        if isinstance(pn, Producto) or isinstance(pn, list):
            c = self.getCarro()
            c.agregarProducto(pn, q)
            self.setCarro(c)

    def removerCarro(self, pn, q=[1]):
        self.carro.removerProducto(pn, q)


    def verCarro(self):
        caro = self.getCarro()
        caro.verProducto()
