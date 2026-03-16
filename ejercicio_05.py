# Ejercicio 5: Pedir un número e indicar:
# Si es positivo, negativo o cero
# Si es par o impar

# BLOQUE 1: Entrada de datos - Solicitar número
numero = int(input("Ingrese un número: "))

# BLOQUE 2: Procesamiento - Determinar signo (positivo, negativo o cero)
if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

# BLOQUE 3: Procesamiento - Determinar paridad (par o impar)
if numero % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

# BLOQUE 4: Salida - Mostrar resultados
print(f"El número {numero} es {signo}")
print(f"El número {numero} es {paridad}")
