from abc import ABC, abstractmethod
from typing import List
from backend.core.entities.usuario import Usuario

class UsuarioRepository(ABC):
    """Interfaz de repositorio para la entidad Usuario."""

    @abstractmethod
    def listar(self) -> List[Usuario]:
        """Listar todos los usuarios"""
        pass

    @abstractmethod
    def guardar(self, usuario: Usuario) -> None:
        """Guardar un nuevo usuario"""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Usuario | None:
        """Buscar usuario por ID"""
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        """Eliminar usuario por ID"""
        pass
