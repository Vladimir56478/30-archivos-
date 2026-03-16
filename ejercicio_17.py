# Ejercicio 17: Crear un sistema de notas para 5 alumnos.
# Para cada alumno pedir: Nombre, Tres notas
# Calcular el promedio e indicar si aprueba o desaprueba.

# BLOQUE 1: Iteración - Procesar 5 alumnos
for i in range(5):
    # BLOQUE 1.1: Entrada de datos - Nombre y notas
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    
    # BLOQUE 1.2: Procesamiento - Calcular promedio
    promedio = (nota1 + nota2 + nota3) / 3
    
    # BLOQUE 1.3: Evaluación - Determinar estado
    estado = "Aprobado" if promedio >= 6 else "Desaprobado"
    
    # BLOQUE 1.4: Salida - Mostrar resultado del alumno
    print(f"{nombre}: Promedio = {promedio:.2f}, Estado = {estado}")
    print()
