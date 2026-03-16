# Ejercicio 28: Realizar una encuesta cargando la edad de 10 personas.
# Mostrar: Promedio de edad, Cantidad de personas mayores de 18

# BLOQUE 1: Entrada de datos - Solicitar edad de 10 personas en una lista
edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

# BLOQUE 2: Procesamiento - Calcular promedio de edad
promedio = sum(edades) / len(edades)

# BLOQUE 3: Procesamiento - Contar personas mayores de 18
mayores_18 = len([edad for edad in edades if edad > 18])

# BLOQUE 4: Salida - Mostrar resultados
print(f"Edades: {edades}")
print(f"Promedio de edad: {promedio:.2f}")
print(f"Personas mayores de 18 años: {mayores_18}")
