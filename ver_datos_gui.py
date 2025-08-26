import tkinter as tk
from tkinter import ttk
import sqlite3

def mostrar_datos():
    conexion = sqlite3.connect("data/usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro")
    registros = cursor.fetchall()
    conexion.close()

    # Limpiar tabla antes de insertar nuevos
    for item in tabla.get_children():
        tabla.delete(item)

    # Insertar registros en la tabla
    for fila in registros:
        tabla.insert("", "end", values=fila)

# ----- Interfaz -----
root = tk.Tk()
root.title("Registros Guardados")
root.geometry("500x300")

# Tabla
columnas = ("ID Interno", "Nombre", "Número ID", "Teléfono")
tabla = ttk.Treeview(root, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=120)

tabla.pack(fill="both", expand=True)

# Botón actualizar
btn_actualizar = tk.Button(root, text="Actualizar datos", command=mostrar_datos, bg="blue", fg="white")
btn_actualizar.pack(pady=10)

mostrar_datos()  
root.mainloop()
