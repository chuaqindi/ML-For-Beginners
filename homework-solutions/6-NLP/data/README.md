# NLP data and reproducibility

Downloaded or prepared on **2026-10-18**. Use Python 3.10 or later with the portfolio's [requirements](../../requirements.txt). The execution environment used Python 3.12, TextBlob 0.19.0, and NLTK 3.9.2. Notebooks run from their own directories, and code adds this folder's `nltk_data` directory to NLTK's search path.

## Included data

| File | Contents and source |
| --- | --- |
| [pride-and-prejudice.txt](pride-and-prejudice.txt) | Complete downloaded [Project Gutenberg text, ebook 1342](https://www.gutenberg.org/ebooks/1342). The source file retains its metadata and licence. The analysis removes publishing material in memory. |
| [dickinson-azure.json](dickinson-azure.json) | 361 poem/score pairs from [Jen Looper's eMiLy project](https://github.com/jlooper/eMiLy/blob/master/app/assets/original-poems.json). The project identifies these as precomputed Microsoft Cognitive Services scores. See the included [Apache licence](dickinson-LICENSE.txt). |
| [movie_reviews.csv.gz](movie_reviews.csv.gz) | Complete 2,000-document Pang–Lee polarity corpus, prepared from NLTK's `movie_reviews`: `file_id`, `label`, and the original processed review text. The [original README](movie-reviews-README.txt) supplies attribution and limitations; see the [authors' data page](https://www.cs.cornell.edu/people/pabo/movie-review-data/). |

The assignment's [Kaggle notebook](https://www.kaggle.com/jenlooper/emily-dickinson-word-frequency) references `597-poems-by-emily-dickinson/emily-flattened.csv`. Its original CSV was not retrievable anonymously during this run. The included 361-poem file is an explicitly documented substitution from the same author; it is not represented as the missing 597-poem file. No new Microsoft service execution or unavailable service version is claimed.

SHA-256 checksums of included files:

```text
3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75  pride-and-prejudice.txt
c2ae3f1ec3ad266dea3a095f02ff96d2324f506cf3a31ceafc7d5c54b0db519b  dickinson-azure.json
14e2b8e0eb51463fe3cc5bbf5dc46bc7ddc0678c304b7445022aa9064afd4ac5  movie_reviews.csv.gz
```

## Translation response snapshot

The [translation notebook](../3-Translation-Sentiment/notebook.ipynb) was re-executed on **2026-10-19 Asia/Singapore** with TextBlob 0.19.0. Its [translation-responses.json](../3-Translation-Sentiment/translation-responses.json) stores four live English-to-French MyMemory GET responses with UTC retrieval times. The first three selected results come from translation memory; the novel robot sentence is marked `MT!` / `neural`. This replaces the retired TextBlob translation backend, while preserving the original lesson and its historical quiz answers.

Re-running that notebook needs internet access. It uses Python's standard library, checks service errors, and writes a new snapshot only after all requests succeed. See the provider's [API specification](https://mymemory.translated.net/doc/spec.php) and [usage limits](https://mymemory.translated.net/doc/usagelimits.php). The saved responses record this run; the public service's future output is not guaranteed to match.

## NLTK resource setup

Run from the repository root, using the same Python environment that runs the notebooks:

```bash
python -m nltk.downloader -d homework-solutions/6-NLP/data/nltk_data punkt_tab averaged_perceptron_tagger_eng conll2000 stopwords wordnet vader_lexicon gutenberg
```

The downloaded resources are ignored by Git. No downloads occur implicitly when a bot is imported. `movie_reviews` is not required for execution because its complete prepared CSV is included. To reconstruct that CSV from the corpus, additionally download NLTK's `movie_reviews` resource, enumerate `movie_reviews.fileids()`, and save each ID, its category, and `movie_reviews.raw(file_id)`.

## Full hotel data

The notebooks use Jiashen Liu's [515K Hotel Reviews Data in Europe](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe), identified by the curriculum as CC0. The original contains **515,738 rows and 17 columns**, and **238,154,765 uncompressed bytes**. The full compressed original and the two generated hotel tables are present locally but ignored by Git to avoid adding large, reproducible downloads to the portfolio.

To download and compress the original, run from the repository root:

```bash
curl --fail --location --output /tmp/mlfb-hotel-reviews.zip https://www.kaggle.com/api/v1/datasets/download/jiashenliu/515k-hotel-reviews-data-in-europe
unzip -p /tmp/mlfb-hotel-reviews.zip Hotel_Reviews.csv | gzip > homework-solutions/6-NLP/data/Hotel_Reviews.csv.gz
```

The SHA-256 of the **uncompressed** `Hotel_Reviews.csv` is:

```text
a4810c2757934f0a826a1b16a437eb67a38be45b1a22ad56772afce0b6c11af9
```

Run `4-Hotel-Reviews-1/notebook.ipynb`, then `5-Hotel-Reviews-2/notebook.ipynb`. The second notebook saves and reloads `Hotel_Reviews_Filtered.csv.gz` and saves `Hotel_Reviews_NLP.csv.gz`, each with all 515,738 rows. No existing raw file is overwritten. Model agreement, hotel score correlation, and exploratory clusters are not human-annotated sentiment accuracy or a production recommender evaluation.

## Verification environment

For this run, compatible packages were staged in `/private/tmp/mlfb-extra` and supplied through `PYTHONPATH`. Matplotlib, IPython, and Jupyter caches used temporary directories. These staging paths are not required by the notebook sources: installing the recorded requirements in a dedicated Python environment and performing the resource setup above is sufficient.

Seven notebooks were executed from clean kernels with saved outputs and a 1,200-second per-cell limit. The full hotel notebook took about 89 seconds in this run. Larger timeouts accommodate slower machines; execution times are observations, not guarantees.
