import json   # Librería para guardar y cargar datos en archivos JSON

# SISTEMA DE INVENTARIO DE TIENDA ROJITAS

# CLASE PRODUCTO

class Producto:
    """
    Representa un producto del inventario.
    Contiene atributos privados y métodos para acceder/modificar datos.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados del producto
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener valores (encapsulamiento)

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos para modificar los valores

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Sirve para guardar el producto en un archivo JSON
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    # Mostrar información de los productos que se encuentran en el inventario
    def mostrar(self):
        print(f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}")

# Clase inventario
class Inventario:
    """
    Maneja todos los productos usando un diccionario.
    La clave es el ID y el valor es el objeto Producto.
    """

    def __init__(self):
        # Diccionario para almacenar los productos
        self.productos = {}

    # Nos permite agregar los productos
    def agregar_producto(self, producto):
        # Verifica si el ID ya existe
        if producto.get_id() in self.productos:
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    # Nos permite eliminar los productos
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # Nos permite actualizar los productos
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            # Actualiza solo si se envían valores
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)

            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # Nos permite buscar por nombre del producto
    def buscar_por_nombre(self, nombre):
        # Lista de productos que coinciden con el nombre
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            print("\n🔍 Resultados:")
            for p in encontrados:
                p.mostrar()
        else:
            print("❌ No se encontraron productos.")

    # Nos permite mostrar todos los productos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            print("\n📋 INVENTARIO:")
            for producto in self.productos.values():
                producto.mostrar()

    # Nos permite guardar el inventario de la tienda en archivo JSON
    def guardar_archivo(self, archivo="inventario.json"):
        # Convierte todos los productos a diccionarios
        datos = [p.to_dict() for p in self.productos.values()]

        # Guarda en archivo JSON
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)

        print("💾 Inventario guardado.")

    # CARGAR DESDE ARCHIVO
    def cargar_archivo(self, archivo="inventario.json"):
        try:
            # Abre archivo y carga datos
            with open(archivo, "r") as f:
                datos = json.load(f)

            # Reconstruye los objetos Producto
            for item in datos:
                producto = Producto(
                    item["id"],
                    item["nombre"],
                    item["cantidad"],
                    item["precio"]
                )
                self.productos[producto.get_id()] = producto

            print("📂 Inventario cargado correctamente.")

        except FileNotFoundError:
            # Si el archivo no existe, no pasa nada
            print("⚠️ No existe archivo previo.")

# MENÚ INTERACTIVO
def menu():
    inventario = Inventario()

    # Carga datos al iniciar el programa
    inventario.cargar_archivo()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione opción: ")

        # AGREGAR PRODUCTOS
        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # ELIMINAR PRODUCTOS
        elif opcion == "2":
            id_p = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        # ACTUALIZAR PRODUCTOS
        elif opcion == "3":
            id_p = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            inventario.actualizar_producto(id_p, cantidad, precio)

        # BUSCAR PRODUCTOS
        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        # MOSTRAR PRODUCTOS
        elif opcion == "5":
            inventario.mostrar_todos()

        # SALIR DEL SISTEMA
        elif opcion == "6":
            inventario.guardar_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")

# Ejecución del programa
menu()