from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_risk

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    source = data.get("source")
    destination = data.get("destination")
    cargo = data.get("cargo", "normal")
    weather = data.get("weather")
    congestion = data.get("congestion")

    risk, level, distance, weather, congestion = predict_risk(
        source,
        destination,
        cargo,
        weather,
        congestion
    )

    return jsonify({
        "distance": distance,
        "weather": weather,
        "congestion": congestion,
        "cargo": cargo,
        "risk_score": risk,
        "risk_level": level
    })


if __name__ == "__main__":
    app.run(debug=True)