from Producto import Producto
from Carro import Carro

#########################################################################
# Clase persona
#########################################################################

# La clase persona será la herramienta para considerar al usuario
# Esta contendrá sus datos relevantes y métodos que ayuden a mejorar su experiencia
# Cada persona tendrá un Carro
class Persona:

    def __init__(self, nombre, genero, edad, telefono, direccion, ID, ):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.ID = ID
        self.carro = Carro(ID, [], [])

#########################################################################
# Setters y Getters
#########################################################################

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

#########################################################################
# Métodos
#########################################################################

    # agregarCarro llama al método agregarProducto() desde su carro
    def agregarCarro(self, pn, q=1):
        if isinstance(pn, Producto) or isinstance(pn, list):
            # usamos c para guardar el carro
            c = self.getCarro()
            # llamamos el método agregando la cantidad y producto ingresados
            c.agregarProducto(pn, q)
            # Actualizamos el carro
            self.setCarro(c)

    def removerCarro(self, pn, q=[1]):
        self.carro.removerProducto(pn, q)


    def verCarro(self):
        caro = self.getCarro()
        caro.verProducto()
