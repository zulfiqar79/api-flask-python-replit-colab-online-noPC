from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None
    error = None

    if request.method == "POST":
        nombre = request.form["nombre"].lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            pokemon_data = {
                "nombre": datos["name"].capitalize(),
                "imagen": datos["sprites"]["front_default"],
                "tipo": datos["types"][0]["type"]["name"].capitalize()
            }
        else:
            error = "Pokémon no encontrado. Revisá el nombre."

    return render_template("index.html", pokemon=pokemon_data, error=error)
