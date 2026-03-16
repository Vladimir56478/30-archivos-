# Ejercicio 14: Pedir 10 notas de alumnos y mostrar cuántos están aprobados y cuántos desaprobados.

# BLOQUE 1: Inicialización - Contadores
aprobados = 0
desaprobados = 0

# BLOQUE 2: Entrada y procesamiento - Solicitar notas y contar
for i in range(10):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

# BLOQUE 3: Salida - Mostrar resultados
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
