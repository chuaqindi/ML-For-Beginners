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
    "3-Web-App/1-Web-App/notebook.ipynb",
    "4-Classification/1-Introduction/notebook.ipynb",
    "4-Classification/2-Classifiers-1/notebook.ipynb",
    "4-Classification/3-Classifiers-2/notebook.ipynb",
    "4-Classification/4-Applied/notebook.ipynb",
    "5-Clustering/1-Visualize/notebook.ipynb",
    "5-Clustering/2-K-Means/notebook.ipynb",
    "6-NLP/1-Introduction-to-NLP/notebook.ipynb",
    "6-NLP/2-Tasks/notebook.ipynb",
    "6-NLP/3-Translation-Sentiment/notebook.ipynb",
    "6-NLP/4-Hotel-Reviews-1/notebook.ipynb",
    "6-NLP/4-Hotel-Reviews-1/nltk-exercises.ipynb",
    "6-NLP/5-Hotel-Reviews-2/notebook.ipynb",
    "6-NLP/5-Hotel-Reviews-2/assignment.ipynb",
    "7-TimeSeries/1-Introduction/notebook.ipynb",
    "7-TimeSeries/2-ARIMA/notebook.ipynb",
    "7-TimeSeries/2-ARIMA/assignment.ipynb",
    "7-TimeSeries/3-SVR/notebook.ipynb",
    "7-TimeSeries/3-SVR/assignment.ipynb",
    "8-Reinforcement/1-QLearning/notebook.ipynb",
    "8-Reinforcement/2-Gym/notebook.ipynb",
    "8-Reinforcement/2-Gym/assignment.ipynb",
    "9-Real-World/2-Debugging-ML-Models/notebook.ipynb",
)
REQUIRED_ARTIFACTS = (
    "7-TimeSeries/quiz-answers.md",
    "7-TimeSeries/data/README.md",
    "7-TimeSeries/1-Introduction/answers.md",
    "7-TimeSeries/1-Introduction/notebook.ipynb",
    "7-TimeSeries/2-ARIMA/answers.md",
    "7-TimeSeries/2-ARIMA/notebook.ipynb",
    "7-TimeSeries/2-ARIMA/assignment.ipynb",
    "7-TimeSeries/3-SVR/answers.md",
    "7-TimeSeries/3-SVR/notebook.ipynb",
    "7-TimeSeries/3-SVR/assignment.ipynb",
    "8-Reinforcement/quiz-answers.md",
    "8-Reinforcement/qlearning.py",
    "8-Reinforcement/world.py",
    "8-Reinforcement/1-QLearning/answers.md",
    "8-Reinforcement/1-QLearning/notebook.ipynb",
    "8-Reinforcement/2-Gym/answers.md",
    "8-Reinforcement/2-Gym/notebook.ipynb",
    "8-Reinforcement/2-Gym/assignment.ipynb",
    "9-Real-World/quiz-answers.md",
    "9-Real-World/1-Applications/answers.md",
    "9-Real-World/1-Applications/ml-scavenger-hunt.pptx",
    "9-Real-World/2-Debugging-ML-Models/answers.md",
    "9-Real-World/2-Debugging-ML-Models/notebook.ipynb",
    "6-NLP/quiz-answers.md",
    "6-NLP/data/README.md",
    "6-NLP/1-Introduction-to-NLP/answers.md",
    "6-NLP/1-Introduction-to-NLP/bot.py",
    "6-NLP/1-Introduction-to-NLP/notebook.ipynb",
    "6-NLP/2-Tasks/answers.md",
    "6-NLP/2-Tasks/bot.py",
    "6-NLP/2-Tasks/notebook.ipynb",
    "6-NLP/3-Translation-Sentiment/answers.md",
    "6-NLP/3-Translation-Sentiment/notebook.ipynb",
    "6-NLP/4-Hotel-Reviews-1/answers.md",
    "6-NLP/4-Hotel-Reviews-1/notebook.ipynb",
    "6-NLP/4-Hotel-Reviews-1/nltk-exercises.ipynb",
    "6-NLP/5-Hotel-Reviews-2/answers.md",
    "6-NLP/5-Hotel-Reviews-2/notebook.ipynb",
    "6-NLP/5-Hotel-Reviews-2/assignment.ipynb",
    "4-Classification/quiz-answers.md",
    "4-Classification/1-Introduction/answers.md",
    "4-Classification/1-Introduction/notebook.ipynb",
    "4-Classification/1-Introduction/classification-methods.docx",
    "4-Classification/2-Classifiers-1/answers.md",
    "4-Classification/2-Classifiers-1/notebook.ipynb",
    "4-Classification/2-Classifiers-1/solver-comparison.docx",
    "4-Classification/3-Classifiers-2/answers.md",
    "4-Classification/3-Classifiers-2/notebook.ipynb",
    "4-Classification/4-Applied/answers.md",
    "4-Classification/4-Applied/notebook.ipynb",
    "4-Classification/4-Applied/index.html",
    "3-Web-App/1-Web-App/answers.md",
    "3-Web-App/1-Web-App/notebook.ipynb",
    "3-Web-App/1-Web-App/quiz-answers.md",
    "3-Web-App/1-Web-App/ufo_app.py",
    "quiz-answers.md",
    "1-Introduction/1-intro-to-ML/answers.md",
    "1-Introduction/2-history-of-ML/answers.md",
    "1-Introduction/2-history-of-ML/timeline/index.html",
    "1-Introduction/3-fairness/answers.md",
    "1-Introduction/4-techniques-of-ML/answers.md",
    "2-Regression/1-Tools/answers.md",
    "2-Regression/1-Tools/notebook.ipynb",
    "2-Regression/2-Data/answers.md",
    "2-Regression/2-Data/notebook.ipynb",
    "2-Regression/3-Linear/answers.md",
    "2-Regression/3-Linear/notebook.ipynb",
    "2-Regression/4-Logistic/answers.md",
    "2-Regression/4-Logistic/notebook.ipynb",
)
APPROVED_SKIPS = (
    "External environment-training courses and videos",
    "External Responsible AI notebook",
    "Data-scientist interview",
    "Cloud deployment",
)


