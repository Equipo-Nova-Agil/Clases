#########################################################################
# Funciones
#########################################################################
# En este script se guardaran funciones externas a las clases y listas que contendrán todos los existentes

from Carro import Carro
from Producto import Producto
from Persona import Persona


# Esta lista contendrá todos los usuarios que se registren
usuarios_registrados = []
# Esta lista contendrá todos los productos registrados
productos_existentes = []


def crearPersona():
    nombre = input('Escriba su nombre: ')
    genero = input('ingrese su género (másculino, femenino u otro): ')
    edad = int(input('Ingrese su edad: '))
    telefono = input('Ingrese su teléfono: ')
    direccion = input('Ingrese su dirección: ')
    ID = input('Ingrese su número de documento de identidad: ')
    Len = len(usuarios_registrados)
    it = 0
    if (Len > 0):
        for i in range(0, Len):
            if ID != usuarios_registrados[i].getID:
                it += 1
            else:
                print('Ya se encuentra inscrito')
                break
        if it == Len:
            nuevo_usuario = Persona(nombre, genero, edad, telefono, direccion, ID)
            usuarios_registrados.append(nuevo_usuario)
            print('Se ha registrado correctamente')
    else:
        nuevo_usuario = Persona(nombre, genero, edad, telefono, direccion, ID)
        usuarios_registrados.append(nuevo_usuario)
        print('Se ha registrado correctamente')
        return nuevo_usuario


def verPersonas(lista):
    Len = len(lista)
    for i in range(0, Len):
        print(lista[i].getNombre())
