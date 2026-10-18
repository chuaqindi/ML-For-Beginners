"""Reproduce the earlier Month regression and export a local model."""

from pathlib import Path
import pickle

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def train():
    dataset = Path(__file__).resolve().parents[3] / "2-Regression/data/US-pumpkins.csv"
    raw = pd.read_csv(dataset)
    rows = raw.loc[
        raw["Package"].str.contains("bushel", case=False, na=False),
        ["Date", "Package", "Low Price", "High Price"],
    ].copy()
    rows["Date"] = pd.to_datetime(rows["Date"], format="%m/%d/%y", errors="coerce")
    for column in ("Low Price", "High Price"):
        rows[column] = pd.to_numeric(rows[column], errors="coerce")
    rows = rows.dropna()
    volume = np.select(
        [rows["Package"].str.contains("1 1/9", regex=False),
         rows["Package"].str.contains("1/2", regex=False)],
        [10 / 9, 1 / 2], default=1.0,
    )
    features = pd.DataFrame({"Month": rows["Date"].dt.month})
    target = (rows["Low Price"] + rows["High Price"]) / 2 / volume
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    model = LinearRegression().fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Rows: {len(rows)}; train: {len(X_train)}; test: {len(X_test)}")
    print(f"R²: {r2_score(y_test, predictions):.3f}")
    print(f"MAE: {mean_absolute_error(y_test, predictions):.3f} USD/bushel")
    assert len(rows) == 415
    assert np.isfinite(predictions).all()
    assert abs(mean_absolute_error(y_test, predictions) - 9.176) < 0.001
    output = Path(__file__).with_name("pumpkin-model.pkl")
    with output.open("wb") as stream:
        pickle.dump(model, stream)
    with output.open("rb") as stream:
        restored = pickle.load(stream)
    np.testing.assert_allclose(restored.predict(X_test), predictions)
    print(f"Saved and verified: {output.name}")


if __name__ == "__main__":
    train()
