import mysql.connector
from mysql.connector import Error
from fastapi import APIRouter

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",   # o "localhost"
            user="root",       # tu usuario de MySQL
            password="",       # tu password si tiene
            database="gestio_empleados"  # tu BD creada en phpMyAdmin
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


# aquí creamos el router
router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

# ruta de prueba
@router.get("/")
def listar_usuarios():
    return {"mensaje": "Aquí iría la lista de usuarios"}
