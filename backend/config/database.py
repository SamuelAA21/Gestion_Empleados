import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",   # o "localhost"
            user="root",       # tu usuario de MySQL
            password="",       # tu password si tiene
            database="gestio_empleados"  # el nombre de tu BD en phpMyAdmin
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
