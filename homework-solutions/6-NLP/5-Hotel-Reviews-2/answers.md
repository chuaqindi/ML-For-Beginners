# Hotel reviews: sentiment analysis

## Filtering and sentiment exercise

The [executed notebook](notebook.ipynb) processes all **515,738 reviews**. It identifies **1,494 properties** using original name/address pairs before abbreviating the address to city and country. It recalculates observed review counts and rounded means, removes the specified unused columns, safely parses the serialized tag lists with `ast.literal_eval`, and creates the eight selected trip/guest indicators. Both spellings of travellers with friends are included in the group indicator.

The filtered table has **17 columns** and is saved and reloaded as `../data/Hotel_Reviews_Filtered.csv.gz`. This includes a property ID that prevents distinct properties with the same hotel name from merging. Unrecognized address countries and malformed tag containers raise an error rather than silently becoming missing values.

The stopword experiment shows that removing **not** reverses the sign of “not good.” VADER therefore scores original text, preserving negation, intensifiers, and punctuation. Empty review placeholders receive zero field scores, with separate missing-text handling. The mean of the available field scores is left missing when both fields are absent. This mean is a descriptive summary, not a calibrated document-level sentiment score.

The notebook scored **740,542 distinct field strings**, reusing results for repeated text. Combined sentiment has **Pearson correlation 0.4947** with reviewer scores. Among nonempty fields, **6,940 positive-labelled comments** have VADER compound scores below -0.05, and **101,827 negative-labelled comments** score above +0.05. The fields' headings therefore cannot be treated as verified sentiment labels. Correlation with ratings is a sanity check rather than a measurement of sentiment accuracy.

The full **515,738-row, 22-column** scored table is saved locally as `../data/Hotel_Reviews_NLP.csv.gz`. Large hotel data and generated tables are ignored by Git and can be reproduced using the [data instructions](../data/README.md).

## Challenge — sentiment patterns

Three K-Means clusters use the two sentiment fields only, excluding the 127 rows with no review text. Reviewer scores describe the resulting clusters and are not used to create them. The fixed 2,000-row silhouette sample gives **0.5009**.

| Cluster | Reviews | Mean negative-field score | Mean positive-field score | Mean reviewer rating |
| --- | ---: | ---: | ---: | ---: |
| 0 | 77,434 | 0.543 | 0.722 | 8.499 |
| 1 | 312,642 | -0.133 | 0.759 | 8.752 |
| 2 | 125,425 | -0.140 | 0.004 | 7.442 |

See the [cluster summary](sentiment-clusters.csv) and [plot](hotel-sentiment.png). Cluster numbers are arbitrary. Choosing three clusters is exploratory, and the separation does not validate real guest categories or a recommendation system. Duplicate rows, repeated reviewers, sampling bias, sarcasm, and mixed opinions limit interpretation.

## Assignment — try a different dataset

The [executed movie-review assignment](assignment.ipynb) includes the complete **2,000-document Pang–Lee corpus** as [a compressed CSV](../data/movie_reviews.csv.gz), with its [original documentation](../data/movie-reviews-README.txt). It checks missing data, normalized duplicates, and label consistency before a fixed, stratified **1,500/500 train/test split**. The TF-IDF vocabulary is fitted inside the training pipeline only.

| Method | Accuracy on the same 500 test reviews | Balanced accuracy |
| --- | ---: | ---: |
| Majority baseline | 50.0% | 50.0% |
| VADER, compound threshold 0 | 65.0% | 65.0% |
| TF-IDF bigrams and logistic regression | 85.6% | 85.6% |

The standard VADER neutral band produces no abstentions in this test set. Coverage is nevertheless reported explicitly. [Metrics](movie-review-metrics.csv), [predictions](movie-review-predictions.csv), and [confusion matrices](movie-review-confusion.png) preserve the measured results.

The trained classifier benefits from domain-specific labelled examples, while VADER uses a fixed lexicon and can saturate on long, mixed-polarity reviews. This comparison does not establish performance on future reviews, new films, other reviewers, or hotel data. The balanced dataset and rating-derived labels are important limitations; no threshold was tuned on the test set.
