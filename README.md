# Busca de Acomodações para Locação de Temporada

Este projeto é um **case de teste** desenvolvido para uma vaga de **Junior Fullstack Developer**. Ele consiste em uma aplicação web que permite buscar acomodações para locação de temporada, utilizando:

- **Back-end:** FastAPI com SQLAlchemy e SQLite.
- **Front-end:** React com TailwindCSS para o estilo.
- **Containerização:** Docker e Docker Compose para facilitar a execução e deploy do ambiente.

---

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
  - [Pré-requisitos](#pré-requisitos)
  - [Setup Local (sem Docker)](#setup-local-sem-docker)
  - [Executando com Docker Compose](#executando-com-docker-compose)
- [Utilização da API](#utilização-da-api)
- [Atualização da Base de Dados](#atualização-da-base-de-dados)
- [Boas Práticas e Considerações](#boas-práticas-e-considerações)
- [Conclusão](#conclusão)

---

## Funcionalidades

- **Busca de acomodações:** Permite filtrar as acomodações por cidade.
- **Detalhes da acomodação:** Visualização dos detalhes (nome, cidade, preço e imagem) de cada acomodação.
- **Favoritar acomodações:** Possibilidade de marcar acomodações como favoritas, armazenadas no `localStorage` do navegador.
- **Documentação automática da API:** A documentação dos endpoints está disponível automaticamente via Swagger (/docs) e Redoc (/redoc).

---

## Tecnologias Utilizadas

### Back-end
- **Python 3.9+**
- **FastAPI** – Framework web moderno e rápido.
- **SQLAlchemy** – ORM para gerenciamento do banco de dados.
- **SQLite** – Banco de dados simples para desenvolvimento.
- **Docker** – Para containerização e isolamento do ambiente.

### Front-end
- **React** – Biblioteca JavaScript para construção da interface.
- **TailwindCSS** – Framework CSS utilitário para estilização rápida e responsiva.
- **Axios** – Cliente HTTP para realizar chamadas à API.
- **Vite** – Ferramenta de build e desenvolvimento.

### DevOps / Deploy
- **Docker Compose** – Para orquestrar os containers de back-end e front-end.

---

## Estrutura do Projeto

O repositório está organizado em dois diretórios principais:

BuscaAcomodacoes/
├── backend/         # Back-end com FastAPI
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Ponto de entrada da API FastAPI
│   │   ├── config.py            # Configurações gerais (variáveis de ambiente)
│   │   ├── models.py            # Modelos de dados (SQLAlchemy)
│   │   ├── schemas.py           # Schemas Pydantic
│   │   ├── crud.py              # Operações CRUD
│   │   ├── database.py          # Configuração do banco de dados (SQLite)
│   │   ├── populate_data.py     # Script para popular a base com dados fictícios
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── accommodations.py  # Endpoints relacionados a acomodações
│   ├── requirements.txt         # Dependências Python
│   └── Dockerfile               # Dockerfile do back-end
├── frontend/        # Front-end com React e TailwindCSS
│   ├── public/
│   │   └── index.html           # Ponto de entrada HTML
│   ├── src/
│   │   ├── assets/              # Assets (imagens, fontes, etc.)
│   │   ├── components/          # Componentes React reutilizáveis
│   │   │   ├── AccommodationCard.jsx
│   │   │   ├── FavoriteButton.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Layout.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── SearchBar.jsx
│   │   ├── pages/               # Páginas da aplicação
│   │   │   ├── Home.jsx
│   │   │   ├── Favorites.jsx
│   │   │   └── AccommodationDetails.jsx
│   │   ├── services/            # Chamadas à API
│   │   │   └── api.js
│   │   ├── App.jsx              # Componente raiz
│   │   ├── App.css
│   │   ├── index.css            # Importação do TailwindCSS
│   │   └── main.jsx             # Ponto de entrada do React
│   ├── package.json             # Dependências Node.js
│   ├── tailwind.config.js       # Configuração do TailwindCSS
│   ├── postcss.config.js        # Configuração do PostCSS
│   ├── vite.config.js           # Configuração do Vite
│   └── Dockerfile               # Dockerfile do front-end
└── docker-compose.yml           # Arquivo para subir ambos os containers

---

## Instalação e Configuração

### Pré-requisitos

- VSCode com WSL configurado (opcional, mas recomendado para ambiente Windows).
- Python 3.9+
- Node.js (versão LTS)
- Docker e Docker Compose

### Setup Local (Sem Docker)

#### Back-end

1. Navegue até a pasta `backend/`:
   ```bash
   cd backend
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie as tabelas no banco de dados (caso ainda não existam):
   ```bash
   python app/create_tables.py
   ```
5. Para popular a base com dados fictícios (50 entradas):
   ```bash
   python app/populate_data.py
   ```
6. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
7. Acesse a API em [http://localhost:8000/](http://localhost:8000/) e a documentação em [http://localhost:8000/docs](http://localhost:8000/docs).

#### Front-end

1. Navegue até a pasta `frontend/`:
   ```bash
   cd frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```
4. Acesse a aplicação em [http://localhost:5173/](http://localhost:5173/).

### Executando com Docker Compose

Na raiz do repositório, verifique se os arquivos Dockerfile (em `backend/` e `frontend/`) e o **docker-compose.yml** estão configurados corretamente.

Execute:

```bash
docker-compose up --build
```

- O back-end ficará acessível em [http://localhost:8000/](http://localhost:8000/).
- O front-end ficará acessível em [http://localhost:5173/](http://localhost:5173/).

---

## Utilização da API

A API possui os seguintes endpoints (documentação automática disponível em `/docs` e `/redoc`):

- **GET /**  
  Rota raiz que retorna uma mensagem de boas-vindas.

- **GET /acomodacoes**  
  Retorna uma lista de acomodações. É possível filtrar por cidade usando o parâmetro `cidade`.

- **GET /acomodacoes/{id}**  
  Retorna os detalhes de uma acomodação específica pelo `id`.

- **POST /acomodacoes**  
  Cria uma nova acomodação. O corpo da requisição deve seguir o modelo `AcomodacaoBase`.

- **PUT /acomodacoes/{id}**  
  Atualiza uma acomodação existente com os dados fornecidos.

- **DELETE /acomodacoes/{id}**  
  Remove uma acomodação da base de dados.

---
## Boas Práticas e Considerações

- **Organização do Código:**  
  O projeto está dividido em duas áreas principais: `backend/` e `frontend/`, o que facilita a manutenção e escalabilidade.

- **Documentação Automática:**  
  O FastAPI gera documentação automática dos endpoints (Swagger em `/docs` e Redoc em `/redoc`).

- **Testabilidade:**  
  A estrutura modular do back-end (rotas, CRUD, modelos) facilita a criação de testes unitários e de integração. No front-end, recomenda-se utilizar ferramentas como Jest e React Testing Library para testar componentes críticos.

- **Containerização com Docker:**  
  O uso de Docker e Docker Compose garante um ambiente consistente, simplifica a implantação e demonstra profissionalismo.

---

## Conclusão

Este case foi desenvolvido com foco em boas práticas, organização e escalabilidade, demonstrando conhecimento tanto em back-end quanto em front-end. Sinta-se à vontade para explorar os arquivos, realizar os testes e verificar a documentação gerada automaticamente pela FastAPI em `/docs`.

*Desenvolvido por Gabriel T. H. S. Santos*
```