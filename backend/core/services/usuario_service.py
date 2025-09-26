from typing import List
from backend.core.entities.usuario import Usuario
from backend.core.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    """Servicio de negocio para la gestión de usuarios."""

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def obtener_usuarios(self) -> List[Usuario]:
        """Listar todos los usuarios"""
        return self.repository.listar()

    def crear_usuario(self, usuario: Usuario) -> None:
        """Crear un nuevo usuario (ejemplo: aquí podrías validar reglas de negocio)"""
        # Aquí podrías agregar validaciones, ej: que el email no esté duplicado
        self.repository.guardar(usuario)

    def obtener_usuario(self, id: int) -> Usuario | None:
        """Buscar usuario por ID"""
        return self.repository.buscar_por_id(id)

    def eliminar_usuario(self, id: int) -> None:
        """Eliminar usuario"""
        self.repository.eliminar(id)
