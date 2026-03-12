# Ejercicio 3: Pedir la edad de una persona y clasificarla en:
# Menor de edad, Joven, Adulto, Adulto mayor

edad = int(input("Ingrese su edad: "))

if edad < 18:
    clasificacion = "Menor de edad"
elif edad < 30:
    clasificacion = "Joven"
elif edad < 60:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto mayor"

print(f"Edad: {edad}")
print(f"Clasificación: {clasificacion}")
