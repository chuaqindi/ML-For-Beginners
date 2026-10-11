# Introduction and Regression Quiz Answers

Answers follow the English quiz data in `quiz-app/src/assets/translations/en.json`.

## Quiz 1: Introduction to Machine Learning — Pre-Lecture

1. Applications of machine learning are all around us.  
   **Answer:** True  
   Recommendation systems, spam filters, fraud detection, and search ranking are common examples.
2. What is the technical difference between classical ML and deep learning?  
   **Answer:** the use of neural networks  
   Deep learning uses multilayer neural networks, while this course concentrates on classical algorithms.
3. Why might a business want to use ML strategies?  
   **Answer:** both of the above  
   ML can automate complex decisions and personalize services from patterns in data.

## Quiz 2: Introduction to Machine Learning — Post-Lecture

1. Machine learning algorithms are meant to simulate:  
   **Answer:** the human brain  
   The lesson uses human pattern learning as a broad analogy for machine learning.
2. What is an example of a classical ML technique?  
   **Answer:** natural language processing  
   NLP tasks can be solved with classical methods such as bag-of-words features and linear classifiers.
3. Why should everyone learn the basics of ML?  
   **Answer:** both of the above  
   ML is accessible to learners and increasingly affects decisions across many industries.

## Quiz 3: History of Machine Learning — Pre-Lecture

1. Approximately when was the term “artificial intelligence” coined?  
   **Answer:** 1950s  
   The term became established around the 1956 Dartmouth workshop.
2. Who was one of the early pioneers of machine learning?  
   **Answer:** Alan Turing  
   Turing's work on computation and machine intelligence helped establish the field's foundations.
3. Why did advancement in AI slow in the 1970s?  
   **Answer:** Limited compute power  
   Early ambitions exceeded the available hardware, data, and practical algorithmic capability.

## Quiz 4: History of Machine Learning — Post-Lecture

1. What is an example of a “scruffy” AI system?  
   **Answer:** ELIZA  
   ELIZA produced useful-looking dialogue through pragmatic pattern matching rather than a complete formal model.
2. What technology was developed during “The Golden Years”?  
   **Answer:** Blocks world  
   Blocks-world systems provided constrained environments for research into reasoning and language.
3. Which event helped create and expand artificial intelligence as a field?  
   **Answer:** Dartmouth Summer Research Project  
   The 1956 workshop brought researchers together around a named research program for AI.

## Quiz 5: Fairness and Machine Learning — Pre-Lecture

1. Unfairness in machine learning can happen:  
   **Answer:** both of the above  
   Harm may arise intentionally or unintentionally through choices about data, objectives, and deployment.
2. The term “unfairness” in ML connotes:  
   **Answer:** harms for a group of people  
   Fairness analysis examines how system outcomes disadvantage groups, including protected groups.
3. The five main types of harms include:  
   **Answer:** allocation, quality of service, stereotyping, denigration, and over- or under-representation  
   These categories cover both material outcomes and representational harms.

## Quiz 6: Fairness and Machine Learning — Post-Lecture

1. Unfairness in a model can be caused by:  
   **Answer:** over reliance on historical data  
   Historical records can encode past discrimination and reproduce it in predictions.
2. To mitigate unfairness, you can:  
   **Answer:** both the above  
   Teams should identify affected groups and define relevant fairness measures before comparing solutions.
3. Fairlearn is a package that can:  
   **Answer:** compare multiple models by using fairness and performance metrics  
   Its metrics help expose trade-offs rather than deciding what fairness means for stakeholders.

## Quiz 7: Tools and Techniques — Pre-Lecture

1. When building a model, you should:  
   **Answer:** prepare your data, then train your model  
   Cleaning and transforming data is necessary before a model can learn reliable patterns.
2. Your data's ___ will impact the quality of your ML model.  
   **Answer:** both of the above  
   Both the amount and quality of data affect what a model can learn.
3. A feature variable is:  
   **Answer:** a measurable property of your data  
   Features are the input measurements supplied to a learning algorithm.

## Quiz 8: Tools and Techniques — Post-Lecture

1. You should visualize your data because:  
   **Answer:** both of these  
   Plots reveal structure and potential data-quality problems that summary numbers can hide.
2. Split your data into:  
   **Answer:** training and test sets  
   Training data fits the model; held-out test data estimates performance on unseen examples.
