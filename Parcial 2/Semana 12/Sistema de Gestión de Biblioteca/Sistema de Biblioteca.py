# Se importa la librería json para poder guardar y cargar datos en formato JSON
import json

# Se importa os para verificar si el archivo existe antes de cargarlo
import os

# Nombre del archivo donde se almacenarán los datos de forma persistente
ARCHIVO = "biblioteca.json"


# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
class Libro:
    """
    Representa un libro dentro del sistema.

    Decisiones de diseño:
    - Se usa una TUPLA para (titulo, autor) porque estos datos no deben cambiar.
    - ISBN funciona como identificador único.
    - 'disponible' indica si el libro está prestado o no.
    """

    def __init__(self, titulo, autor, categoria, isbn, disponible=True):
        # Se almacenan título y autor en una TUPLA
        self.datos = (titulo, autor)

        # Categoría del libro (puede modificarse si se reclasifica)
        self.categoria = categoria

        # Identificador único del libro
        self.isbn = isbn

        # Estado del libro (True = disponible, False = prestado)
        self.disponible = disponible

    def to_dict(self):
        """
        Convierte el objeto Libro en un diccionario.
        Esto es necesario porque JSON no puede guardar objetos directamente.
        """
        return {
            "titulo": self.datos[0],
            "autor": self.datos[1],
            "categoria": self.categoria,
            "isbn": self.isbn,
            "disponible": self.disponible
        }

    def __str__(self):
        # Representación en texto del libro
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.datos[0]} - {self.datos[1]} | {self.categoria} | ISBN: {self.isbn} | {estado}"

# CLASE USUARIO
class Usuario:
    """
    Representa un usuario registrado en la biblioteca.

    Decisiones:
    - Se usa una LISTA para libros_prestados
    - Se almacenan los ISBN en lugar de objetos Libro para evitar duplicación.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre

        # ID único del usuario
        self.id_usuario = id_usuario

        # Lista dinámica de ISBN de libros prestados
        self.libros_prestados = []

    def to_dict(self):
        """
        Convierte el objeto Usuario en diccionario para guardarlo en JSON.
        """
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": self.libros_prestados
        }

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

# CLASE BIBLIOTECA

class Biblioteca:
    """
    Clase principal que gestiona todo el sistema.

    Estructuras utilizadas:
    - Diccionario (catalogo):
        Permite buscar libros rápidamente usando ISBN como clave.
    - Diccionario (usuarios):
        Permite acceso rápido por ID.
    - Set (ids_registrados):
        Garantiza que no existan IDs repetidos.
    """

    def __init__(self):
        # Diccionario: ISBN  objeto Libro
        self.catalogo = {}

        # Diccionario: ID  objeto Usuario
        self.usuarios = {}

        # Conjunto para asegurar unicidad de IDs
        self.ids_registrados = set()

        # Al iniciar el sistema se cargan los datos guardados
        self.cargar_datos()

    # Aquí se guardan y se cargan los libros
    def guardar_datos(self):
        """
        Guarda toda la información en el archivo JSON.
        Se llama automáticamente después de cada modificación importante.
        """

        # Aquí se convierten los objetos a diccionarios
        data = {
            "libros": [libro.to_dict() for libro in self.catalogo.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }

        # Aquí se escribe el archivo en modo escritura
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """
        Carga la información desde el archivo JSON si existe.
        Permite persistencia de datos entre ejecuciones.
        """

        # Aquí se verifica si el archivo existe
        if os.path.exists(ARCHIVO):

            # Se abre el archivo en modo lectura
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Se reconstruyen los objetos Libro
                for l in data.get("libros", []):
                    libro = Libro(
                        l["titulo"],
                        l["autor"],
                        l["categoria"],
                        l["isbn"],
                        l["disponible"]
                    )
                    self.catalogo[libro.isbn] = libro

                # Se reconstruyen los objetos Usuario
                for u in data.get("usuarios", []):
                    usuario = Usuario(u["nombre"], u["id_usuario"])
                    usuario.libros_prestados = u["libros_prestados"]
                    self.usuarios[usuario.id_usuario] = usuario

                    # Se agrega el ID al set para mantener unicidad
                    self.ids_registrados.add(usuario.id_usuario)

    # LIBROS DEL SISTEMA
    def agregar_libro(self, libro):
        # Verifica que el ISBN no exista
        if libro.isbn not in self.catalogo:
            self.catalogo[libro.isbn] = libro
            self.guardar_datos()  # Se guarda automáticamente
            print("✔ Libro agregado.")
        else:
            print("⚠ El libro ya existe.")

    def eliminar_libro(self, isbn):
        # Verifica existencia antes de eliminar
        if isbn in self.catalogo:
            del self.catalogo[isbn]
            self.guardar_datos()
            print("✔ Libro eliminado.")
        else:
            print("⚠ ISBN no encontrado.")

    # USUARIOS
    def registrar_usuario(self, usuario):
        # Se valida unicidad usando el set
        if usuario.id_usuario not in self.ids_registrados:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_registrados.add(usuario.id_usuario)
            self.guardar_datos()
            print("✔ Usuario registrado.")
        else:
            print("⚠ ID ya registrado.")

    # PRÉSTAMOS
    def prestar_libro(self, isbn, id_usuario):
        # Se verifica que libro y usuario existan
        if isbn in self.catalogo and id_usuario in self.usuarios:

            libro = self.catalogo[isbn]
            usuario = self.usuarios[id_usuario]

            # Se verifica disponibilidad del libro
            if libro.disponible:
                libro.disponible = False
                usuario.libros_prestados.append(isbn)
                self.guardar_datos()
                print("✔ Préstamo realizado.")
            else:
                print("⚠ Libro ya prestado.")
        else:
            print("⚠ Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        # Verifica que el usuario exista
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            # Verifica que el usuario tenga ese libro
            if isbn in usuario.libros_prestados:
                usuario.libros_prestados.remove(isbn)
                self.catalogo[isbn].disponible = True
                self.guardar_datos()
                print("✔ Libro devuelto.")
                return

        print("⚠ No se encontró el préstamo.")

    # LISTAR
    def listar_prestados(self, id_usuario):
        # Muestra los libros prestados a un usuario
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            if usuario.libros_prestados:
                for isbn in usuario.libros_prestados:
                    print(self.catalogo[isbn])
            else:
                print("No tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# MENÚ DEL SISTEMA DE BIBLIOTECA

def mostrar_menu():
    """
    Muestra las opciones disponibles para el usuario.
    """
    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Listar libros prestados")
    print("6. Salir")


# Se crea una instancia de la biblioteca
biblioteca = Biblioteca()

# Bucle infinito para mantener activo el sistema
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Captura de datos para nuevo libro
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")
        libro = Libro(titulo, autor, categoria, isbn)
        biblioteca.agregar_libro(libro)

    elif opcion == "2":
        # Registro de usuarios
        nombre = input("Nombre: ")
        id_usuario = input("ID: ")
        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)

    elif opcion == "3":
        # Préstamos
        isbn = input("ISBN del libro: ")
        id_usuario = input("ID del usuario: ")
        biblioteca.prestar_libro(isbn, id_usuario)

    elif opcion == "4":
        # Devolución
        isbn = input("ISBN del libro: ")
        id_usuario = input("ID del usuario: ")
        biblioteca.devolver_libro(isbn, id_usuario)

    elif opcion == "5":
        # Listar libros prestados
        id_usuario = input("ID del usuario: ")
        biblioteca.listar_prestados(id_usuario)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")