class Estudiante:
    "Clase que representa a un estudiante dentro de un sistema académico."

    def __init__(self, nombre, carrera):
        """
        Constructor:
        Se ejecuta cuando se crea el objeto.
        Inicializa los datos del estudiante.
        """
        self.nombre = nombre
        self.carrera = carrera
        print(f"Constructor: Estudiante {self.nombre} ingreso en la carrera de {self.carrera}.")

    def mostrar_datos(self):
        "Muestra la información del estudiante."
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")

    def __del__(self):
        """
        Destructor:
        Se ejecuta cuando el objeto se elimina o finaliza el programa.
        Simula la eliminación del estudiante del sistema.
        """
        print(f"Destructor: Estudiante {self.nombre} ha sido eliminado con éxito.")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto estudiante
    estudiante1 = Estudiante("Cristian Rojas Burgos", "Tecnologías de la Información")

    # Uso del objeto
    estudiante1.mostrar_datos()

    # El destructor se ejecutará automáticamente al finalizar el programa o eliminar el objeto
