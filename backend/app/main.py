# app/main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import accommodations
from app.database import engine, Base
from app import models

# Cria as tabelas no banco de dados (caso ainda não existam)
Base.metadata.create_all(bind=engine)

# Instância do FastAPI
app = FastAPI(title="API de Acomodações")

# Defina as origens que poderão acessar este back-end.
# Ajuste conforme necessário; se estiver usando localhost, inclua as portas.
# Exemplo: http://localhost:5173 e/ou http://127.0.0.1:5173
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Se você estiver usando Docker Compose
    # e quiser liberar para outras origens, adicione aqui.
    # Exemplo: "http://localhost:3000" etc.
]

# Configura o CORS Middleware para inserir os cabeçalhos de CORS nas respostas.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # ou ["*"] para liberar geral (não recomendado em produção)
    allow_credentials=True,
    allow_methods=["*"],        # ou especifique ["GET", "POST", "PUT", "DELETE"]
    allow_headers=["*"],        # Autoriza todos os cabeçalhos
)

# Rotas
app.include_router(accommodations.router, prefix="/acomodacoes", tags=["Acomodações"])

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Acomodações"}
