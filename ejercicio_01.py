# Ejercicio 1: Pedir tres números al usuario y determinar cuál es el mayor y cuál es el menor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
