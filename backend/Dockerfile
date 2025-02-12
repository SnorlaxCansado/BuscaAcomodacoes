# Dockerfile para o back-end (FastAPI)
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências e instala os pacotes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o container
COPY . .

# Exponha a porta em que a API irá rodar
EXPOSE 8000

# Comando para iniciar o Uvicorn (servidor ASGI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
