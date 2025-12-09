# Programa tradicional

# Función para ingresar las temperaturas
# ---------------------------
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura por día:")

    # Se piden 7 datos, uno por cada día de la semana
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)

    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temps):
    # Se suman todas las temperaturas y se dividen entre 7
    return sum(temps) / len(temps)

# Función principal
def main():
# Llamamos a la función que pide los datos al usuario
    temperaturas = ingresar_temperaturas()

    # Calculamos el promedio con otra función
    promedio = calcular_promedio(temperaturas)

    # Mostramos el resultado final
    print(f"\nEl promedio semanal de la temperatura es: {promedio:.2f} °C")

# Ejecutamos el programa
main()

