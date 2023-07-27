from sqlalchemy.orm import Session 
from fastapi import Depends, APIRouter
from src.schemas import schemas
from src.models import models
from src.config.database import get_db, criar_db
from src.repositorio.repositorio import RepositorioUsuario


router = APIRouter()



@router.post('/usuario')
def criar_usuario(usuario:schemas.Usuario, session = Depends(get_db)):

    produto_criado = RepositorioUsuario(session).criar(usuario)
    return produto_criado
