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

            # Obtener imagen o mostrar placeholder si falta
            imagen = datos["sprites"]["front_default"]
            if not imagen:
                imagen = "https://via.placeholder.com/150?text=Sin+imagen"

            # 🔍 Mostrar en consola la URL de la imagen
            print("URL de imagen:", imagen)

            pokemon_data = {
                "nombre": datos["name"].capitalize(),
                "imagen": imagen,
                "tipo": datos["types"][0]["type"]["name"].capitalize()
            }
        else:
            error = "Pokémon no encontrado. Revisá el nombre."

    return render_template("index.html", pokemon=pokemon_data, error=error)

if __name__ == "__main__":
    app.run()
