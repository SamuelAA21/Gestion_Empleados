from typing import List
from core.entities.usuario import Usuario
from core.repositories.usuario_repository import UsuarioRepository
from config.database import get_connection

class UsuarioRepositoryMySQL(UsuarioRepository):

    def listar(self) -> List[Usuario]:
        usuarios = []
        conn = get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, nombre, email, rol FROM usuarios")
            for row in cursor.fetchall():
                usuarios.append(
                    Usuario(
                        id=row["id"],
                        nombre=row["nombre"],
                        email=row["email"],
                        rol=row["rol"]
                    )
                )
            cursor.close()
            conn.close()
        return usuarios

    def guardar(self, usuario: Usuario) -> None:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)",
                (usuario.nombre, usuario.email, "123456", usuario.rol)  # ⚠️ contraseña fija por ahora
            )
            conn.commit()
            cursor.close()
            conn.close()
