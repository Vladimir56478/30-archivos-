# Ejercicio 11: Pedir números al usuario hasta que ingrese 0.
# Mostrar: La suma total, La cantidad de números ingresados

# BLOQUE 1: Inicialización - Variables acumuladores
suma_total = 0
cantidad = 0

# BLOQUE 2: Entrada y procesamiento - Solicitar números hasta recibir 0
while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    suma_total += num
    cantidad += 1

# BLOQUE 3: Salida - Mostrar resultados
print(f"Cantidad de números: {cantidad}")
print(f"Suma total: {suma_total}")
