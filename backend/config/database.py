import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",   # o localhost
            user="root",        # tu usuario de MySQL
            password="",        # tu contraseña (si la tenés configurada)
            database="gestion_empleados",
            port=3306           # cambia a 3307 si tu MySQL corre ahí
        )
        return connection
    except Error as e:
        print("❌ Error al conectar a MySQL:", e)
        return None
