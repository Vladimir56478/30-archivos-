# Ejercicio 15: Pedir 10 edades y mostrar:
# El promedio de edad, La edad mayor

# BLOQUE 1: Entrada de datos - Solicitar 10 edades en una lista
edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)

# BLOQUE 2: Procesamiento - Calcular promedio y edad máxima
promedio = sum(edades) / len(edades)
edad_mayor = max(edades)

# BLOQUE 3: Salida - Mostrar resultados
print(f"Edades: {edades}")
print(f"Promedio de edad: {promedio:.2f}")
print(f"Edad mayor: {edad_mayor}")
