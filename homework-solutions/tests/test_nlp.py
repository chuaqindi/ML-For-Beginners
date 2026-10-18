import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


PORTFOLIO = Path(__file__).resolve().parents[1]
NLP = PORTFOLIO / "6-NLP"


class NlpBotTests(unittest.TestCase):
    def load_bot(self, lesson):
        path = NLP / lesson / "bot.py"
        self.assertTrue(path.is_file(), f"Missing homework bot: {path}")
        spec = importlib.util.spec_from_file_location(lesson, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_basic_bot_exits_only_on_whole_bye(self):
        bot = self.load_bot("1-Introduction-to-NLP")
        self.assertIsNone(bot.reply("  BYe  "))
        self.assertIn(bot.reply("goodbye is a word"), bot.RESPONSES)

    def test_basic_bot_cli_accepts_input_and_eof(self):
        path = NLP / "1-Introduction-to-NLP/bot.py"
        for conversation in ("hello\n  BYE  \n", "hello\n"):
            with self.subTest(conversation=conversation):
                result = subprocess.run(
                    [sys.executable, str(path)], input=conversation,
                    text=True, capture_output=True, timeout=20,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("goodbye", result.stdout.lower())

    def test_friendly_bot_handles_questions_as_words(self):
        bot = self.load_bot("2-Tasks")
        self.assertIn("cause", bot.reply("WHY is that?", {}).lower())
        self.assertIn("step", bot.reply("How can I learn?", {}).lower())
        self.assertNotIn("step", bot.reply("Somehow I feel good.", {}).lower())

    def test_friendly_bot_uses_sentiment_and_remembers_topic(self):
        bot = self.load_bot("2-Tasks")
        memory = {}
        positive = bot.reply("I saw a lovely cat.", memory)
        self.assertIn("positive", positive.lower())
        self.assertIn("lovely cats", positive.lower())
        self.assertIn("lovely cats", bot.reply("It was wonderful!", memory).lower())
        self.assertIn("bad", bot.reply("This is awful and horrible.", {}).lower())

    def test_friendly_bot_empty_input_and_exit_preserve_memory(self):
        bot = self.load_bot("2-Tasks")
        memory = {"topic": "lovely cats"}
        self.assertIn("type", bot.reply("   ", memory).lower())
        self.assertIsNone(bot.reply(" BYE ", memory))
        self.assertEqual(memory, {"topic": "lovely cats"})

    def test_friendly_bot_cli_exits_without_reading_more_input(self):
        path = NLP / "2-Tasks/bot.py"
        result = subprocess.run(
            [sys.executable, str(path)], input="how?\nbye\nignored\n",
            text=True, capture_output=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("step", result.stdout.lower())
        self.assertNotIn("ignored", result.stdout.lower())


class NlpQuizTests(unittest.TestCase):
    def test_nlp_quiz_answers_match_the_english_question_bank(self):
        path = NLP / "quiz-answers.md"
        self.assertTrue(path.is_file())
        source = PORTFOLIO.parent / "quiz-app/src/assets/translations/en.json"
        quizzes = json.loads(source.read_text())[0]["quizzes"]
        text = path.read_text()
        self.assertEqual(text.count("**Answer:**"), 30)
        for quiz in quizzes:
            if 31 <= int(quiz["id"]) <= 40:
                with self.subTest(quiz=quiz["id"]):
                    self.assertIn(f"## Quiz {quiz['id']}:", text)
                    for question in quiz["quiz"]:
                        for answer in question["answerOptions"]:
                            if str(answer["isCorrect"]).lower() == "true":
                                self.assertIn(f"**Answer:** {answer['answerText']}", text)


if __name__ == "__main__":
    unittest.main()
