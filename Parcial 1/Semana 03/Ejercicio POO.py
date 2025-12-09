# Programa para calcular el promedio semanal del clima usando POO
# Clase que representa el clima semanal
class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado donde se guardan las temperaturas
        self.__temperaturas = []
    # Metodo para ingresar datos
    # ---------------------------
    def ingresar_datos(self):
        print("Ingrese la temperatura de cada día:")
        # Recolectamos 7 temperaturas
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.__temperaturas.append(temp)
       # Metodo para calcular el promedio semanal
    def calcular_promedio(self):
        # Promedio = suma total / cantidad de días
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase hija (ejemplo de herencia)
# Solo muestra el resultado formateado
class MostrarClima(ClimaSemanal):
    # Metodo que combina ingreso, cálculo y despliegue
    def ejecutar(self):
        # Llamamos al metodo heredado para ingresar los datos
        self.ingresar_datos()

        # Calculamos el promedio con el metodo de la clase base
        promedio = self.calcular_promedio()

        # Mostramos el resultado
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")

programa = MostrarClima()
programa.ejecutar()
