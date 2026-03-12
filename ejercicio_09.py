# Ejercicio 9: Pedir 10 números y contar cuántos son positivos y cuántos negativos.

positivos = 0
negativos = 0

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
