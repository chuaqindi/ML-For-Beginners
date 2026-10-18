# Common NLP tasks

## Exercise, challenge, and assignment

The documented assignment is [bot.py](bot.py); the [executed notebook](notebook.ipynb) demonstrates tokenization, frequency counts, bigrams, part-of-speech tags, noun phrases, pluralization, lemmatization, and the improved conversation.

From this directory, after the [data setup](../data/README.md), run:

```bash
python bot.py
```

The bot responds to `why` with a question about causes, and to `how` with a question about a first step. It matches whole words, so “somehow” does not accidentally trigger “how.” For other messages it estimates TextBlob polarity and chooses a corresponding response. A ConLL-trained noun-phrase extractor supplies a topic, which is pluralized for a follow-up. A neutral score gets a neutral acknowledgement. Blank input asks for a message, and a whole, trimmed `bye` exits.

The conversation challenge adds one remembered topic. For example, the scripted “lovely cat” message is followed by a response referring to “lovely cats,” including on the next message if no new noun phrase replaces it. The notebook records supplied test messages; no conversation with a friend or successful deception experiment is claimed.

## Knowledge checks

- A sympathetic response can seem relevant while misunderstanding sarcasm, negation, or the speaker's intent. Fluency does not establish comprehension.
- A noun phrase helps keep a reply on a recognizable topic and can be useful for search or entity extraction. A grammatical phrase is not necessarily the user's intended subject.
- In the Austen example, candidate phrases include “the hour,” “the spot,” “the look,” “the words,” “the foundation,” and “the middle.” Different chunkers can choose different boundaries.
- A lexicon can combine word polarities effectively for direct opinions, but has trouble with irony, implicit judgements, and the target of an opinion. Subjectivity is an estimator output, not a fact-checking score.

## How ML would reduce manual work

A labelled intent classifier could learn examples of requests for explanations, instructions, or topic changes instead of requiring a new keyword rule for each phrasing. Split training and evaluation data, include ambiguous and unrelated messages, and ask for clarification when confidence is low. The current noun-phrase extractor already uses a trained model; the question routing remains deliberately manual to meet the assignment.

The bot also addresses the next lesson's feature-extraction challenge through question words, noun phrases, sentiment, and conversational context. Its one-topic memory does not resolve multiple entities or pronouns generally. It is a learning exercise, not a reliable support or counselling system.
