
from Persona import Persona
from Producto import Producto
from Carro import Carro
from Tienda import Tienda

Persona1 = Persona('Luis', 'M', 27, 3154175450,'cll 70a #2c-28', '1143850138')


n = Persona1.getNombre()
e = Persona1.getEdad()
d = Persona1.direccion

print(f'Mi nombre es {n}, tengo {e} años y vivo en {d}')

c = Carro([], [])

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
Persona1.costoTotalCarro()

print('Primeros productos')
Persona1.agregarCarro(Producto1)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Agregando 2 entero')
Persona1.agregarCarro(Producto1, 2)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Agregando 3 en una lista')
Persona1.agregarCarro(Producto1, [3])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se agrega una lista sin cantidad')
Persona1.agregarCarro(productos)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se agrega una lista con 2 entero')
Persona1.agregarCarro(productos, 2)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se agrega una lista con 3 en una lista')
Persona1.agregarCarro(productos, [3])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se agrega una lista con cantidades diferentes')
Persona1.agregarCarro(productos, [1, 2, 4])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover un producto')
Persona1.removerCarro(Producto1)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover un producto con cantidad entera')
Persona1.removerCarro(Producto1, 2)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover un producto con cantidad en una lista')
Persona1.removerCarro(Producto1, [3])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover un todas las unidades de un producto')
Persona1.removerCarro(Producto1, [7])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover un todas las unidades de un producto')
Persona1.removerCarro(Producto1, [7])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Remover más de las unidades que hay de un producto')
Persona1.removerCarro(Producto2, 10)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Agregamos nuevamente papas y carne')
Persona1.agregarCarro(productos, [10])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se remueve una lista')
Persona1.removerCarro(productos)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se remueve una lista con cantidad entera')
Persona1.removerCarro(productos, 3)
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se remueve una lista con cantidad en una lista')
Persona1.removerCarro(productos, [2])
Persona1.verCarro()
Persona1.costoTotalCarro()

print()
print('Se remueve una lista con cantidades diferentes en una lista')
Persona1.removerCarro(productos, [3, 1, 9])
Persona1.verCarro()
Persona1.costoTotalCarro()


print()
print('Se crea la tienda super_market')
super_market = Tienda('super_market')
super_market.agregarInventario(productos, 100)
super_market.verInventario()


print()
print('Se prueba el metodo consultarExistencia')
exists = super_market.consultarExistencia(Persona1.getCarro())
print(exists)


print()
print('Se crea un nuevo producto a consultar existencia')
Producto4 = Producto('Martillo', 25000, 'Ferreteria', 64)
Persona1.agregarCarro(Producto4)
exists = super_market.consultarExistencia(Persona1.getCarro())
print(exists)

print()
print('Agregaremos más unidades al carro que las disponibles en inventario')
Persona1.agregarCarro(Producto1, 100)
Persona1.agregarCarro(Producto2, 100)
Persona1.verCarro()

print()
print('Se prueba el metodo de consultar cantidades')
super_market.consultarCantidad(Persona1.getCarro())

