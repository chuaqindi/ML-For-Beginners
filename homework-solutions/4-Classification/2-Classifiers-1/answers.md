# Cuisine classifiers and solvers

## Exercise

The [executed notebook](notebook.ipynb) evaluates two logistic formulations on the same grouped 1,960/488 split. LIBLINEAR one-versus-rest gives accuracy **0.8340**, macro F1 **0.8094**; multinomial L-BFGS gives accuracy **0.8258**, macro F1 **0.8015**. The difference is small on a single split and also reflects different multiclass objectives, so it is not proof that one solver is universally better.

Three held-out rows are inspected with ingredient lists and full probability vectors. The first receives an Indian probability rounded to 1.000. Cumin, yogurt, and cardamom have positive Indian-class coefficients in the fitted model and appear in its ingredient list. These associations help explain the score but do not establish causality, authenticity, or calibrated certainty. Class weighting changes the fitting emphasis; probabilities should be calibrated before being used for consequential decisions.

## Assignment and challenge

The [solver comparison Word document](solver-comparison.docx) contains the requested comparison paragraphs, with a short introduction and source. Its one-page rendering was visually checked.

LIBLINEAR solves regularized binary logistic-regression problems and works with dense or sparse feature matrices. Its coordinate-descent methods update model variables iteratively; the exact formulation depends on the selected penalty and primal or dual setting. It supports L1 and L2 penalties, which makes it useful for a small or medium binary task or when sparse coefficients are wanted. For our five cuisine labels, I wrap it in OneVsRestClassifier, fitting one binary problem per cuisine. That is easy to interpret but does not directly optimize a joint multinomial objective. The binary ingredient matrix suits this approach; for a much larger dataset I would compare more scalable solvers rather than assuming it remains fastest.

L-BFGS uses a limited-memory approximation to curvature to choose successive optimization steps, avoiding storage of a full Hessian. In Scikit-learn logistic regression it supports the joint multinomial objective and L2 or no regularization, but not an L1 penalty. It accepts dense and sparse input; similarly scaled features and a sufficient iteration limit help convergence. I would choose it as the starting point for our moderate-sized five-class cuisine problem because it learns the classes jointly without five separate binary fits. I would choose LIBLINEAR instead when binary classification and L1 sparsity are priorities. Our notebook compares LIBLINEAR with one-versus-rest against multinomial L-BFGS, so differences reflect the multiclass formulation as well as the solver; they are not a pure speed or solver-quality comparison.

## Sources and limits

[Logistic regression guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) and [estimator API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html). The executed environment is Scikit-learn 1.7.2; explicit OneVsRestClassifier avoids relying on the deprecated `multi_class` parameter. This small recipe collection does not represent every regional cuisine. [Quiz answers](../quiz-answers.md).
