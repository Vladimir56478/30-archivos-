# Ejercicio 13: Pedir números hasta que el usuario ingrese un número negativo.
# Contar cuántos números positivos se ingresaron.

# BLOQUE 1: Inicialización - Contador de positivos
cantidad_positivos = 0

# BLOQUE 2: Entrada y procesamiento - Solicitar números hasta recibir negativo
while True:
    num = int(input("Ingrese un número (negativo para salir): "))
    if num < 0:
        break
    if num > 0:
        cantidad_positivos += 1

# BLOQUE 3: Salida - Mostrar resultado
print(f"Cantidad de números positivos: {cantidad_positivos}")
