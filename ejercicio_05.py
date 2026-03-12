# Ejercicio 5: Pedir un número e indicar:
# Si es positivo, negativo o cero
# Si es par o impar

numero = int(input("Ingrese un número: "))

if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

if numero % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

print(f"El número {numero} es {signo}")
print(f"El número {numero} es {paridad}")
