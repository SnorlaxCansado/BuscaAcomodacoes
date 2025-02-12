# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_acomodacoes(db: Session, cidade: str = None):
    """
    Retorna todas as acomodações ou filtra por cidade se informado.
    """
    query = db.query(models.Acomodacao)
    if cidade:
        # ilike permite busca case-insensitive
        query = query.filter(models.Acomodacao.cidade.ilike(f"%{cidade}%"))
    return query.all()

def get_acomodacao(db: Session, acomodacao_id: int):
    """
    Retorna uma única acomodação pelo ID.
    """
    return db.query(models.Acomodacao).filter(models.Acomodacao.id == acomodacao_id).first()

def create_acomodacao(db: Session, acomodacao: schemas.AcomodacaoBase):
    """
    Cria uma nova acomodação.
    """
    db_acomodacao = models.Acomodacao(**acomodacao.dict())
    db.add(db_acomodacao)
    db.commit()
    db.refresh(db_acomodacao)
    return db_acomodacao

def update_acomodacao(db: Session, acomodacao_id: int, acomodacao: schemas.AcomodacaoBase):
    """
    Atualiza uma acomodação existente.
    """
    db_acomodacao = get_acomodacao(db, acomodacao_id)
    if not db_acomodacao:
        return None
    for key, value in acomodacao.dict().items():
        setattr(db_acomodacao, key, value)
    db.commit()
    db.refresh(db_acomodacao)
    return db_acomodacao

def delete_acomodacao(db: Session, acomodacao_id: int):
    """
    Remove uma acomodação do banco de dados.
    """
    db_acomodacao = get_acomodacao(db, acomodacao_id)
    if db_acomodacao:
        db.delete(db_acomodacao)
        db.commit()
    return db_acomodacao
