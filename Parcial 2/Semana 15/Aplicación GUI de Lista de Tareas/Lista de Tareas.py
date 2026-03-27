import tkinter as tk
from tkinter import messagebox
# Se define una clase para organizar mejor el código
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de las Tareas")

        # Lista interna sirve para guardar las tareas
        self.tareas = []

        # Permite al usuario escribir nuevas tareas
        self.entry = tk.Entry(root, width=45)
        self.entry.pack(pady=12)
        # Se vincula la tecla Enter con la función agregar_tarea
        self.entry.bind("<Return>", self.agregar_tarea_evento)  # Enter

        # Listbox para mostrar todas las tareas
        self.lista = tk.Listbox(root, width=55, height=12)
        self.lista.pack(pady=12)

        # Evento opcional: doble clic para completar
        self.lista.bind("<Double-Button-1>", self.marcar_completada_evento)

        # Se usa un Frame para organizar mejor los botones
        frame_botones = tk.Frame(root)
        frame_botones.pack()
        # Botón para añadir tarea
        tk.Button(frame_botones, text="Añadir Tareas", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        # Botón para marcar tarea como completada
        tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada).grid(row=0, column=1, padx=5)
        # Botón para eliminar tarea
        tk.Button(frame_botones, text="Eliminar Tareas", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

    # Funciones principales
    def agregar_tarea(self):
        """Función que añade una nueva tarea a la lista.
           Se ejecuta al presionar el botón o la tecla Enter.
        """
        texto = self.entry.get().strip()
        # Validación: evita agregar tareas vacías
        if texto == "":
            messagebox.showwarning("Advertencia", "Escribe una tarea")
            return
        # Se agrega la tarea con estado inicial "no completada"
        self.tareas.append({"texto": texto, "completada": False})
        # Se actualiza la interfaz gráfica
        self.actualizar_lista()
        # Se limpia el campo de entrada
        self.entry.delete(0, tk.END)


    def agregar_tarea_evento(self, event):
        """ Manejador de evento para la tecla Enter.
            Recibe el evento automáticamente, pero reutiliza la lógica principal.
        """
        self.agregar_tarea()

    def marcar_completada(self):
        """
            Marca una tarea seleccionada como completada.
        """
        seleccion = self.lista.curselection()
        # Validación: verificar que haya selección
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = seleccion[0]
        # Se cambia el estado de la tarea a completada
        self.tareas[index]["completada"] = True
        # Se actualiza la vista
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        """
            Evento de doble clic sobre una tarea.
            Permite una interacción más rápida.
        """
        self.marcar_completada()

    def eliminar_tarea(self):
        """
            Elimina la tarea seleccionada de la lista.
        """
        seleccion = self.lista.curselection()
        # Validación: verificar selección
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = seleccion[0]
        # Se elimina la tarea de la lista interna
        del self.tareas[index]
        # Se actualiza la interfaz
        self.actualizar_lista()

    def actualizar_lista(self):
        """
            Refresca el contenido del Listbox para reflejar el estado actual
            de las tareas.
        """
        # Se limpia la lista visual
        self.lista.delete(0, tk.END)
        # Se recorre la lista interna y se muestra cada tarea
        for tarea in self.tareas:
            if tarea["completada"]:
                # Se muestra con un símbolo de completado
                self.lista.insert(tk.END, f"✔ {tarea['texto']}")
            else:
                # Se muestra como pendiente
                self.lista.insert(tk.END, f"✗ {tarea['texto']}")

# Ejecución del programa
if __name__ == "__main__":
    # Se crea la ventana principal
    root = tk.Tk()
    # Se instancia la aplicación
    app = ListaTareasApp(root)
    # Bucle principal de eventos
    root.mainloop()