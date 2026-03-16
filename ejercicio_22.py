# Ejercicio 22: Cargar 10 números en una lista y mostrar cuál es el mayor.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Encontrar el mayor
mayor = max(numeros)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"El mayor es: {mayor}")
