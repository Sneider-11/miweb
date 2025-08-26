import sqlite3

def ver_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM registro")
    registros = cursor.fetchall()

    print("📋 Datos guardados en la base de datos:\n")
    for fila in registros:
        print(f"ID Interno: {fila[0]} | Nombre: {fila[1]} | Número ID: {fila[2]} | Teléfono: {fila[3]}")

    conexion.close()

if __name__ == "__main__":
    ver_datos()
