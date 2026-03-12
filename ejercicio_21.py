# Ejercicio 21: Cargar 10 números en un arreglo (lista) y mostrarlos por pantalla.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

print("Números ingresados:")
print(numeros)
