# Ejercicio 12: Pedir números hasta ingresar 0 y calcular el promedio de los números ingresados.

suma_total = 0
cantidad = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    suma_total += num
    cantidad += 1

if cantidad > 0:
    promedio = suma_total / cantidad
    print(f"Cantidad de números: {cantidad}")
    print(f"Suma total: {suma_total}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números")
