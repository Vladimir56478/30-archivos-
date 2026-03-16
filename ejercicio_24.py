# Ejercicio 24: Cargar 10 números en una lista y mostrar solo los números pares.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Filtrar solo números pares
pares = [num for num in numeros if num % 2 == 0]

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Números pares: {pares}")
