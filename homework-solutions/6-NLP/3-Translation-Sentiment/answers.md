# Translation and sentiment analysis

## Sentiment exercise and novel challenge

The [executed notebook](notebook.ipynb) contains the lesson's two Austen sentence examples, ambiguity probes, the complete novel analysis, and the poetry assignment. Publishing material, illustrations, and chapter headings are removed before sentence scoring; the downloaded source and its licence remain unchanged.

With the supplied Gutenberg edition, TextBlob 0.19.0, and NLTK 3.9.2, the novel yielded **4,648 sentences: 26 with polarity exactly +1 and 14 with polarity exactly -1**. It therefore has more absolutely positive than absolutely negative sentences according to this estimator. The notebook prints both complete collections, also saved in [extreme-sentences.csv](extreme-sentences.csv). These counts describe a particular tokenizer and lexicon, not the novel's overall emotional meaning. Different editions and package versions can change them.

## Knowledge checks

The estimator combines lexical evidence; its output does not show that it understands a sentence. An excellent father or landlord can be praised directly, but the surrounding dialogue can also be ironic. A wish that someone were happy does not mean that they are happy now. Relief when an unwelcome guest leaves is not praise of that guest. In “very great distress” or “greatest dislike,” positive associations with *great* can mislead an estimator about the whole phrase. The negative examples mention disgust or dread directly, so their broad negative interpretation is reasonable even when an exact score is not.

Translation likewise needs syntax and idiom: mapping words independently does not preserve an expression's meaning or grammatical structure. The lesson's French examples illustrate a difference between money generally and loose change. A comparison with a human translation must align the same passage, including additional clauses, before making a quality claim.

## Translation exercise — completed with an API replacement

TextBlob removed `translate()` in version 0.18.0 ([changelog](https://textblob.readthedocs.io/en/stable/changelog.html)). The notebook keeps the pinned TextBlob 0.19.0 for sentiment and executes four English-to-French requests through the documented [MyMemory API](https://mymemory.translated.net/doc/spec.php). This substitutes the translation backend rather than claiming the retired method works. The [complete responses](translation-responses.json) preserve the input, retrieval time in UTC, service status, returned translation, and match provenance. Retrieval was on **2026-10-19 Asia/Singapore**.

| Probe | Observed result and interpretation |
| --- | --- |
| Austen's opening sentence | The service returned a public-corpus match. It changed “universally acknowledged” to “presque incontestable” and rendered the single man as a young man. These shift certainty and age/marital-status information, so fluency alone does not establish fidelity. |
| “I have no money.” | The selected public-corpus match uses “argent,” conveying money generally rather than loose change. The returned alternatives include a less grammatical match, illustrating why memory matches still need review. |
| “It's raining cats and dogs.” | The public-corpus match uses a French heavy-rain idiom, “Il pleut comme vache qui pisse.” It avoids a literal animal translation, but its coarse register would be unsuitable for some audiences. |
| Novel sentence about an orange robot and seven umbrellas | The service explicitly labels this result `created-by=MT!`, `model=neural`. The French output retains the seven umbrellas, orange robot, and silent library. This is a semantic spot check, not a measured translation-quality score. |

The service combines translation-memory retrieval with machine translation; the first three results must not be presented as fresh neural-model outputs. The fourth supplies a separately identified machine-translation example. The lesson's longer human French passage also covers the following English sentence, so its extra clauses do not by themselves prove invention. A fair comparison aligns the same passage and evaluates meaning, idiom, and register. These four examples do not establish that machine or human translation is generally superior.

Re-running the notebook makes live requests and stops on service errors before replacing the response file. Each segment is below the API's 500-byte limit, and the four requests fit within its [5,000-character anonymous daily quota](https://mymemory.translated.net/doc/usagelimits.php). No account, API key, or extra package is needed; results can change because the service is not version-pinned.

## Assignment — poetic license

The assignment's Kaggle notebook was accessible, but its referenced `emily-flattened.csv` could not be retrieved anonymously on 2026-10-18. The notebook therefore explicitly substitutes **361 poems published by the same author, Jen Looper**, in [eMiLy](https://github.com/jlooper/eMiLy). The project's README identifies its stored sentiment values as Microsoft Cognitive Services output. The [original sample](../data/dickinson-azure.json), attribution, and licence are included. These are precomputed service results; no new Azure call or 597-poem analysis is claimed.

For those exact 361 poems, TextBlob and Microsoft scores have **Pearson correlation 0.1160**. A three-way comparison uses neutral bands of -0.2 to +0.2 for TextBlob and 0.4 to 0.6 for the Microsoft score, giving **11.36% agreement**. Microsoft labels are 314 negative, 17 neutral, and 30 positive; TextBlob labels are 12 negative, 248 neutral, and 101 positive. The [comparison CSV](poetry-comparison.csv), [plot](poetry-comparison.png), and notebook retain the scores and a threshold-sensitivity table.

The strongest disagreement was a poem beginning “Dying! Dying in the night!”: its stored Microsoft score is 0.0 while TextBlob gives +0.8125. Its imagery concerns death and a plea for help, so the positive TextBlob result is surprising on that reading. Another disagreement combines “perfect” and memory with an evening's judgement. Such juxtaposition, figurative language, and local word associations plausibly explain differences, but the precise service version and internal decisions are unavailable.

Neither service is human literary ground truth, and a rescaling of scores does not calibrate their meanings. The small substituted sample and chosen neutral bands limit the comparison. The result establishes disagreement on this supplied sample, rather than general superiority of Azure or TextBlob on poetry.

## Bot challenge

The [improved Marvin](../2-Tasks/bot.py) extracts question words and noun phrases, estimates polarity, and remembers one topic. Its executed tests and limitations are recorded in the preceding lesson.
