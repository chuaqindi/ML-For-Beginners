# Techniques of Machine Learning

## Challenge

The seven lesson stages form an iterative workflow:

```mermaid
flowchart TD
    Q[Decide on the question] --> D[Collect and prepare data]
    D --> M[Choose a training method]
    M --> T[Train the model]
    T --> E[Evaluate the model]
    E --> U[Parameter tuning]
    U -->|Retrain with selected parameters| T
    U -->|Meets evaluation criteria| P[Predict]
```

1. **Decide on the question:** Define the target, intended users, and success criteria; check whether a simple rule would suffice.
2. **Collect and prepare data:** Document sources and representation, clean the data, and separate training, validation, and test examples. Fit preprocessing only on training data to prevent leakage.
3. **Choose a training method:** Match the problem to a suitable approach, such as supervised regression for a numeric target, and choose a simple baseline.
4. **Train the model:** Fit the selected method to training features and their targets.
5. **Evaluate the model:** Use validation data or cross-validation during development to assess errors, overfitting, and subgroup performance. Reserve the untouched test set for the final assessment after tuning.
6. **Parameter tuning:** Adjust hyperparameters using validation results and retrain. Revisit the data or method if the model still fails the agreed criteria.
7. **Predict:** Apply the selected model and its fitted preprocessing to new inputs. Monitor outcomes and return to earlier stages when performance changes.

## Reflection — grounded in this portfolio

**Current stage:** This portfolio has completed the workflow through evaluation and prediction. Its notebooks prepare data, fit models, evaluate held-out examples, and explain their limitations. The [local pumpkin app](../../3-Web-App/1-Web-App/answers.md) also demonstrates applying an exported model to a new input. Reaching prediction completes the classroom workflow; the app's poor held-out score still limits its usefulness.

**Likely difficulties:** Defining the question and selecting a valid evaluation are the hardest parts to carry into a new project. Duplicate recipes must stay in one partition, time-series forecasts must use earlier observations, and preprocessing must learn only from training data. The [Nile experiment](../../7-TimeSeries/2-ARIMA/answers.md) also shows that a more complicated model can lose to a simple baseline. These examples make representative data and honest comparisons more consequential than successfully calling `fit`.

**Most straightforward parts:** Loading documented data, drawing labeled plots, and fitting a baseline are the most repeatable steps in the completed notebooks. Existing Pandas, Matplotlib, and Scikit-learn patterns make those mechanics easier to reproduce. Interpreting an apparent improvement remains harder: it requires checking the split, minority errors, and whether the result answers the original question.

## Assignment — Skipped

The data scientist interview requires external participation and is excluded under the approved scope. No interview, attributed testimony, or account of a professional's daily work is fabricated.
