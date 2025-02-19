# imdb_api.py
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para buscar o código IMDb usando scraping
def buscar_codigo_imdb(titulo_filme):
    try:
        query = "+".join(titulo_filme.split())
        url = f"https://www.imdb.com/find?q={query}&s=tt"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.30>
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('li', class_='ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result->
        if result:
            link = result.find('a', href=True)
            if link:
                imdb_id = link['href'].split('/')[2]
                print(f"Código IMDb encontrado: {imdb_id} para o título {titulo_filme}")
                return imdb_id
        else:
            print(f"Nenhum resultado encontrado para: {titulo_filme}")
            return None
    except Exception as e:
        print(f"Erro ao buscar código IMDb: {e}")
        return None

# Rota para buscar o código IMDb com base no nome do filme
@app.route('/buscar_imdb', methods=['GET'])
def buscar_imdb():
    titulo = request.args.get('titulo')
    if not titulo:
        return jsonify({"error": "Parâmetro 'titulo' é necessário"}), 400

    imdb_id = buscar_codigo_imdb(titulo)
    if imdb_id:
        return jsonify({"titulo": titulo, "imdb_id": imdb_id})
    else:
        return jsonify({"error": "Filme não encontrado ou erro no scraping"}), 404

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
