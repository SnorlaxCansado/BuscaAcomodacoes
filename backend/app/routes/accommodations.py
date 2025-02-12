# app/routes/accommodations.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Acomodacao])
async def read_acomodacoes(cidade: Optional[str] = Query(None, description="Filtrar por cidade"), db: Session = Depends(get_db)):
    acomodacoes = crud.get_acomodacoes(db, cidade)
    return acomodacoes

@router.get("/{id}", response_model=schemas.Acomodacao)
async def read_acomodacao(id: int, db: Session = Depends(get_db)):
    db_acomodacao = crud.get_acomodacao(db, id)
    if not db_acomodacao:
        raise HTTPException(status_code=404, detail="Acomodação não encontrada")
    return db_acomodacao

@router.post("/", response_model=schemas.Acomodacao, status_code=201)
async def create_acomodacao(acomodacao: schemas.AcomodacaoBase, db: Session = Depends(get_db)):
    return crud.create_acomodacao(db, acomodacao)

@router.put("/{id}", response_model=schemas.Acomodacao)
async def update_acomodacao(id: int, acomodacao: schemas.AcomodacaoBase, db: Session = Depends(get_db)):
    db_acomodacao = crud.update_acomodacao(db, id, acomodacao)
    if not db_acomodacao:
        raise HTTPException(status_code=404, detail="Acomodação não encontrada")
    return db_acomodacao

@router.delete("/{id}", response_model=schemas.Acomodacao)
async def delete_acomodacao(id: int, db: Session = Depends(get_db)):
    db_acomodacao = crud.delete_acomodacao(db, id)
    if not db_acomodacao:
        raise HTTPException(status_code=404, detail="Acomodação não encontrada")
    return db_acomodacao
