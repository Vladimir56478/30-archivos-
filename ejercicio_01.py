# Ejercicio 1: Pedir tres números al usuario y determinar cuál es el mayor y cuál es el menor.

# BLOQUE 1: Entrada de datos - Solicitar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# BLOQUE 2: Procesamiento - Encontrar mayor y menor
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

# BLOQUE 3: Salida - Mostrar resultados
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
