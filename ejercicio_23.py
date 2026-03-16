# Ejercicio 23: Cargar 10 números en una lista y calcular el promedio.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Calcular promedio
promedio = sum(numeros) / len(numeros)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Promedio: {promedio:.2f}")
