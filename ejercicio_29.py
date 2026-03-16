# Ejercicio 29: Pedir un número y mostrar todos sus divisores.

# BLOQUE 1: Entrada de datos - Solicitar número
numero = int(input("Ingrese un número: "))

# BLOQUE 2: Procesamiento - Encontrar todos los divisores
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Número: {numero}")
print(f"Divisores: {divisores}")
