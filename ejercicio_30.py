# Ejercicio 30: Pedir un número e indicar si el número es primo o no primo.

# BLOQUE 1: Entrada de datos - Solicitar número
numero = int(input("Ingrese un número: "))

# BLOQUE 2: Evaluación - Verificar si es primo
if numero < 2:
    print(f"{numero} no es primo")
else:
    # BLOQUE 2.1: Procesamiento - Buscar divisores
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    # BLOQUE 2.2: Salida - Mostrar resultado
    if es_primo:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
