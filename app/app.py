from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app) 

# Load model and vectorizer
model = joblib.load("ai_model/model.pkl")
vectorizer = joblib.load("ai_model/vectorizer.pkl")

@app.route("/")
def home():
    return jsonify({"message": "Customer Query Classifier API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    X_new = vectorizer.transform([query])
    prediction = model.predict(X_new)[0]
    return jsonify({"query": query, "category": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
