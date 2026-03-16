# Ejercicio 21: Cargar 10 números en un arreglo (lista) y mostrarlos por pantalla.

# BLOQUE 1: Entrada de datos - Solicitar 10 números en una lista
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# BLOQUE 2: Salida - Mostrar números ingresados
print("Números ingresados:")
print(numeros)
