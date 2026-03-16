# Ejercicio 7: Mostrar los números entre 1 y 100 que sean pares y múltiplos de 5.

# BLOQUE 1: Encabezado
print("Números pares y múltiplos de 5 entre 1 y 100:")

# BLOQUE 2: Iteración - Recorrer números y filtrar por condiciones
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end=" ")

# BLOQUE 3: Salida - Nueva línea para finalizar
print()
