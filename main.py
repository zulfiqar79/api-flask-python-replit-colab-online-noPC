from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    pokemon = None
    if request.method == 'POST':
        name = request.form.get('pokemon_name').lower()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        if response.ok:
            data = response.json()
            pokemon = {
                'nombre': data['name'],
                'altura': data['height'],
                'peso': data['weight'],
                'imagen': data['sprites']['front_default']  # URL de la imagen
            }
        else:
            pokemon = {'error': 'Pokémon no encontrado'}
    return render_template('index.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)

