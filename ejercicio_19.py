# Ejercicio 19: Registrar la asistencia de 10 alumnos usando:
# 1 = presente, 0 = ausente
# Mostrar la cantidad de presentes y ausentes.

presentes = 0
ausentes = 0

for i in range(10):
    asistencia = int(input(f"Ingrese asistencia del alumno {i+1} (1=presente, 0=ausente): "))
    if asistencia == 1:
        presentes += 1
    elif asistencia == 0:
        ausentes += 1

print(f"Presentes: {presentes}")
print(f"Ausentes: {ausentes}")
