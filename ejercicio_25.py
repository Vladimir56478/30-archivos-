# Ejercicio 25: Cargar 10 números en una lista y mostrar cuántos son mayores que el promedio.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Calcular promedio
promedio = sum(numeros) / len(numeros)

# BLOQUE 3: Procesamiento - Filtrar números mayores que el promedio
mayores_promedio = [num for num in numeros if num > promedio]
cantidad = len(mayores_promedio)

# BLOQUE 4: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Promedio: {promedio:.2f}")
print(f"Números mayores que el promedio: {mayores_promedio}")
print(f"Cantidad: {cantidad}")
