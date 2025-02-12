from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Acomodacao
from faker import Faker
import random

# Garante que as tabelas estão criadas (caso ainda não existam)
Base.metadata.create_all(bind=engine)

# Instancia o Faker com a localidade para pt_BR (Brasil)
fake = Faker('pt_BR')

def gerar_acomodacao():
    """
    Gera um dicionário com dados fictícios para uma acomodação.
    """
    return {
        "nome": fake.company() + " " + fake.word().capitalize(),
        "cidade": fake.city(),
        "preco": round(random.uniform(100.0, 500.0), 2),
        "imagem_url": fake.image_url(width=640, height=480)
    }

def popular_acomodacoes(n=50):
    """
    Insere 'n' acomodações no banco de dados.
    """
    db: Session = SessionLocal()
    try:
        for _ in range(n):
            dados = gerar_acomodacao()
            acomodacao = Acomodacao(**dados)
            db.add(acomodacao)
        db.commit()
        print(f"{n} acomodações foram inseridas com sucesso!")
    except Exception as e:
        db.rollback()
        print("Ocorreu um erro durante a inserção:", e)
    finally:
        db.close()

if __name__ == "__main__":
    popular_acomodacoes(50)
