# app/schemas.py
from pydantic import BaseModel

class AcomodacaoBase(BaseModel):
    nome: str
    cidade: str
    preco: float
    imagem_url: str

class Acomodacao(AcomodacaoBase):
    id: int

    class Config:
        from_attributes = True

