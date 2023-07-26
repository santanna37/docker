from pydantic import BaseModel
from typing import Optional


#tabalas 
class Usuario(BaseModel):
    id: int 
    nome: str