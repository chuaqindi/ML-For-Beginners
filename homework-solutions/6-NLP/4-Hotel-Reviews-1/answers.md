# Hotel reviews: processing the data

## Exercise results

The [executed notebook](notebook.ipynb) analyzes the **entire 515,738-row, 17-column dataset**. The raw compressed file is available locally; [data notes](../data/README.md) describe its source, hash, and download procedure.

- The nationality field has **227 distinct values**, including an unspecified blank value. The notebook prints all values and the requested counts. United Kingdom is most common, with **245,246 reviews**; the next ten and each top-ten nationality's most-reviewed hotel are shown.
- There are **1,492 hotel names**, but **1,494 distinct name/address pairs**. Grouping by name alone merges some properties. The exploration follows the lesson's name-based calculations, while the next notebook uses the original name/address pair as identity.
- Britannia International Hotel Canary Wharf has the most observed reviews, **4,789**. Its supplied total is **9,086**, and the dataset-derived rounded mean is **6.8** against the supplied **7.1**. The data cannot establish how unobserved reviews affected the supplied aggregates.
- **417 hotel names** have equal supplied and calculated means after rounding to one decimal place. The notebook uses a row function with `.apply()` on one row per hotel, prints every mismatch once, and saves [hotel-summary.csv](hotel-summary.csv).
- **127,890** rows contain `No Negative`; **35,946** contain `No Positive`; **127** contain both. Those 127 rows have a rating but no review text and should not be interpreted as expressed neutral sentiment.
- The original dataset contains **526 complete duplicate rows**. Latitude and longitude each have missing values; the absence does not justify dropping useful review text for this sentiment task.

The [exploration plot](hotel-exploration.png) shows nationality counts and differences between supplied and observed hotel means. These are counts of reviews, not a count of independent reviewers.

## Challenge — bias and skew in text datasets

Hotel reviews cover selected hotels in six European cities, not a representative sample of all travellers or properties. The nationality distribution is uneven, reviewer IDs are unavailable, and repeated guests may occur. Using nationality as a causal explanation for sentiment would invite stereotyping and confounding by destination, travel purpose, and expectations.

The negative/positive field names are collection prompts, not verified sentiment labels. Sarcasm, mixed opinions, empty fields, and complaints unrelated to the hotel can break that assumption. Preserve Unicode and negation; diagnose encoding problems instead of removing non-English characters indiscriminately. Distinctive words, room labels, and duplicated reviews can also distort frequencies.

As a comparison, the next lesson's movie corpus deliberately contains 1,000 positive and 1,000 negative rating-derived labels. Its balance, document length, domain, and already lowercased text differ from hotel comments. A document split cannot establish performance on new films or reviewers without corresponding identifiers. This explains why a method's success in one text dataset cannot simply be assumed in another.

## Assignment — NLTK

The [executed NLTK exercises](nltk-exercises.ipynb) adapt the vocabulary and text-search exercises from [NLTK book Chapter 1](https://www.nltk.org/book/ch01.html): token and type counts, lexical diversity, frequency percentages, suffix and length filters, concordance, and adjacent bigrams. The [frequency plot](nltk-frequencies.png) records actual output. These are selected exercises, not a claim to have completed the entire book.
