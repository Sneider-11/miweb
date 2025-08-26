import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------- CREAR BASE DE DATOS ----------
def crear_bd():
    conexion = sqlite3.connect("usuarios.db")  # Se crea archivo .db
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            numero_id INTEGER NOT NULL,
            telefono INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

# ---------- GUARDAR DATOS ----------
def guardar_datos():
    nombre = entry_nombre.get().strip()
    numero_id = entry_id.get().strip()
    telefono = entry_telefono.get().strip()

    # Validaciones
    if not nombre.isalpha() and " " not in nombre:
        messagebox.showerror("Error", "El nombre solo debe contener letras")
        return
    if not numero_id.isdigit():
        messagebox.showerror("Error", "El ID solo debe contener números")
        return
    if not telefono.isdigit():
        messagebox.showerror("Error", "El teléfono solo debe contener números")
        return

    # Guardar en la base de datos
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO registro (nombre, numero_id, telefono) VALUES (?, ?, ?)",
                (nombre, numero_id, telefono))
    conexion.commit()
    conexion.close()

    messagebox.showinfo("Éxito", "Datos guardados correctamente")
    entry_nombre.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

# ---------- INTERFAZ GRÁFICA ----------
root = tk.Tk()
root.title("Formulario de Registro")
root.geometry("400x300")

# Etiquetas y entradas
tk.Label(root, text="Nombre completo:").pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack()

tk.Label(root, text="Número ID:").pack(pady=5)
entry_id = tk.Entry(root, width=30)
entry_id.pack()

tk.Label(root, text="Número telefónico:").pack(pady=5)
entry_telefono = tk.Entry(root, width=30)
entry_telefono.pack()

# Botón Guardar
btn_guardar = tk.Button(root, text="Guardar", command=guardar_datos, bg="green", fg="white")
btn_guardar.pack(pady=20)

crear_bd()  # Crea la BD si no existe
root.mainloop()
