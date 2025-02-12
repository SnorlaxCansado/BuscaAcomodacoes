# Dockerfile para o front-end (React)
FROM node:18-alpine

WORKDIR /app

# Copia os arquivos de package e instala as dependências
COPY package.json package-lock.json ./
RUN npm install

# Copia o restante do código
COPY . .

EXPOSE 5173

# Comando para ambiente de desenvolvimento
CMD ["npm", "run", "dev"]

