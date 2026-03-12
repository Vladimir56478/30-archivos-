# Ejercicio 23: Cargar 10 números en una lista y calcular el promedio.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

promedio = sum(numeros) / len(numeros)
print(f"Números: {numeros}")
print(f"Promedio: {promedio:.2f}")
