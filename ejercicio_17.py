# Ejercicio 17: Crear un sistema de notas para 5 alumnos.
# Para cada alumno pedir: Nombre, Tres notas
# Calcular el promedio e indicar si aprueba o desaprueba.

for i in range(5):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    
    promedio = (nota1 + nota2 + nota3) / 3
    estado = "Aprobado" if promedio >= 6 else "Desaprobado"
    
    print(f"{nombre}: Promedio = {promedio:.2f}, Estado = {estado}")
    print()
