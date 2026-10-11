# Logistic regression homework

## Assignment — full pumpkin color model

### Cleaning and preprocessing

The notebook keeps all **1,141 rows with a known color**, including the 12 striped pumpkins. Cleaning removes only columns that are entirely empty or whose names begin with `Unnamed`; it does not drop rows merely because a feature is missing. The original date is replaced by Year, Month, and DayOfYear. Numeric and categorical gaps are then handled by median and most-frequent imputation inside the model pipeline.

Numeric standardization is also inside the pipeline, so its statistics are learned only from the 912 training rows. Categorical features are one-hot encoded with unknown-category handling. Runtime assertions confirm that `Color` is never among the preprocessing inputs and that the scaler saw only the training sample.

### Class imbalance and results

The target has 916 orange, 213 white, and only 12 striped pumpkins. A stratified split preserves all classes, `class_weight="balanced"` reduces majority-class dominance, and macro F1 gives each class equal weight. The held-out accuracy is **0.865** and macro F1 is **0.688**. The confusion matrix shows 156/184 orange, 2/2 striped, and 40/43 white test examples classified correctly. The apparent striped recall is not stable: it comes from only two test examples, and its precision is **0.25** because other colors are sometimes predicted as striped.

Important limitations remain. These are market reports rather than independent samples collected for color recognition, feature values may encode location or packaging practices that change over time, and the extreme striped-class scarcity makes minority performance uncertain. Balanced weighting and imputation do not create missing evidence, so this model is an educational baseline rather than a deployment-ready classifier.

## Challenge — breast-cancer classification

For a separate logistic-regression experiment, I use Scikit-learn's breast-cancer dataset and define malignant as the positive class. A stratified split is followed by training-only standardization and balanced logistic regression in one pipeline. On the held-out set, the model reaches accuracy **0.972**, malignant-class F1 **0.962**, and ROC AUC **0.995**. Its confusion matrix has 89 true benign, 1 false malignant alarm, 3 missed malignant cases, and 50 correctly detected malignant cases.

This result is not clinical validation. The built-in dataset is small and curated, a single random split understates uncertainty, and false-negative costs require domain-specific threshold selection and external evaluation. No medical decision should rely on this classroom model.
