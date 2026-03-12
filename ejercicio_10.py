# Ejercicio 10: Pedir 10 números y determinar cuál es el mayor y cuál es el menor.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)

print(f"Números: {numeros}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
