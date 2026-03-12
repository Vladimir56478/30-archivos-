# Ejercicio 22: Cargar 10 números en una lista y mostrar cuál es el mayor.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
print(f"Números: {numeros}")
print(f"El mayor es: {mayor}")
