from flask import Flask, request, render_template, jsonify
import pickle
import os

app = Flask(__name__)

# Load model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

# 🔹 UI ROUTE (HTML PAGE)
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        msg = request.form["message"]
        pred = model.predict([msg])[0]
        prediction = "Spam" if pred == 1 else "Ham"
    return render_template("index.html", prediction=prediction)

# 🔹 REST API ROUTE
@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "JSON must contain 'message'"}), 400

    message = data["message"]
    pred = model.predict([message])[0]

    return jsonify({
        "message": message,
        "prediction": "Spam" if pred == 1 else "Ham"
    })

if __name__ == "__main__":
    app.run(debug=True)