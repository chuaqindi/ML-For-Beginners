import csv
import json
import posixpath
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


PORTFOLIO = Path(__file__).resolve().parents[1]


class RemainingHomeworkTests(unittest.TestCase):
    def test_remaining_quiz_keys_match_the_question_bank(self):
        quizzes = json.loads((PORTFOLIO.parent / "quiz-app/src/assets/translations/en.json").read_text())[0]["quizzes"]
        groups = {
            "7-TimeSeries": [41, 42, 43, 44, 51, 52],
            "8-Reinforcement": [45, 46, 47, 48],
            "9-Real-World": [49, 50],
        }
        for section, expected in groups.items():
            with self.subTest(section=section):
                path = PORTFOLIO / section / "quiz-answers.md"
                self.assertTrue(path.is_file())
                text = path.read_text()
                ids = [int(value) for value in re.findall(r"^## Quiz (\d+):", text, re.MULTILINE)]
                self.assertEqual(ids, expected)
                self.assertEqual(text.count("**Answer:**"), 3 * len(expected))
                for quiz in quizzes:
                    if int(quiz["id"]) in expected:
                        for question in quiz["quiz"]:
                            for answer in question["answerOptions"]:
                                if str(answer["isCorrect"]).lower() == "true":
                                    self.assertIn(f"**Answer:** {answer['answerText']}", text)

    def test_proposal_package_contains_editable_evidence_and_matching_results(self):
        path = PORTFOLIO / "9-Real-World/1-Applications/ml-scavenger-hunt.pptx"
        self.assertTrue(path.is_file())
        ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
        with zipfile.ZipFile(path) as archive:
            self.assertIsNone(archive.testzip())
            names = set(archive.namelist())
            slides = sorted(name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name))
            self.assertEqual(len(slides), 7)
            for owner in (3, 4):
                root = ET.fromstring(archive.read(f"ppt/slides/slide{owner}.xml"))
                self.assertIsNotNone(root.find(".//a:tbl", ns))
            evidence = " ".join(ET.fromstring(archive.read("ppt/slides/slide4.xml")).itertext())
            with (PORTFOLIO / "7-TimeSeries/3-SVR/energy-metrics.csv").open() as source:
                for row in csv.DictReader(source):
                    self.assertIn(f"{float(row['MAPE_percent']):.3f}", evidence)
                    self.assertIn(f"{float(row['MAE']):.2f}", evidence)
            for name in names:
                if name.endswith(".rels"):
                    base = posixpath.dirname(posixpath.dirname(name)) if "/_rels/" in name else ""
                    for relation in ET.fromstring(archive.read(name)):
                        target = posixpath.normpath(posixpath.join(base, relation.attrib["Target"]))
                        self.assertIn(target, names)


if __name__ == "__main__":
    unittest.main()
