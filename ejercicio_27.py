# Ejercicio 27: Cargar 10 notas en una lista y mostrar:
# Promedio general, Cantidad de aprobados, Cantidad de desaprobados

# BLOQUE 1: Entrada de datos - Solicitar 10 notas en una lista
notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# BLOQUE 2: Procesamiento - Calcular promedio general
promedio = sum(notas) / len(notas)

# BLOQUE 3: Procesamiento - Contar aprobados y desaprobados
aprobados = len([nota for nota in notas if nota >= 6])
desaprobados = len([nota for nota in notas if nota < 6])

# BLOQUE 4: Salida - Mostrar resultados
print(f"Notas: {notas}")
print(f"Promedio general: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
