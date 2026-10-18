# Introduction to classification

## Exercise and findings

The [executed notebook](notebook.ipynb) explores 2,448 recipes and plots the ten most frequent ingredients for each cuisine. Original counts are Korean 799, Indian 598, Chinese 442, Japanese 320, and Thai 289. Counts describe this collection, not the prevalence of dishes worldwide. Within-cuisine rates are more useful than raw counts when comparing cuisines of different sample sizes.

The grouped split contains 1,960 training and 488 test recipes. Identical model-input vectors cannot cross the boundary. Following the lesson, rice, garlic, and ginger are excluded, leaving 380 ingredients. This is a reproduction choice, not proof that frequent ingredients are useless: their prevalence differs across cuisines.

SMOTE is applied only to training rows, giving 647 examples per class. It creates 8,440 fractional ingredient entries because interpolation is performed in floating-point feature space. These are synthetic feature vectors, not literal recipes. The notebook exports `training-balanced.csv` and `held-out.csv` locally; both are reproducible generated files excluded from Git. Later classifiers instead use class weights where supported and always evaluate untouched original recipes.

## Challenge and knowledge checks

- **Cuisine multiclass:** which of the five labels matches the ingredient basket? This estimates a dataset label, not authenticity.
- **Cuisine binary:** does a recipe use fenugreek? Remove fenugreek from predictors to avoid revealing the answer. In this collection its prevalence is 28.8% for Indian recipes and 21.1% for Thai recipes; it is not exclusive to one cuisine.
- **Pumpkin binary:** orange versus another recorded color, using price, variety, package, and market features while excluding Color itself.
- **UFO multiclass:** reported country from duration and coordinates. A geographic lookup is more appropriate for actual border identification.
- **Review sentiment binary:** positive versus negative text, using the NLP lesson’s labeled reviews and training-only text vectorization.

A basket containing star anise, artichokes, cauliflower, and horseradish could be scored by a cuisine classifier, but the result does not establish that a complete or typical Indian dish can be made. Ingredients alone omit amounts, preparation, substitutions, and regional context.

## Assignment

The [five-algorithm Word table](classification-methods.docx) pairs logistic regression, K-nearest neighbors, Bernoulli naive Bayes, decision trees, and random forests with curriculum datasets, targets, preprocessing, and evaluation limitations. It uses the modern `.docx` Word format. Its one-page landscape rendering was visually checked.

## Review and sources

[SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html) addresses minority-class scarcity by interpolating neighbors. It needs meaningful feature distances and sufficient minority examples; it can create unrealistic combinations or amplify noise. For binary ingredients, class weighting or random oversampling is often easier to interpret. Any resampling must happen within training folds. Balancing is not a guarantee of improvement.

See the [Scikit-learn classifier guide](https://scikit-learn.org/stable/supervised_learning.html) and the method references in the Word document. Quiz answers are in [the Classification key](../quiz-answers.md).
