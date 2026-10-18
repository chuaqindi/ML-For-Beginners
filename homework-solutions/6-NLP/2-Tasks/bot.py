"""Marvin: sentiment, noun phrases, question rules, and one remembered topic."""

import re
from pathlib import Path

import nltk
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor


nltk.data.path.insert(0, str(Path(__file__).resolve().parents[1] / "data/nltk_data"))
EXTRACTOR = ConllExtractor()


def reply(message, memory):
    message = message.strip()
    if message.casefold() == "bye":
        return None
    if not message:
        return "Please type a message, or 'bye' to stop."

    words = re.findall(r"[a-z]+", message.casefold())
    blob = TextBlob(message, np_extractor=EXTRACTOR)
    phrases = blob.noun_phrases
    if phrases:
        memory["topic"] = str(phrases[0].pluralize())

    if "why" in words:
        response = "What cause do you think explains it? "
    elif "how" in words:
        response = "What first step could you try? "
    elif blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad. "
    elif blob.polarity < 0:
        response = "That sounds difficult. "
    elif blob.polarity == 0:
        response = "I see. "
    elif blob.polarity <= 0.5:
        response = "That sounds positive. "
    else:
        response = "That sounds very positive. "

    # shortcut: retain one noun phrase without resolving pronouns; upgrade for multiple topics.
    if memory.get("topic"):
        return response + f"Can you tell me more about {memory['topic']}?"
    return response + "Can you tell me more?"


def main():
    print("Hello, I am Marvin, a practice bot. Type 'bye' to stop.")
    print("I use word patterns and sentiment scores; I can misunderstand you.")
    memory = {}
    while True:
        try:
            message = input("> ")
        except EOFError:
            break
        response = reply(message, memory)
        if response is None:
            break
        print(response)
    print("It was nice talking to you, goodbye!")


if __name__ == "__main__":
    main()
