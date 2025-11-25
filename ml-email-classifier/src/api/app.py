from flask import Flask, request, jsonify
import joblib
from src.basic_text_playground import clean_text, summarize_email
from pathlib import Path
import nltk
from nltk.corpus import stopwords

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


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    summary = summarize_email(text)

    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)
