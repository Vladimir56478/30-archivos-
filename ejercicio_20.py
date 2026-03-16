# Ejercicio 20: Pedir 10 números y contar cuántos son pares y cuántos impares.

# BLOQUE 1: Inicialización - Contadores
pares = 0
impares = 0

# BLOQUE 2: Entrada y procesamiento - Solicitar números y contar
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
