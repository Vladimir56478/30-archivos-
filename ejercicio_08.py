# Ejercicio 8: Pedir 10 números al usuario y calcular:
# La suma total
# El promedio

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma_total = sum(numeros)
promedio = suma_total / len(numeros)

print(f"Números: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
