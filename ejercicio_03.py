# Ejercicio 3: Pedir la edad de una persona y clasificarla en:
# Menor de edad, Joven, Adulto, Adulto mayor

# BLOQUE 1: Entrada de datos - Solicitar edad
edad = int(input("Ingrese su edad: "))

# BLOQUE 2: Procesamiento - Clasificar edad en categorías
if edad < 18:
    clasificacion = "Menor de edad"
elif edad < 30:
    clasificacion = "Joven"
elif edad < 60:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto mayor"

# BLOQUE 3: Salida - Mostrar resultados
print(f"Edad: {edad}")
print(f"Clasificación: {clasificacion}")
