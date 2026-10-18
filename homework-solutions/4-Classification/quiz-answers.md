# Classification quiz answers

Answers follow English quiz IDs 19–26 in the repository. Clarifications distinguish the expected quiz wording from stronger statistical claims.

## Quiz 19: Classification 1: Pre-Lecture Quiz

1. Classification is a form of supervised learning that has a lot in common with  
   **Answer:** Regression techniques  
   Both learn from labeled examples; regression predicts a numeric quantity while classification predicts a category.
2. What question can classification help answer?  
   **Answer:** Is this email spam or not?  
   Spam detection has two target labels and is a binary classification task.
3. What is the first step to using Classification techniques?  
   **Answer:** cleaning and balancing your data  
   This is the quiz’s expected answer. In an evaluated pipeline, split first and balance only training data; balancing is optional and should be tested.

## Quiz 20: Classification 1: Post-Lecture Quiz

1. What is a multiclass question?  
   **Answer:** the task of classifying data points into one of several classes  
   Each example receives one label from more than two possible classes.
2. It's important to clean out recurrent or unhelpful data to help your classifiers solve your problem.  
   **Answer:** true  
   Remove identifiers and leakage, but verify whether recurring features are actually unhelpful rather than discarding them automatically.
3. What's the best reason to balance your data?  
   **Answer:** Balancing your data yields better results because an ML model won't skew towards one class  
   This is the quiz’s intended rationale, not a guarantee: balancing can improve minority learning but must be checked on original held-out data.

## Quiz 21: Classification 2: Pre-Lecture Quiz

1. Balanced, clean data yields the best classification results  
   **Answer:** true  
   The quiz expects true; clean data matters, while balancing can help or hurt depending on the data and metric.
2. How do you choose the right classifier?  
   **Answer:** Both of the above  
   Use the estimator guide to shortlist candidates, then compare suitable methods with validation data.
3. Classification is a type of  
   **Answer:** Supervised Learning  
   Training examples include target labels for the model to learn.

## Quiz 22: Classification 2: Post-Lecture Quiz

1. What is a 'solver'?  
   **Answer:** the algorithm to use in the optimization problem  
   The solver numerically optimizes the estimator’s objective; it is distinct from the task and model family.
2. Which classifier did we use in this lesson?  
   **Answer:** Logistic Regression  
   Logistic regression maps feature scores to class probabilities despite having regression in its name.
3. How do you know if the classification algorithm is working as expected?  
   **Answer:** By checking the accuracy of its predictions  
   Accuracy checks held-out predictions; also inspect per-class recall and macro F1 when classes are uneven.

## Quiz 23: Classification 3: Pre-Lecture Quiz

1. A good initial classifier to try is:  
   **Answer:** Linear SVC  
   A linear margin classifier supplies a useful baseline before adding nonlinear complexity.
2. Regularization controls:  
   **Answer:** the influence of parameters  
   Regularization constrains the fitted parameters to reduce overfitting; too much can underfit.
3. K-Neighbors classifier can be used for:  
   **Answer:** both of these  
   Neighbor methods support both classification and regression through different aggregation rules.

## Quiz 24: Classification 3: Post-Lecture Quiz

1. Support-Vector classifiers can be used for  
   **Answer:** both of these  
   Support-vector methods have both classification and regression variants.
2. Random Forest is a ___ type of classifier  
   **Answer:** Ensemble  
   A forest aggregates many randomized decision trees.
3. Adaboost is known for:  
   **Answer:** focusing on the weights of incorrectly classified items  
   Boosting raises the influence of examples that earlier stages handled poorly.

## Quiz 25: Classification 4: Pre-Lecture Quiz

1. Recommendation systems might be used for  
   **Answer:** Both of these  
   Recommenders can support multiple application domains by relating inputs to candidate choices.
2. Embedding a model in a web app helps it to be offline-capable  
   **Answer:** true  
   Local inference can work offline only when model files and runtime assets are also available locally or cached.
3. Onnx Runtime can be used for  
   **Answer:** Running models in a web app  
   ONNX Runtime executes compatible exported models, including in browser applications.

## Quiz 26: Classification 4: Post-Lecture Quiz

1. Netron app helps you:  
   **Answer:** Visualize your model's structure  
   Netron displays the model graph, tensor information, and operators rather than training a model.
2. Convert your Scikit-learn model for use with Onnx using:  
   **Answer:** sklearn-onnx  
   The sklearn-onnx project, imported as skl2onnx, converts supported Scikit-learn estimators.
3. Using your model in a web app is called:  
   **Answer:** inference  
   Inference applies a fitted model to new feature values; training estimates its parameters.
