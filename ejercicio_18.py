# Ejercicio 18: Registrar el sueldo de 10 empleados y mostrar:
# El sueldo promedio, El sueldo más alto

# BLOQUE 1: Entrada de datos - Solicitar sueldo de 10 empleados
sueldos = []
for i in range(10):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    sueldos.append(sueldo)

# BLOQUE 2: Procesamiento - Calcular promedio y máximo
promedio = sum(sueldos) / len(sueldos)
mas_alto = max(sueldos)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Sueldos: {sueldos}")
print(f"Sueldo promedio: {promedio:.2f}")
print(f"Sueldo más alto: {mas_alto:.2f}")
