from Carro import Carro
from Producto import Producto
from Persona import Persona


Pro1 = Producto('Pescado', 11000, 'pescaderia', 4)


Pro2 = Producto('Carne de res', 11000, 'Carnicería', 1)
Pro3 = Producto('Papas', 3000, 'Verduras', 2)
Pro4 = Producto('Pasta', 4700, 'Empacados', 3)


car1 = Carro(1, [], [])
car2 = Carro(1, [], [])

car1.agregarProducto(Pro1)

car2.agregarProducto(Pro2)

print()
print('Carro 1')
car1.verProducto()
print()
print('Carro 2')
car2.verProducto()

Persona1 = Persona('Luis', 'M', 27, 3154175450,'cll 70a #2c-28', '1143850138')

print()
print('Persona1')
Persona1.verCarro()

#Persona1.carro.setLproductos([])
#Persona1.carro.setCantidades([])


print()
print('Carro 1')
car1.verProducto()
print()
print('Carro 2')
car2.verProducto()
print()
print('Persona1')
Persona1.verCarro()

c3 = Carro(3, [], [])

print()
print('Carro 3')
c3.verProducto()

c3.agregarProducto(Pro4)

print()
print('Carro 1')
car1.verProducto()
print()
print('Carro 2')
car2.verProducto()
print()
print('Persona1')
Persona1.verCarro()
print()
print('Carro 3')
c3.verProducto()

Persona1.agregarCarro(Pro3)

print()
print('Carro 1')
car1.verProducto()
print()
print('Carro 2')
car2.verProducto()
print()
print('Persona1')
Persona1.verCarro()
print()
print('Carro 3')
c3.verProducto()


carro = Carro(69, [], [])

carro.agregarProducto(Producto1)
carro.removerProducto(Producto1)

carro.agregarProducto(productos, 10)
carro.verProducto()

carro.removerProducto(productos)
carro.removerProducto(productos, 2)
carro.removerProducto(productos, [2])
print('se elimina en lista')

carro.removerProducto(productos, [1, 2, 3])

print()
print('Carro')
carro.verProducto()

