# BIBLIOTECA 
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models

# CRIANDO
class RepositorioUsuario():
    def __init__(self, session:Session):
        self.session = Session

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome = usuario.nome
        )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario
    