class Producto:
    """
       SISTEMA DE INVENTARIOS DE UNA FERRETERÍA
       Cada producto tiene un ID único, nombre, cantidad y precio.
       """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_archivo()

    # =========================
    # GUARDAR EN ARCHIVO
    # =========================
    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)
            print("💾 Inventario guardado en archivo.")
        except PermissionError:
            print("❌ Error: No hay permisos para escribir el archivo.")

    # =========================
    # CARGAR ARCHIVO
    # =========================
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id_p, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(id_p, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("📂 Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()
        except PermissionError:
            print("❌ Error: No hay permisos para leer el archivo.")

    # Añade los productos verificando ID único
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_archivo()
        print("✅ Producto agregado y guardado.")

    # Elimina el producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_archivo()
                print("✅ Producto eliminado y archivo actualizado.")
                return
        print("❌ Producto no encontrado.")

    # Actualiza la cantidad o precio
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_archivo()
                print("✅ Producto actualizado y guardado.")
                return
        print("❌ Producto no encontrado.")

    # Busca por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("\n🔎 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos.")

    # Muestra todos los productos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            print("\n📋 Inventario:")
            for p in self.productos:
                print(p)

def menu():
    # Se crea una instancia del inventario una sola vez.
    # Esto permite que los productos se mantengan guardados
    # mientras el usuario usa el sistema
    inventario = Inventario()
    # Bucle infinito sirve para mantener activo el menú
    # hasta que el usuario decida salir.
    while True:
        print("\n===== SISTEMA DE INVENTARIO DE FERRETERÍA =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Salir")
        # Solicitamos al usuario para que eliga una opción
        opcion = input("Seleccione una opción: ")
        # Aquí se agregan los productos
        if opcion == "1":
            try:
                # Se piden los datos necesarios del producto
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                # Se crea un objeto Producto con los datos ingresados
                producto = Producto(id_p, nombre, cantidad, precio)
                # Se añade al inventario (la clase Inventario valida que el ID sea único)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Error: Cantidad o precio inválido.")
        # Aquí se eliminan los productos
        elif opcion == "2":
            # Se solicita el ID del producto a eliminar
            id_p = input("Ingrese ID a eliminar: ")
            # Se llama al método que busca y elimina el producto
            inventario.eliminar_producto(id_p)
        # Aquí se actualizan los productos
        elif opcion == "3":
            # Se pide el ID del producto a modificar
            id_p = input("ID del producto: ")
            # Se permite actualizar solo cantidad o precio (o ambos).
            # Si el usuario presiona ENTER, el valor no se cambia.
            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")
            # Convertimos solo si el usuario ingresó datos
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                # Se actualizan los datos del producto
                inventario.actualizar_producto(id_p, cantidad, precio)
            except ValueError:
                print("❌ Error: Datos numéricos inválidos.")
        # Aquí se buscan los productos
        elif opcion == "4":
            # Se busca por nombre (puede encontrar coincidencias parciales)
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)
        # Aquí mostramos todos los productos existentes
        elif opcion == "5":
            inventario.mostrar_todos()
        # Aquí salimos del sistema
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        # Aquí muestra la opción inválida
        else:
            # Manejo de errores si el usuario ingresa una opción incorrecta
            print("❌ Opción inválida.")


menu()
