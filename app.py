# this is snadaru's branch

from flask import Flask, render_template

app = Flask(__name__)

# Data for exoplanets
exoplanets = [
    {
        "name": "55 Cancri e",
        "image": "/static/Nasa data/55 Cancri e/55 Cancri e pic1.jpg",
        "size": "1.9 Earth radii",
        "distance": "41 light-years",
        "description": "A planet orbiting extremely close to its star, possibly covered in lava.",
        "id": "55-cancri-e"
    },
    {
        "name": "Earth-like Exoplanet",
        "image": "/static/images/earth.jpg",
        "size": "1 Earth radius",
        "distance": "100 light-years",
        "description": "A potentially habitable exoplanet with Earth-like conditions.",
        "id": "earth-like-exoplanet"
    },
        {
        "name": "Earth-like Exoplanet",
        "image": "/static/images/earth.jpg",
        "size": "1 Earth radius",
        "distance": "100 light-years",
        "description": "A potentially habitable exoplanet with Earth-like conditions.",
        "id": "earth-like-exoplanet"
    },
        {
        "name": "Earth-like Exoplanet",
        "image": "/static/images/earth.jpg",
        "size": "1 Earth radius",
        "distance": "100 light-years",
        "description": "A potentially habitable exoplanet with Earth-like conditions.",
        "id": "earth-like-exoplanet"
    },
        {
        "name": "Earth-like Exoplanet",
        "image": "/static/images/earth.jpg",
        "size": "1 Earth radius",
        "distance": "100 light-years",
        "description": "A potentially habitable exoplanet with Earth-like conditions.",
        "id": "earth-like-exoplanet"
    },
        {
        "name": "Earth-like Exoplanet",
        "image": "/static/images/earth.jpg",
        "size": "1 Earth radius",
        "distance": "100 light-years",
        "description": "A potentially habitable exoplanet with Earth-like conditions.",
        "id": "earth-like-exoplanet"
    }
    # Add more exoplanet data here...
]

@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/explore")
def explore():
    return render_template("explorepg.html")

@app.route("/exo")
def exo():
    # Pass the exoplanets data to the template
    return render_template("exoplanet.html", exoplanets=exoplanets)

@app.route("/exoplanet/<id>")
def exoplanet_detail(id):
    # Find the exoplanet by its ID
    exoplanet = next((planet for planet in exoplanets if planet["id"] == id), None)
    if exoplanet:
        return render_template("exoplanet_detail.html", exoplanet=exoplanet)
    else:
        return "Exoplanet not found", 404

if __name__ == "__main__":
    app.run(debug=True)
