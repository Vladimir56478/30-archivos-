# Ejercicio 15: Pedir 10 edades y mostrar:
# El promedio de edad, La edad mayor

edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)

promedio = sum(edades) / len(edades)
edad_mayor = max(edades)

print(f"Edades: {edades}")
print(f"Promedio de edad: {promedio:.2f}")
print(f"Edad mayor: {edad_mayor}")
