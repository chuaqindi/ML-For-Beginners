import json
import re
import unittest
from pathlib import Path


PORTFOLIO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_NOTEBOOKS = (
    "2-Regression/1-Tools/notebook.ipynb",
    "2-Regression/2-Data/notebook.ipynb",
    "2-Regression/3-Linear/notebook.ipynb",
    "2-Regression/4-Logistic/notebook.ipynb",
)


def assert_executed_notebook(test_case, relative_path):
    notebook = json.loads((PORTFOLIO_ROOT / relative_path).read_text())
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    test_case.assertTrue(code_cells)
    for cell in code_cells:
        test_case.assertIsNotNone(cell["execution_count"])
        test_case.assertNotIn("error", {output["output_type"] for output in cell["outputs"]})


class PortfolioTests(unittest.TestCase):
    def test_required_notebooks_are_executed(self):
        for relative_path in REQUIRED_NOTEBOOKS:
            with self.subTest(notebook=relative_path):
                self.assertTrue((PORTFOLIO_ROOT / relative_path).is_file())
                assert_executed_notebook(self, relative_path)

    def test_linnerud_answer_is_exploratory(self):
        path = PORTFOLIO_ROOT / "2-Regression/1-Tools/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in ("situps", "waist", "20", "small sample", "exploratory", "non-causal"):
            with self.subTest(topic=topic):
                self.assertIn(topic, text)

    def test_data_answers_compare_plotting_libraries(self):
        path = PORTFOLIO_ROOT / "2-Regression/2-Data/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in (
            "## matplotlib", "## seaborn", "scatter", "regression", "residual",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic, text)

    def test_linear_answers_explain_model_choice_and_accuracy(self):
        path = PORTFOLIO_ROOT / "2-Regression/3-Linear/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in (
            "correlation", "predictive accuracy", "linear", "polynomial", "limitation",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic, text)

    def test_logistic_answers_cover_cleaning_standardization_and_imbalance(self):
        path = PORTFOLIO_ROOT / "2-Regression/4-Logistic/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in ("cleaning", "standardization", "class imbalance", "limitation"):
            with self.subTest(topic=topic):
                self.assertIn(topic, text)

    def test_index_and_manifest_exist(self):
        self.assertTrue((PORTFOLIO_ROOT / "README.md").is_file())
        self.assertTrue((PORTFOLIO_ROOT / "requirements.txt").is_file())

    def test_quiz_key_covers_ids_1_through_16(self):
        path = PORTFOLIO_ROOT / "quiz-answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text()
        quiz_ids = [int(value) for value in re.findall(r"^## Quiz (\d+):", text, re.MULTILINE)]
        self.assertEqual(quiz_ids, list(range(1, 17)))
        self.assertEqual(text.count("**Answer:**"), 48)

    def test_intro_ml_has_diagram_and_skip(self):
        path = PORTFOLIO_ROOT / "1-Introduction/1-intro-to-ML/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text()
        self.assertIn("## Challenge", text)
        self.assertIn("```mermaid", text)
        self.assertIn("## Assignment — Skipped", text)
        self.assertIn("external training", text.lower())

    def test_history_timeline_has_events_and_media(self):
        lesson = PORTFOLIO_ROOT / "1-Introduction/2-history-of-ML"
        answer_path = lesson / "answers.md"
        html_path = lesson / "timeline/index.html"
        css_path = lesson / "timeline/styles.css"
        self.assertTrue(answer_path.is_file())
        self.assertTrue(html_path.is_file())
        self.assertTrue(css_path.is_file())
        html = html_path.read_text()
        self.assertGreaterEqual(html.count("data-year="), 8)
        self.assertGreaterEqual(html.count("<iframe"), 2)
        self.assertIn('href="styles.css"', html)
        self.assertIn("<main", html)
        self.assertGreaterEqual(html.count("<a href="), 8)

    def test_fairness_answer_covers_lending_harms_and_controls(self):
        path = PORTFOLIO_ROOT / "1-Introduction/3-fairness/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in (
            "lending", "allocation", "data representation",
            "subgroup evaluation", "appeal", "monitoring",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic, text)
        self.assertIn("## assignment — skipped", text)
        self.assertIn("external responsible ai notebook", text)

    def test_ml_techniques_answer_has_workflow_and_skip_notes(self):
        path = PORTFOLIO_ROOT / "1-Introduction/4-techniques-of-ML/answers.md"
        self.assertTrue(path.is_file())
        text = path.read_text()
        self.assertIn("```mermaid", text)
        for stage in (
            "Decide on the question", "Collect and prepare data",
            "Choose a training method", "Train the model",
            "Evaluate the model", "Parameter tuning", "Predict",
        ):
            with self.subTest(stage=stage):
                self.assertIn(stage, text)
        self.assertIn("## Personal reflection — Skipped", text)
        self.assertIn("## Assignment — Skipped", text)
        self.assertIn("interview", text.lower())


if __name__ == "__main__":
    unittest.main()
