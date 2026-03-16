# Ejercicio 9: Pedir 10 números y contar cuántos son positivos y cuántos negativos.

# BLOQUE 1: Inicialización - Contadores para positivos y negativos
positivos = 0
negativos = 0

# BLOQUE 2: Entrada y procesamiento - Solicitar números y contar
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# BLOQUE 3: Salida - Mostrar resultados
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
