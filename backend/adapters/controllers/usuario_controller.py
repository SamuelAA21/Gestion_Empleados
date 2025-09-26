from fastapi import APIRouter
from core.services.usuario_service import UsuarioService
from adapters.persistence.usuario_repository_mysql import UsuarioRepositoryMySQL

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

service = UsuarioService(UsuarioRepositoryMySQL())

@router.get("/")
def listar_usuarios():
    return [u.__dict__ for u in service.obtener_usuarios()]
