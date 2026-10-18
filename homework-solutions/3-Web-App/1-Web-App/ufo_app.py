"""UFO lesson exercise and local, synchronous training-route challenge."""

from pathlib import Path

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler


FEATURES = ["Seconds", "Latitude", "Longitude"]
DATASET = Path(__file__).resolve().parents[3] / "3-Web-App/1-Web-App/data/ufos.csv"
COUNTRIES = {"au": "Australia", "ca": "Canada", "de": "Germany", "gb": "UK", "us": "US"}


def clean_data(raw):
    rows = raw.rename(columns={
        "duration (seconds)": "Seconds", "latitude": "Latitude",
        "longitude": "Longitude", "country": "Country",
    })[FEATURES + ["Country"]].copy()
    for column in FEATURES:
        rows[column] = pd.to_numeric(rows[column], errors="coerce")
    return rows.loc[
        rows["Seconds"].between(1, 60)
        & rows["Latitude"].between(-90, 90)
        & rows["Longitude"].between(-180, 180)
        & rows["Country"].isin(COUNTRIES)
    ].copy()


def train_model():
    rows = clean_data(pd.read_csv(DATASET))
    X_train, X_test, y_train, y_test = train_test_split(
        rows[FEATURES], rows["Country"], test_size=0.2,
        random_state=0, stratify=rows["Country"],
    )
    encoder = LabelEncoder().fit(y_train)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    model.fit(X_train, encoder.transform(y_train))
    predicted = encoder.inverse_transform(model.predict(X_test))
    metrics = {
        "rows": len(rows), "train_rows": len(X_train), "test_rows": len(X_test),
        "accuracy": accuracy_score(y_test, predicted),
        "macro_f1": f1_score(y_test, predicted, average="macro"),
        "majority_accuracy": float((y_test == y_train.mode()[0]).mean()),
    }
    return model, encoder, metrics, X_test, y_test, predicted


def create_app():
    app = Flask(__name__)
    app.config["UFO_MODEL"] = None

    @app.get("/")
    def home():
        return render_template("ufo.html")

    @app.post("/train")
    def train():
        model, encoder, metrics, *_ = train_model()
        # shortcut: process-local model, use a versioned model store for multiple workers.
        app.config["UFO_MODEL"] = (model, encoder)
        return render_template("ufo.html", metrics=metrics)

    @app.post("/predict")
    def predict():
        try:
            values = [float(request.form.get(name, ""))
                      for name in ("seconds", "latitude", "longitude")]
            if not (np.isfinite(values).all() and 1 <= values[0] <= 60
                    and -90 <= values[1] <= 90 and -180 <= values[2] <= 180):
                raise ValueError
        except ValueError:
            return render_template("ufo.html", error="Enter valid duration and coordinates."), 400
        fitted = app.config["UFO_MODEL"]
        if fitted is None:
            return render_template("ufo.html", error="Train the model first."), 503
        model, encoder = fitted
        code = encoder.inverse_transform(model.predict(pd.DataFrame([values], columns=FEATURES)))[0]
        return render_template("ufo.html", prediction=COUNTRIES[code])

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5001)
