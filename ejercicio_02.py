# Ejercicio 2: Pedir el sueldo de una persona y calcular el sueldo final aplicando aumentos:
# Si es menor a 400000 → aumento del 15%
# Si está entre 400000 y 800000 → aumento del 10%
# Si es mayor a 800000 → aumento del 5%

# BLOQUE 1: Entrada de datos - Solicitar sueldo
sueldo = int(input("Ingrese el sueldo: "))

# BLOQUE 2: Procesamiento - Calcular aumento según rango de sueldo
if sueldo < 400000:
    aumento = sueldo * 0.15
elif sueldo <= 800000:
    aumento = sueldo * 0.10
else:
    aumento = sueldo * 0.05

# BLOQUE 3: Cálculo final - Sueldo final con aumento
sueldo_final = sueldo + aumento

# BLOQUE 4: Salida - Mostrar resultados
print(f"Sueldo original: {sueldo}")
print(f"Aumento: {aumento}")
print(f"Sueldo final: {sueldo_final}")
