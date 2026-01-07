"""Programa: Cálculo del área de un rectángulo"""

# Solicitar datos al usuario
ancho = float(input("Ingrese el ancho del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Cálculo del área
area_rectangulo = ancho * altura

# Contador de cálculos realizados (integer)
cantidad_calculos = 1

# Evaluación del área (boolean)
es_area_grande = area_rectangulo >= 50

# Mostrar resultados en pantalla
print("El área del rectángulo es:", area_rectangulo)
print("Cantidad de cálculos realizados:", cantidad_calculos)

#Condición
if es_area_grande:
    print("El área es grande.")
else:
    print("El área es pequeña.")
