import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Clase principal
class Agenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("650x450")

        # Lista interna para almacenar eventos
        self.eventos = []

        # Tabla de eventos

        frame_tabla = tk.Frame(root)
        frame_tabla.pack(pady=10)

        # Tabla (TreeView)
        self.tabla = ttk.Treeview(frame_tabla, columns=("Fecha", "Hora", "Evento"), show="headings")

        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Hora", text="Hora")
        self.tabla.heading("Evento", text="Evento")

        self.tabla.column("Fecha", width=100)
        self.tabla.column("Hora", width=80)
        self.tabla.column("Evento", width=250)

        self.tabla.pack()

        # Formulario

        frame_form = tk.LabelFrame(root, text="Nuevo Evento")
        frame_form.pack(pady=10, padx=10, fill="x")

        # Fecha
        tk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha = DateEntry(frame_form, date_pattern="yyyy-mm-dd")
        self.fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_form, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.hora = tk.Entry(frame_form)
        self.hora.grid(row=1, column=1, padx=5, pady=5)

        # Evento
        tk.Label(frame_form, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.evento = tk.Entry(frame_form, width=40)
        self.evento.grid(row=2, column=1, padx=5, pady=5)

        # Botones

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Guardar", command=self.guardar_evento).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_evento).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=2, padx=10)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=3, padx=10)

    # Valida el formato de hora
    def validar_hora(self, hora):
        try:
            partes = hora.split(":")
            if len(partes) != 2:
                return False
            h, m = int(partes[0]), int(partes[1])
            return 0 <= h < 24 and 0 <= m < 60
        except:
            return False

    # Guardar los eventos
    def guardar_evento(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        evento = self.evento.get()

        # Validaciones
        if not fecha or not hora or not evento:
            messagebox.showwarning("Error", "Complete todos los campos")
            return

        if not self.validar_hora(hora):
            messagebox.showerror("Error", "Formato de hora inválido (HH:MM)")
            return

        # Guardar en lista
        self.eventos.append((fecha, hora, evento))

        # Actualiza la tabla
        self.actualizar_tabla()

        # Limpiar los campos
        self.limpiar_campos()

    # Actualiza la tabla de eventos
    def actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar datos actualizados
        for ev in self.eventos:
            self.tabla.insert("", "end", values=ev)

    # Elimina los eventos
    def eliminar_evento(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un evento")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmar:
            item = self.tabla.item(seleccion)
            valores = item["values"]

            # Eliminar de la lista
            self.eventos.remove(tuple(valores))

            # Actualiza la tabla
            self.actualizar_tabla()

    # Limpia los campos

    def limpiar_campos(self):
        self.hora.delete(0, tk.END)
        self.evento.delete(0, tk.END)

# Ejecuta el programa
if __name__ == "__main__":
    root = tk.Tk()
    app = Agenda(root)
    root.mainloop()