
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pokemon")
def obtener_pokemon_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    response = requests.get(url)
    data = response.json()
    imagen = data["sprites"]["front_default"]
    return jsonify({
        "nombre": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "imagen": imagen,
        "habilidades": [h["ability"]["name"] for h in data["abilities"]]
    })

@app.route("/pokemon/<nombre>")
def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "nombre": data["name"],
            "altura": data["height"],
            "peso": data["weight"]
        })
    else:
        return jsonify({"error": "Pokémon no encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
