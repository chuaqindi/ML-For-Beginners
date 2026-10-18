import importlib.util
from pathlib import Path
import sys
import unittest

import pandas as pd


LESSON = Path(__file__).resolve().parents[1] / "3-Web-App/1-Web-App"


class UfoAppTests(unittest.TestCase):
    def test_training_and_predictions(self):
        path = LESSON / "ufo_app.py"
        self.assertTrue(path.is_file(), "UFO exercise and challenge are missing")
        spec = importlib.util.spec_from_file_location("ufo_app", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        app = module.create_app()
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get("/").status_code, 200)
        self.assertEqual(client.get("/train").status_code, 405)
        valid = {"seconds": "20", "latitude": "40.7", "longitude": "-74.0"}
        self.assertEqual(client.post("/predict", data=valid).status_code, 503)
        self.assertEqual(client.post("/train").status_code, 200)
        response = client.post("/predict", data=valid)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Likely country: US", response.text)
        for name, value in (("seconds", "nan"), ("seconds", "0"),
                            ("seconds", "61"), ("latitude", "91"),
                            ("longitude", "-181"), ("longitude", "inf"),
                            ("latitude", "")):
            with self.subTest(name=name, value=value):
                data = {**valid, name: value}
                self.assertEqual(client.post("/predict", data=data).status_code, 400)
        self.assertEqual(client.post("/predict", data={}).status_code, 400)
        frame = pd.DataFrame({
            "duration (seconds)": [20, 0, 61, 20, 20, 20],
            "latitude": [40, 40, 40, 91, 40, 40],
            "longitude": [-74, -74, -74, -74, float("inf"), -74],
            "country": ["us", "us", "us", "us", "us", None],
        })
        cleaned = module.clean_data(frame)
        self.assertEqual(len(cleaned), 1)
        self.assertEqual(cleaned.iloc[0]["Country"], "us")


if __name__ == "__main__":
    unittest.main()
