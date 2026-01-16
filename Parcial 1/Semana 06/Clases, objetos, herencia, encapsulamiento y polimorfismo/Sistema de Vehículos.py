# Sistema de Vehículos
# Vehículo genérico
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos
        self.marca = marca
        self.modelo = modelo

        # Atributo (Encapsulación)
        # Solo puede accederse desde la misma clase
        self.__velocidad = 0

        # Método para aumentar la velocidad

    def acelerar(self, incremento):
        if incremento > 0:
            self.__velocidad += incremento

    # Método para obtener la velocidad actual
    # Permite acceder al atributo privado
    def get_velocidad(self):
        return self.__velocidad

    # Método que será sobrescrito en la clase hija
    # Ejemplo de Polimorfismo
    def descripcion(self):
        return f"Vehículo {self.marca} {self.modelo}"

# Clase derivada Auto
# Hereda los atributos y métodos de la clase Vehículo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamada al constructor de la clase padre (Herencia)
        super().__init__(marca, modelo)

        # Atributo propio de la clase Auto
        self.puertas = puertas

    # Método sobrescrito
    # Demuestra el Polimorfismo
    def descripcion(self):
        return f"Auto {self.marca} {self.modelo} con {self.puertas} puertas"

# Programa principal
if __name__ == "__main__":
    # Creación de un objeto de la clase Vehiculo
    vehiculo1 = Vehiculo("Genérico", "2014")

    # Creación de un objeto de la clase Auto
    auto1 = Auto("Chevrolet", "Sail", 5)

    # Uso del método acelerar en ambos objetos
    vehiculo1.acelerar(60)
    auto1.acelerar(80)

    # Información del vehículo genérico
    print(vehiculo1.descripcion())
    print("Velocidad:", vehiculo1.get_velocidad(), "km/h")

    # Información del auto
    print(auto1.descripcion())
    print("Velocidad:", auto1.get_velocidad(), "km/h")
