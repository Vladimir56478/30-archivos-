# Ejercicio 27: Cargar 10 notas en una lista y mostrar:
# Promedio general, Cantidad de aprobados, Cantidad de desaprobados

notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
aprobados = len([nota for nota in notas if nota >= 6])
desaprobados = len([nota for nota in notas if nota < 6])

print(f"Notas: {notas}")
print(f"Promedio general: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
