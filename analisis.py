Python

import csv

total_ventas = 0
total_ganancia = 0
productos = {}

with open('ventas.csv', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        costo = float(row['costo'])
        precio = float(row['precio'])
        cantidad = int(row['cantidad'])

        venta = precio * cantidad
        ganancia = (precio - costo) * cantidad

        total_ventas += venta
        total_ganancia += ganancia

        producto = row['producto']
        productos[producto] = productos.get(producto, 0) + cantidad

print("Total vendido:", total_ventas)
print("Ganancia total:", total_ganancia)

print("\nProductos más vendidos:")
for p, c in productos.items():
    print(p, ":", c)




