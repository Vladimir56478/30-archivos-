# Ejercicio 4: Pedir tres notas de un alumno, calcular el promedio e indicar si:
# Promoción directa (promedio >= 8), Aprobado (promedio >= 6), Desaprobado (promedio < 6)

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 8:
    estado = "Promoción directa"
elif promedio >= 6:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")
