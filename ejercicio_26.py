# Ejercicio 26: Cargar 10 números en una lista y mostrar:
# El mayor, El menor, El promedio

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Calcular mayor, menor y promedio
mayor = max(numeros)
menor = min(numeros)
promedio = sum(numeros) / len(numeros)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Promedio: {promedio:.2f}")
