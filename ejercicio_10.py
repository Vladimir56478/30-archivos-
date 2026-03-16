# Ejercicio 10: Pedir 10 números y determinar cuál es el mayor y cuál es el menor.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Encontrar mayor y menor
mayor = max(numeros)
menor = min(numeros)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
