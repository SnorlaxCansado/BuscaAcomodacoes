# create_tables.py
from app.database import engine, Base
from app import models

# Cria todas as tabelas definidas nos modelos
Base.metadata.create_all(bind=engine)