3. A common command to start training in ML libraries is:  
   **Answer:** model.fit  
   Scikit-learn estimators conventionally learn parameters through their `fit` method.

## Quiz 9: Introduction to Regression — Pre-Lecture

1. Which variable is numeric?  
   **Answer:** Height  
   Height can be measured on a numeric scale.
2. Which variable is categorical?  
   **Answer:** Blood Type  
   Blood type represents one of a finite set of labels rather than a continuous measurement.
3. Which problem is regression-based?  
   **Answer:** Predicting the final exam marks of a student  
   Exam marks are numeric values, making their prediction a regression task.

## Quiz 10: Introduction to Regression — Post-Lecture

1. Training accuracy is 95% and testing accuracy is 30%. What is this condition?  
   **Answer:** Overfitting  
   The large gap indicates that the model learned the training data but generalizes poorly.
2. Identifying significant features from a set of features is called:  
   **Answer:** Feature Selection  
   Feature selection retains useful existing inputs while removing less informative ones.
3. Splitting a dataset into training and testing sets is called:  
   **Answer:** Hold-Out Validation  
   A held-out subset provides an evaluation set not used for fitting.

## Quiz 11: Prepare and Visualize Data for Regression — Pre-Lecture

1. Which Python module is used to plot data?  
   **Answer:** Matplotlib  
   Matplotlib provides the foundational plotting API used throughout these lessons.
2. To understand the spread and characteristics of data points, perform:  
   **Answer:** Data Visualization  
   Appropriate plots make distributions, clusters, and outliers easier to see.
3. Which is part of data visualization in an ML project?  
   **Answer:** Creating a pictorial representation of data using different plotting methods  
   Visual encodings translate variables and relationships into interpretable charts.

## Quiz 12: Prepare and Visualize Data for Regression — Post-Lecture

1. How do you check missing values in a pandas DataFrame named `dataset`?  
   **Answer:** dataset.isnull().sum()  
   `isnull` marks missing entries and `sum` counts them by column.
2. Which plot helps compare the spread of different groups of data points?  
   **Answer:** Bar Plot  
   In the lesson, grouped bars summarize and compare values across categories.
3. What can data visualization not tell you?  
   **Answer:** The source from where the dataset is collected  
   Provenance must come from dataset documentation and cannot be inferred reliably from a chart.

## Quiz 13: Linear and Polynomial Regression — Pre-Lecture

1. Matplotlib is a:  
   **Answer:** data visualization library  
   It creates static, animated, and interactive plots in Python.
2. Linear regression represents relationships using:  
   **Answer:** a straight line  
   The fitted coefficients define a linear relationship between predictors and the response.
3. A good linear regression model has a ___ correlation coefficient.  
   **Answer:** high  
   A strong linear association can support a useful linear model, though test metrics remain essential.

## Quiz 14: Linear and Polynomial Regression — Post-Lecture

1. If data is nonlinear, try a ___ type of regression.  
   **Answer:** polynomial  
   Polynomial features allow a linear estimator to represent curved relationships.
2. These are all regression methods:  
   **Answer:** Stepwise, Ridge, Lasso and Elasticnet  
   They select, constrain, or regularize regression coefficients in different ways.
3. Least-squares regression means residuals are:  
   **Answer:** squared and then added up  
   Fitting minimizes the sum of squared differences between observations and predictions.

## Quiz 15: Logistic Regression — Pre-Lecture

1. Use logistic regression to predict:  
   **Answer:** whether an apple is ripe or not  
   A ripe/not-ripe label is a binary classification target.
2. Types of logistic regression include:  
   **Answer:** multinomial and ordinal  
   Multinomial targets are unordered classes, while ordinal targets have a meaningful order.
3. Your data has weak correlations. The quiz's suggested regression type is:  
   **Answer:** Logistic  
   Logistic regression models class probabilities and is appropriate when the target is categorical.

## Quiz 16: Logistic Regression — Post-Lecture

1. Seaborn is a type of:  
   **Answer:** data visualization library  
   Seaborn builds statistical plotting functions on top of Matplotlib.
2. A confusion matrix is also known as an:  
   **Answer:** error matrix  
   It tabulates predicted classes against actual classes to expose error types.
3. A good model will have:  
   **Answer:** a large number of true positives and true negatives in its confusion matrix  
   Correct classifications appear on the matrix diagonal for a binary task.
