# Ejercicio 28: Realizar una encuesta cargando la edad de 10 personas.
# Mostrar: Promedio de edad, Cantidad de personas mayores de 18

edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

promedio = sum(edades) / len(edades)
mayores_18 = len([edad for edad in edades if edad > 18])

print(f"Edades: {edades}")
print(f"Promedio de edad: {promedio:.2f}")
print(f"Personas mayores de 18 años: {mayores_18}")
