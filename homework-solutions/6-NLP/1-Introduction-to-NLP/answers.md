# Introduction to natural language processing

## Exercise and knowledge checks

[bot.py](bot.py) implements the lesson's random-response Marvin. Run it with `python bot.py`, enter messages, and end with `bye`. Whitespace and case are ignored for the exit command; an end-of-file also exits cleanly. Importing the module does not start an interactive session. The [executed notebook](notebook.ipynb) records example replies and the assignment experiment.

Random replies can briefly resemble conversation, but do not depend on the input's meaning. Better replies need intent recognition, relevant information, context, and a way to admit uncertainty. Remembering previous turns helps resolve references, although storing text alone does not establish understanding. Dictation, search suggestions, spelling assistance, and message filters are examples of software features that can involve NLP; this is not a claim about any particular app's implementation.

## Challenge — remember a topic

Choose the third “stop and consider” question: a conversational system needs context when later messages refer to earlier ones.

```text
memory = empty topic
repeat:
    read message
    if the whole trimmed message is "bye": exit
    extract candidate noun phrases and estimate sentiment
    if a topic is found: replace the remembered topic
    choose a reply using question words and sentiment
    if a topic is remembered: ask a follow-up about that topic
    otherwise: ask for clarification
```

The [next lesson's bot](../2-Tasks/bot.py) implements this small memory. Keeping one topic is intentionally limited: it cannot distinguish several cats, resolve every “it,” or know when an unstated subject has changed.

## Assignment — search for a bot

### Investigating a published ELIZA-style bot

For this experiment I selected the ELIZA-style bot shipped with NLTK. It is an accessible, published conversational program that can be run locally without a banking account or a paid service. I tested the actual `nltk.chat.eliza` rules using `Chat.respond()`, rather than inventing a transcript. The [notebook](notebook.ipynb) saves the six prompts, their replies, and a fixed random seed; a separate [CSV transcript](eliza-transcript.csv) makes the observations easy to inspect. This experiment concerns NLTK's implementation, not a direct recreation of the complete historical ELIZA system.

I began with a plausible emotional statement: “I am sad.” The bot asked how I felt about being sad. Its reply was relevant on the surface because it reused the emotional description and turned it into a question. That is more responsive than Marvin's random choice, but a single appropriate answer does not demonstrate that a program understands an emotion. The rule source provides a more concrete explanation: regular expressions recognize common sentence forms, captured text fills response templates, and a reflection dictionary changes pronouns. Random selection among templates varies the wording.

I next supplied the deliberately nonsensical statement “You are a bicycle.” The observed response asked why I thought the bot was a bicycle. This exposed a boundary of the approach: it accepted the form of the sentence without checking whether its premise made sense. The system could match the phrase “you are,” capture the remaining words, and produce a grammatical question, even though the assertion was inappropriate for the speaker. The mechanism preserved conversational flow while failing a basic plausibility test.

The negation probe, “I am not sad,” produced a template containing “not sad.” This showed that negation could be copied successfully, but did not establish a general ability to reason about negated claims. To probe memory, I then said that my brother had broken my bicycle and asked what I had said about my brother. The follow-up received a generic question about how an answer would help me. It did not recover the earlier bicycle event. That is an observed failure on this prompt, rather than proof that every possible use of context is absent from all ELIZA variants.

Finally, I asked why the sky was blue. The bot asked me to supply a reason instead of giving a factual explanation. A reflective question is compatible with the conversational role it is simulating, so this prompt alone would not be a decisive failure. Combined with the bicycle and recall probes, however, it makes the limits clear: topical language and a fluent question can appear useful while providing neither factual knowledge nor reliable memory. The punctuation was also awkward when captured sentences already ended with a full stop.

My conclusion is that template reflection can produce locally relevant replies cheaply, but the relevance is fragile. The strongest evidence came from comparing actual responses with inspected rules, not from assuming an architecture based only on how human a reply sounded. Useful improvements would include a clearly stated scope, explicit clarification, basic context tracking, and evaluation on negation and reference questions. A learned intent model could broaden coverage, but would still require representative test data and a fallback. I did not test the bot on a friend or claim that it deceived a person.

Source: [NLTK ELIZA rules and implementation](https://www.nltk.org/_modules/nltk/chat/eliza.html). Experiment executed on 2026-10-18.
