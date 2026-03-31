import tkinter as tk
from tkinter import messagebox

class AplicacionTareas:
    def __init__(self, ventana):
        # Configuración de nuestra ventana
        self.ventana = ventana
        self.ventana.title("Gestores de Tareas")

        # Lista donde se guardan todas las tareas
        # Estado: False = pendiente, True = completada
        self.lista_tareas = []

        # Campo de entrada
        self.entrada_tarea = tk.Entry(ventana, width=42, font=("Arial", 14))
        self.entrada_tarea.pack(pady=12)
        self.entrada_tarea.focus()  # Coloca el cursor automáticamente

        # Lista visual
        self.listbox_tareas = tk.Listbox(
            ventana, width=52, height=12, font=("Arial", 12), selectmode=tk.SINGLE
        )
        self.listbox_tareas.pack(pady=12)

        # Los botones
        frame_botones = tk.Frame(ventana)
        frame_botones.pack()

        # Botón para añadir las tareas
        tk.Button(frame_botones, text="Añadir", command=self.agregar_tarea)\
            .grid(row=0, column=0, padx=5)

        # Botón completar las tareas
        tk.Button(frame_botones, text="Completar", command=self.completar_tarea)\
            .grid(row=0, column=1, padx=5)

        # Botón eliminar las tareas
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea)\
            .grid(row=0, column=2, padx=5)

        # Atajos del teclado
        self.ventana.bind("<Return>", lambda event: self.agregar_tarea())
        self.ventana.bind("<c>", lambda event: self.completar_tarea())
        self.ventana.bind("<C>", lambda event: self.completar_tarea())
        self.ventana.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.ventana.bind("<d>", lambda event: self.eliminar_tarea())
        self.ventana.bind("<Escape>", lambda event: self.ventana.quit())

    # Funciones principales
    def agregar_tarea(self):
        """Agrega una nueva tarea a la lista"""
        texto = self.entrada_tarea.get().strip()

        # Validación: evitar tareas vacías
        if not texto:
            messagebox.showwarning("Aviso", "La tarea no debe estar en blanco")
            return

        # Se agrega como tarea pendiente (False)
        self.lista_tareas.append((texto, False))

        # Sirve para actualizar la interfaz
        self.actualizar_lista()

        # Sirve para limpiar los campos de entrada
        self.entrada_tarea.delete(0, tk.END)

    def completar_tarea(self):
        """Marca la tarea seleccionada como completada"""
        seleccion = self.listbox_tareas.curselection()

        # Sirve para verificar que haya selección
        if not seleccion:
            return

        indice = seleccion[0]
        texto, estado = self.lista_tareas[indice]

        # Cambia el estado ha completado (True)
        self.lista_tareas[indice] = (texto, True)

        # Actualiza la interfaz
        self.actualizar_lista()

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.listbox_tareas.curselection()

        # Sirve para verificar selección
        if not seleccion:
            return

        indice = seleccion[0]

        # Elimina las tareas de la lista
        del self.lista_tareas[indice]

        # Actualiza la interfaz
        self.actualizar_lista()

    def actualizar_lista(self):
        """Refresca visualmente la lista de tareas"""
        self.listbox_tareas.delete(0, tk.END)

        # Recorre todas las tareas y las muestra
        for i, (texto, completada) in enumerate(self.lista_tareas):

            if completada:
                # Tarea completada (gris con check)
                self.listbox_tareas.insert(tk.END, f"✔ {texto}")
                self.listbox_tareas.itemconfig(i, fg="gray")
            else:
                # Tarea pendiente (negro con cruz)
                self.listbox_tareas.insert(tk.END, f"✗ {texto}")
                self.listbox_tareas.itemconfig(i, fg="black")


# Programa principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionTareas(ventana)
    ventana.mainloop()