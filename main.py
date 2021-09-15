
from Persona import Persona
from Producto import Producto
from Carro import Carro

Persona1 = Persona('Luis', 'M', 27, 3154175450,'cll 70a #2c-28', '1143850138')



n = Persona1.getNombre()
e = Persona1.getEdad()
d = Persona1.direccion

print(f'Mi nombre es {n}, tengo {e} años y vivo en {d}')

c = Carro(69, [], [])

print('Carro carrudo')
c.verProducto()

Producto1 = Producto('Carne de res', 11000, 'Carnicería', 1)
Producto2 = Producto('Papas', 3000, 'Verduras', 2)
Producto3 = Producto('Pasta', 4700, 'Empacados', 3)

productos = []

productos.append(Producto1)
productos.append(Producto2)
productos.append(Producto3)

print('Se prueba el carro dentro de los atributos de persona')
Persona1.verCarro()

print('Primeros productos')
Persona1.agregarCarro(Producto1)

Persona1.verCarro()


print()
print('Agregando 2 entero')
Persona1.agregarCarro(Producto1, 2)
Persona1.verCarro()

print()
print('Agregando 3 en una lista')
Persona1.agregarCarro(Producto1, [3])
Persona1.verCarro()

print()
print('Se agrega una lista sin cantidad')
Persona1.agregarCarro(productos)
Persona1.verCarro()

print()
print('Se agrega una lista con 2 entero')
Persona1.agregarCarro(productos, 2)
Persona1.verCarro()


print()
print('Se agrega una lista con 3 en una lista')
Persona1.agregarCarro(productos, [3])

Persona1.verCarro()


print()
print('Se agrega una lista con cantidades diferentes')
Persona1.agregarCarro(productos, [1, 2, 4])
Persona1.verCarro()

print()
print('Remover de a un producto')
#Persona1.removerCarro(Producto1)
#Persona1.verCarro()

c.agregarProducto(productos, [10])
c.verProducto()

c.removerProducto(productos)

c.verProducto()