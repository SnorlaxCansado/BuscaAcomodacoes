# app/models.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Acomodacao(Base):
    __tablename__ = "acomodacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    cidade = Column(String, index=True, nullable=False)
    preco = Column(Float, nullable=False)
    imagem_url = Column(String, nullable=False)
