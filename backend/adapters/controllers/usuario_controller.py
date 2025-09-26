from fastapi import APIRouter
from backend.core.entities.usuario import Usuario
from backend.core.services.usuario_service import UsuarioService
from adapters.persistence.usuario_repository_mysql import UsuarioRepositoryMySQL

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

service = UsuarioService(UsuarioRepositoryMySQL())

@router.get("/")
def listar_usuarios():
    return [u.__dict__ for u in service.obtener_usuarios()]
