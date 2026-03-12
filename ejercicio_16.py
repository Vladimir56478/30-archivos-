# Ejercicio 16: Simular un sistema de ventas.
# Pedir el precio de 5 productos y calcular:
# El total de la compra, El precio promedio

precios = []
for i in range(5):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    precios.append(precio)

total = sum(precios)
promedio = total / len(precios)

print(f"Precios: {precios}")
print(f"Total de la compra: {total:.2f}")
print(f"Precio promedio: {promedio:.2f}")
