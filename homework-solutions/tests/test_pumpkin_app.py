import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


APP_DIR = Path(__file__).resolve().parents[1] / "3-Web-App/1-Web-App"


class PumpkinAppTests(unittest.TestCase):
    def test_app_predictions_and_validation(self):
        path = APP_DIR / "app.py"
        self.assertTrue(path.is_file(), "Pumpkin assignment app is missing")
        subprocess.run([sys.executable, str(APP_DIR / "train.py")], check=True, capture_output=True)
        spec = importlib.util.spec_from_file_location("pumpkin_app", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        client = module.app.test_client()
        self.assertEqual(client.get("/").status_code, 200)
        for month in (1, 6, 12):
            with self.subTest(month=month):
                response = client.post("/predict", data={"month": str(month)})
                self.assertEqual(response.status_code, 200)
                self.assertRegex(response.text, r"USD \d+\.\d{2} per bushel")
        for value in (None, "", "nan", "inf", "0", "13", "2.5", "hello"):
            with self.subTest(invalid=value):
                data = {} if value is None else {"month": value}
                response = client.post("/predict", data=data)
                self.assertEqual(response.status_code, 400)
                self.assertNotIn("USD ", response.text)
        # Submitted field order must not replace the named model feature.
        extra = client.post("/predict", data={"other": "999", "month": "6"})
        normal = client.post("/predict", data={"month": "6"})
        self.assertEqual(extra.data, normal.data)


if __name__ == "__main__":
    unittest.main()
