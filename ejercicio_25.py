# Ejercicio 25: Cargar 10 números en una lista y mostrar cuántos son mayores que el promedio.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

promedio = sum(numeros) / len(numeros)
mayores_promedio = [num for num in numeros if num > promedio]
cantidad = len(mayores_promedio)

print(f"Números: {numeros}")
print(f"Promedio: {promedio:.2f}")
print(f"Números mayores que el promedio: {mayores_promedio}")
print(f"Cantidad: {cantidad}")