def assert_executed_notebook(test_case, relative_path):
    notebook = json.loads((PORTFOLIO_ROOT / relative_path).read_text())
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    test_case.assertTrue(code_cells)
    test_case.assertEqual(
        [cell["execution_count"] for cell in code_cells],
        list(range(1, len(code_cells) + 1)),
    )
    for cell in code_cells:
        for output in cell["outputs"]:
            test_case.assertNotEqual(output["output_type"], "error")
            if output["output_type"] == "stream":
                test_case.assertNotEqual(output["name"], "stderr")


class PortfolioTests(unittest.TestCase):
    def test_all_required_notebooks_execute_cleanly(self):
        for relative_path in REQUIRED_NOTEBOOKS:
            with self.subTest(notebook=relative_path):
                self.assertTrue((PORTFOLIO_ROOT / relative_path).is_file())
                assert_executed_notebook(self, relative_path)

    def test_index_links_every_required_artifact(self):
        text = (PORTFOLIO_ROOT / "README.md").read_text()
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)
        local_links = {link.split("#", 1)[0] for link in links if "://" not in link}
        self.assertTrue(set(REQUIRED_ARTIFACTS).issubset(local_links))
        for relative_path in local_links:
            with self.subTest(link=relative_path):
                resolved = (PORTFOLIO_ROOT / relative_path).resolve()
                self.assertTrue(resolved.is_relative_to(PORTFOLIO_ROOT.resolve()))
                self.assertTrue(resolved.is_file())

    def test_all_approved_skips_are_labeled(self):
        text = (PORTFOLIO_ROOT / "README.md").read_text()
        label = "**Skipped — approved exclusion:**"
        self.assertEqual(text.count(label), len(APPROVED_SKIPS))
        for category in APPROVED_SKIPS:
            with self.subTest(category=category):
                self.assertEqual(text.count(f"{label} {category}"), 1)

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

    def test_ml_techniques_answer_has_workflow_and_interview_skip(self):
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
        self.assertIn("## Assignment — Skipped", text)
        self.assertIn("interview", text.lower())


if __name__ == "__main__":
    unittest.main()
