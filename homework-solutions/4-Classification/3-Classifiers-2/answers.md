# Classifier comparison and parameter play

The [executed notebook](notebook.ipynb) completes all five classifier exercises, prints their installed defaults, and runs nine Random Forest parameter settings. Recipe inputs are grouped before both outer testing and inner validation, preventing identical inputs from leaking across partitions.

## Model comparison

Validation macro F1 was **0.7464** for LinearSVC, **0.6052** for K-neighbors, **0.7781** for RBF SVC, **0.7603** for Random Forest, and **0.6752** for AdaBoost. These are validation results, not training accuracy. RBF SVC is strongest in this comparison; Random Forest is retained for the assignment’s planned parameter experiment, not claimed to be the best algorithm overall.

## Assignment results

The forest varies `max_depth` across 2, 8, and unlimited and `min_samples_leaf` across 1, 5, and 20, with 100 trees and a fixed seed throughout. Unlimited depth with leaf size 1 wins validation at **0.7603** macro F1. Depth 2 with leaf size 20 performs worst at **0.6608**: these constraints prevent the model from capturing enough ingredient interactions. Depth 8 with leaf size 5 scores **0.7265**, a small improvement over leaf size 1 at **0.7251**, consistent with modest smoothing helping that depth.

At unlimited depth, increasing leaf size from 1 to 5 lowers training macro F1 from **0.9877** to **0.8103** and validation F1 from **0.7603** to **0.7494**. It reduces the overfitting gap, but the lost detail also reduces validation performance. Thus a smaller gap alone is not the selection objective. Leaf size 20 reduces validation F1 further to **0.7011**.

The selected setting is refitted on all outer training rows, then tested once: accuracy **0.8074**, macro F1 **0.7679**. Japanese recall is only **0.51**, demonstrating why per-class metrics matter. The scores remain uncertain because they come from one held-out split; future work could repeat grouped cross-validation. No parameters were chosen from the final test score.

## Challenge

- **LinearSVC:** smaller `C` penalizes complexity more; a larger iteration limit helps convergence but does not add model capacity.
- **K-neighbors:** larger neighbor counts smooth decisions; distance weighting gives nearer recipes more influence. Sparse high-dimensional flags can make distance less informative.
- **SVC:** `C` balances fit against regularization; `gamma` controls RBF locality. Very large values can fit isolated training points.
- **Random Forest:** depth and leaf size control tree complexity; more trees reduce ensemble variability at a compute cost.
- **AdaBoost:** `learning_rate` and `n_estimators` jointly control stage strength; noisy labels can attract excessive attention.

Defaults are printed directly from the installed estimators in the notebook. See [SVM](https://scikit-learn.org/stable/modules/svm.html), [neighbors](https://scikit-learn.org/stable/modules/neighbors.html), and [ensemble](https://scikit-learn.org/stable/modules/ensemble.html) documentation. [Quiz answers](../quiz-answers.md).
