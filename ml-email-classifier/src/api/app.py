from flask import Flask, request, jsonify
import joblib
from src.basic_text_playground import clean_text
from pathlib import Path

app = Flask(__name__)

vectorizer = joblib.load(Path(__file__).parent.parent.parent /
                         "models" / "vectorizer.pkl")
model = joblib.load(Path(__file__).parent.parent.parent /
                    "models" / "classifier.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]
    cleaned_text = clean_text(text)
    X = vectorizer.transform([cleaned_text])
    pred = model.predict(X)

    return jsonify(pred[0])


if __name__ == "__main__":
    app.run(debug=True)
