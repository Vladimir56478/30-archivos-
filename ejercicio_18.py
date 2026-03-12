# Ejercicio 18: Registrar el sueldo de 10 empleados y mostrar:
# El sueldo promedio, El sueldo más alto

sueldos = []
for i in range(10):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    sueldos.append(sueldo)

promedio = sum(sueldos) / len(sueldos)
mas_alto = max(sueldos)

print(f"Sueldos: {sueldos}")
print(f"Sueldo promedio: {promedio:.2f}")
print(f"Sueldo más alto: {mas_alto:.2f}")
