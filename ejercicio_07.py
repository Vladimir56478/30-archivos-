# Ejercicio 7: Mostrar los números entre 1 y 100 que sean pares y múltiplos de 5.

print("Números pares y múltiplos de 5 entre 1 y 100:")
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end=" ")
print()
