from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    distancia = None

    if request.method == "POST":
        x1 = float(request.form["x1"])
        y1 = float(request.form["y1"])
        x2 = float(request.form["x2"])
        y2 = float(request.form["y2"])

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("index.html", distancia=distancia)

if __name__ == "__main__":
    app.run(debug=True)

print("Hello world")