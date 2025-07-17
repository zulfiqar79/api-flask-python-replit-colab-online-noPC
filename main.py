from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/pokemon/<nombre>')
def get_pokemon(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Pokémon no encontrado'}), 404

    data = response.json()
    resultado = {
        'nombre': data['name'],
        'altura': data['height'],
        'peso': data['weight'],
        'imagen': data['sprites']['front_default']  # URL de imagen frontal
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

