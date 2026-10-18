"""The lesson's basic bot. Run with Python; type bye to stop."""

import random


RESPONSES = [
    "That is quite interesting, please tell me more.",
    "I see. Do go on.",
    "Why do you say that?",
    "Funny weather we've been having, isn't it?",
    "Let's change the subject.",
    "Did you catch the game last night?",
]


def reply(message):
    if message.strip().casefold() == "bye":
        return None
    return random.choice(RESPONSES)


def main():
    print("Hello, I am Marvin, the simple robot. Type 'bye' to stop.")
    print("How are you today?")
    while True:
        try:
            message = input("> ")
        except EOFError:
            break
        response = reply(message)
        if response is None:
            break
        print(response)
    print("It was nice talking to you, goodbye!")


if __name__ == "__main__":
    main()
