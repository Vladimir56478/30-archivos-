# Ejercicio 2: Pedir el sueldo de una persona y calcular el sueldo final aplicando aumentos:
# Si es menor a 400000 → aumento del 15%
# Si está entre 400000 y 800000 → aumento del 10%
# Si es mayor a 800000 → aumento del 5%

sueldo = int(input("Ingrese el sueldo: "))

if sueldo < 400000:
    aumento = sueldo * 0.15
elif sueldo <= 800000:
    aumento = sueldo * 0.10
else:
    aumento = sueldo * 0.05

sueldo_final = sueldo + aumento
print(f"Sueldo original: {sueldo}")
print(f"Aumento: {aumento}")
print(f"Sueldo final: {sueldo_final}")
