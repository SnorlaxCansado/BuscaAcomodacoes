# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Para este exemplo, utilizaremos SQLite. Caso deseje usar outro banco, ajuste a URL.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Para outros bancos, a URL pode ser algo como:
# SQLALCHEMY_DATABASE_URL = "postgresql://usuario:senha@localhost/nome_banco"

# No caso do SQLite, precisamos do argumento abaixo:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos ORM
Base = declarative_base()
