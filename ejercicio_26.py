# Ejercicio 26: Cargar 10 números en una lista y mostrar:
# El mayor, El menor, El promedio

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)
promedio = sum(numeros) / len(numeros)

print(f"Números: {numeros}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Promedio: {promedio:.2f}")
