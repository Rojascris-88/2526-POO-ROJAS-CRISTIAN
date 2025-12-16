class Libro:
    """Representa un libro físico en la biblioteca."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Atributo de estado

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


class Usuario:
    """Representa a una persona que puede retirar libros."""
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_en_prestamo = []

    def solicitar_libro(self, libro):
        """Intenta cambiar el estado del objeto Libro y lo añade a su lista."""
        if libro.disponible:
            libro.disponible = False
            self.libros_en_prestamo.append(libro)
            print(f"{self.nombre} ha retirado: {libro.titulo}")
        else:
            print(f"Disculpa, el libro '{libro.titulo}' ya está prestado.")


class Biblioteca:
    """Clase principal que gestiona el inventario de libros."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_libro(self, libro):
        self.inventario.append(libro)

    def mostrar_libros(self):
        print(f"\n--- Libros en {self.nombre} ---")
        for libro in self.inventario:
            print(f"- {libro}")


# --- Ejecución del Programa ---
if __name__ == "__main__":
    # Crear la biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Universidad Amazónica")

    # Crear libros (Instancias)
    libro_1 = Libro("Don Quijote de la mancha", "Miguel de Cervantes")
    libro_2 = Libro("El Principito", "Antonie de Saint-Exupéry")

    # Registrar libros en la biblioteca
    mi_biblioteca.agregar_libro(libro_1)
    mi_biblioteca.agregar_libro(libro_2)

    # Crear un usuario
    estudiante = Usuario("Cristian Rojas", "ST001")

    # Mostrar estado inicial
    mi_biblioteca.mostrar_libros()

    # Interacción de préstamo
    print("\nPROCESO DE PRÉSTAMO:")
    estudiante.solicitar_libro(libro_1)
    estudiante.solicitar_libro(libro_1) # Intentar llevar el mismo libro de nuevo

    # Mostrar estado final
    mi_biblioteca.mostrar_libros()