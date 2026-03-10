# Se procede a importar la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# Todas las funciones de la aplicación GUI Básica

def agregar_dato():
    """
    Esta función se ejecuta cuando el usuario presiona el botón 'Agregar'.
    """
    dato = entrada_texto.get()

    if dato != "":
        lista_datos.insert(tk.END, dato)  # Se agrega el dato a la lista
        entrada_texto.delete(0, tk.END)   # Se limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato primero")


def limpiar_lista():
    """
    Esta función elimina todos los elementos de la lista.
    """
    lista_datos.delete(0, tk.END)

# Ventana principal

ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("420x360")  # Tamaño de la ventana GUI

# Componentes de interfaz

# Etiquetas
label = tk.Label(ventana, text="Ingrese los datos:", font=("Times New Roman", 14))
label.pack(pady=12)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=35)
entrada_texto.pack(pady=7)

# Este es el botón para agregar datos en la aplicación
boton_agregar = tk.Button(
    ventana,
    text="Agregar",
    command=agregar_dato,
    bg="blue",
    fg="black",
    width=18
)
boton_agregar.pack(pady=7)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=35, height=8)
lista_datos.pack(pady=12)

# Este es el botón para limpiar datos
boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar_lista,
    bg="red",
    fg="black",
    width=18
)
boton_limpiar.pack(pady=7)

# Se ejecuta la aplicación

ventana.mainloop()