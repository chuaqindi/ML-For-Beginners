import json
import unittest
from pathlib import Path


PORTFOLIO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_NOTEBOOKS = ()


def assert_executed_notebook(test_case, relative_path):
    notebook = json.loads((PORTFOLIO_ROOT / relative_path).read_text())
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    test_case.assertTrue(code_cells)
    for cell in code_cells:
        test_case.assertIsNotNone(cell["execution_count"])
        test_case.assertNotIn("error", {output["output_type"] for output in cell["outputs"]})


class PortfolioTests(unittest.TestCase):
    def test_index_and_manifest_exist(self):
        self.assertTrue((PORTFOLIO_ROOT / "README.md").is_file())
        self.assertTrue((PORTFOLIO_ROOT / "requirements.txt").is_file())


if __name__ == "__main__":
    unittest.main()
