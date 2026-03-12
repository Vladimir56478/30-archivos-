# Ejercicio 24: Cargar 10 números en una lista y mostrar solo los números pares.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

pares = [num for num in numeros if num % 2 == 0]
print(f"Números: {numeros}")
print(f"Números pares: {pares}")
