# Exploring songs before clustering

The [executed notebook](notebook.ipynb) completes the lesson exploration and the five-scatterplot assignment using Matplotlib, Seaborn, and pandas. It includes genre counts, descriptive statistics, a correlation heatmap, and the lesson’s KDE distribution view. Source: `5-Clustering/data/nigerian-songs.csv` from this curriculum.

## Findings from the five scatterplots

1. **Popularity and danceability, Matplotlib:** genre colors overlap; their correlation is only **0.070** in this subset. A popular song is not necessarily more danceable by this descriptor.
2. **Energy and loudness, Seaborn:** correlation is **0.724**. Including both may give a related audio characteristic extra influence on distances; this is association, not causation.
3. **Tempo and speechiness, pandas:** correlation is **0.040**. Popularity coloring does not produce an obvious clean separation; isolated high-speechiness points deserve inspection rather than automatic removal.
4. **Acousticness and energy, Seaborn facets:** separate genre panels expose sample-size differences and overlapping ranges. A sparse genre panel is weaker evidence than the large one.
5. **Length and danceability, Matplotlib:** duration is shown in minutes; energy controls marker area and color. This adds a third measurement but overlapping large markers are harder to read precisely.

Filtering leaves **286 of 530 songs**: 206 afro dancehall, 61 afropop, and 19 Nigerian pop. Excluding zero popularity reproduces the lesson’s choice; it does not establish that zero means missing. The filter limits conclusions about less popular songs. Artist-level genre is also an imperfect description of each song, and the sample does not establish Nigerian listeners’ preferences.

## Challenge — choosing an algorithm

| Method | Problem it can address | Main choice or limitation |
| --- | --- | --- |
| K-Means | Fast grouping around compact numeric profiles | Choose k and scale features; poorly matches curved groups |
| MiniBatch K-Means | Similar grouping on a large stream or collection | Approximation trades some fit quality for lower cost |
| Agglomerative clustering | Explore nested group structure | Linkage and distance change the hierarchy; large pairwise work can be costly |
| DBSCAN | Find density-connected shapes and flag isolated samples | Radius and minimum density matter; varying densities are difficult |
| Gaussian mixture | Represent overlapping elliptical populations probabilistically | Covariance assumptions and component count need checking |
| Spectral clustering | Partition a similarity graph with nonlinear structure | Similarity construction and memory cost can dominate |

## Knowledge checks

E-commerce can group browsing patterns to explore customer segments; search can group related documents; operations teams can inspect unusual sensor profiles. These are hypothetical uses, not claimed personal experiences. Cluster IDs provide compact references for summaries, routing, or comparing groups. Replacing names with IDs alone **does not anonymize data**: small or distinctive clusters may still identify individuals.

## Sources

[Clustering guide](https://scikit-learn.org/stable/modules/clustering.html), [Matplotlib scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html), and [Seaborn scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html). [Quiz answers](../quiz-answers.md).
