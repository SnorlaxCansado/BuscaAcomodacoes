# app/set_images_placeholder.py
from app.database import SessionLocal
from app.models import Acomodacao

def set_placeholder_image():
    db = SessionLocal()
    try:
        # Define aqui a URL da imagem que você deseja usar
        nova_url = "https://img.freepik.com/fotos-gratis/um-quarto-tranquilo-com-cores-bege-e-design-simples_157027-4426.jpg?t=st=1739283231~exp=1739286831~hmac=867377e67fc574c1e60a6bc70aeb3fb8891729c60d9c464aa08aad86682c25f1&w=1380"

        acomodacoes = db.query(Acomodacao).all()

        for acomodacao in acomodacoes:
            acomodacao.imagem_url = nova_url

        db.commit()
        print("Imagens atualizadas com sucesso!")
    except Exception as e:
        db.rollback()
        print("Erro ao atualizar imagens:", e)
    finally:
        db.close()

if __name__ == "__main__":
    set_placeholder_image()
