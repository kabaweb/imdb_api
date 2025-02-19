# Dockerfile
# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para instalar as dependências
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY imdb_api.py .

# Expor a porta que a aplicação Flask usará
EXPOSE 5001

# Definir o comando padrão para executar a aplicação
CMD ["python", "imdb_api.py"]
