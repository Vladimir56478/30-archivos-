# Ejercicio 13: Pedir números hasta que el usuario ingrese un número negativo.
# Contar cuántos números positivos se ingresaron.

cantidad_positivos = 0

while True:
    num = int(input("Ingrese un número (negativo para salir): "))
    if num < 0:
        break
    if num > 0:
        cantidad_positivos += 1

print(f"Cantidad de números positivos: {cantidad_positivos}")
