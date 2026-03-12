# Ejercicio 29: Pedir un número y mostrar todos sus divisores.

numero = int(input("Ingrese un número: "))

divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Número: {numero}")
print(f"Divisores: {divisores}")
