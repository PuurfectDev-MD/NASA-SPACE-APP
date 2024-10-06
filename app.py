

from flask import Flask, render_template
from exoplanet_data import exoplanets

app = Flask(__name__)


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
