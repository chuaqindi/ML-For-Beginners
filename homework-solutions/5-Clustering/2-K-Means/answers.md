# K-Means and alternative clustering

The [executed notebook](notebook.ipynb) contains boxplots, the k=1–10 elbow experiment, silhouette scores, cluster projections and profiles, scaling and feature-selection comparisons, seed stability, and two non-K-Means models for the assignment.

## Lesson corrections and findings

Genre is excluded from clustering inputs. Encoding it as an integer would introduce the known category and an arbitrary distance between genre codes. Cluster IDs are arbitrary, so direct equality with genre IDs is not classification accuracy. Adjusted Rand index (ARI) compares partitions without depending on the numeric IDs.

For three clusters, raw features give silhouette **0.5495** but genre ARI only **0.0179**. Standardized features give silhouette **0.2232** and ARI **0.0958**. Raw popularity has a much larger numeric scale than the fractional audio features and dominates distances. Scaling removes that units advantage; the lower silhouette does not by itself make scaling wrong because it changes the metric space. Contrary to the lesson’s final wording, high-variance features tend to dominate unscaled Euclidean distances, not low-variance ones.

The standardized elbow decreases smoothly rather than establishing a unique k. Among the tested standardized settings, k=2 has the largest silhouette (**0.2264**), only slightly above k=3 (**0.2232**). Three clusters are retained as the lesson’s illustrative setting, not declared the true genre count. Their mean profiles distinguish a more popular group, a louder/high-energy group, and a quieter/more-acoustic group. Every group still mixes genres.

## Challenge

Robust scaling gives silhouette **0.1912**, genre ARI **0.0738**. Standardizing only audio features gives **0.2457** and **0.0399**. These changes answer different grouping questions rather than guaranteeing better genre recovery. The three-cluster standardized fit has ARI **1.0** against each of five tested seeds with 20 starts, suggesting initialization stability for this setup, not proof of semantic validity. I retain outliers rather than deleting unusual songs merely to improve a score.

## Assignment — methods other than K-Means

**Ward agglomerative clustering** on the same standardized songs gives silhouette **0.1969**, genre ARI **0.0500**, and ARI **0.5599** against K-Means. The grouping differs, but it is not more aligned with artist genres here. Ward offers a hierarchy and avoids random centroid initialization while retaining a compact-group bias.

**DBSCAN** demonstrates a clearer geometric advantage on 400 synthetic two-moon points generated with Scikit-learn `make_moons(noise=0.06, random_state=42)`. At `eps=0.15, min_samples=5`, it recovers two groups with one noise point and ARI **0.9950**; two-centroid K-Means scores **0.2481**. At eps=0.08, DBSCAN fragments into 17 groups with 35 noise points. At eps=0.30, these particular moons still form two groups with ARI 1.0; a larger radius need not merge them immediately. The results show radius sensitivity, not a universal winning parameter.

The notebook guards silhouette calculation when there are fewer than two non-noise clusters and states whether noise is excluded. This prevents reporting a misleading or undefined score. Synthetic truth is used only for diagnosis after fitting. Clustering remains exploratory; these are not held-out predictive scores.

[Clustering reference](https://scikit-learn.org/stable/modules/clustering.html). [Quiz answers](../quiz-answers.md).
