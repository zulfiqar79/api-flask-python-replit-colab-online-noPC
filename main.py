from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/pokemon/<nombre>')
def get_pokemon(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Pokémon no encontrado'}), 404

    data = response.json()

    imagen_url = data['sprites']['front_default']  # puede ser None

    resultado = {
        'nombre': data['name'],
        'altura': data['height'],
        'peso': data['weight'],
        'imagen': imagen_url if imagen_url else "https://via.placeholder.com/96"
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

