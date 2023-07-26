# BIBLIOTECAS 
from sqlalchemy import Column, Integer, String
from src.config.database import Base

class Usuario(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    nome = Column(String)
    