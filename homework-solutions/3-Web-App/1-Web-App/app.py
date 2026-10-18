"""Local assignment app. Run train.py first to produce the trusted model."""

from pathlib import Path
import pickle

from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)
# Only load the artifact generated locally by train.py; pickle can execute code.
with Path(__file__).with_name("pumpkin-model.pkl").open("rb") as stream:
    model = pickle.load(stream)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/predict")
def predict():
    try:
        month = int(request.form.get("month", ""))
        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        return render_template("index.html", error="Enter a whole month from 1 to 12."), 400
    features = pd.DataFrame({"Month": [month]})
    price = float(model.predict(features)[0])
    return render_template("index.html", month=month, prediction=f"USD {price:.2f} per bushel")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
