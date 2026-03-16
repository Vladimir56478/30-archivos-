# Ejercicio 8: Pedir 10 números al usuario y calcular:
# La suma total
# El promedio

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Procesamiento - Calcular suma y promedio
suma_total = sum(numeros)
promedio = suma_total / len(numeros)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
