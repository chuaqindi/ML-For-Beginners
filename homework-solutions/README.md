# Introduction and Regression Homework Solutions

This portfolio covers the in-repository quizzes, challenges, notebook exercises, and assignments for all eight lessons in `1-Introduction` and `2-Regression`. It uses Python only and leaves the curriculum, solution, and translation files unchanged.

## Environment

The package bounds are recorded in [requirements.txt](requirements.txt). From the repository root, install them with:

```bash
/opt/anaconda3/bin/python -m pip install -r homework-solutions/requirements.txt
```

Each notebook is self-contained and is run from its own directory with `/opt/anaconda3/bin/jupyter`, a 300-second timeout, and Matplotlib/Jupyter cache directories under `/tmp`.

## Portfolio checklist

- [x] **Complete:** [Quiz answer key for English quiz IDs 1–16](quiz-answers.md)

### 1 — Introduction

- [x] **Complete:** [Introduction to machine learning challenge and assignment status](1-Introduction/1-intro-to-ML/answers.md)
- [x] **Complete:** [Machine learning history research](1-Introduction/2-history-of-ML/answers.md) and [local interactive timeline](1-Introduction/2-history-of-ML/timeline/index.html)
- [x] **Complete:** [Fairness challenge and assignment status](1-Introduction/3-fairness/answers.md)
- [x] **Complete:** [Machine learning techniques workflow and assignment status](1-Introduction/4-techniques-of-ML/answers.md)

### 2 — Regression

- [x] **Complete:** Regression tools [written answers](2-Regression/1-Tools/answers.md) and [executed notebook](2-Regression/1-Tools/notebook.ipynb)
- [x] **Complete:** Regression data [written answers](2-Regression/2-Data/answers.md) and [executed notebook](2-Regression/2-Data/notebook.ipynb)
- [x] **Complete:** Linear and polynomial regression [written answers](2-Regression/3-Linear/answers.md) and [executed notebook](2-Regression/3-Linear/notebook.ipynb)
- [x] **Complete:** Logistic regression [written answers](2-Regression/4-Logistic/answers.md) and [executed notebook](2-Regression/4-Logistic/notebook.ipynb)

## Approved exclusions

- [ ] **Skipped — approved exclusion:** External environment-training courses and videos — completion would require participation outside this repository.
- [ ] **Skipped — approved exclusion:** External Responsible AI notebook — no external run or personal observations were fabricated.
- [ ] **Skipped — approved exclusion:** Data-scientist interview — no interview or personal reflection was fabricated.
- [ ] **Skipped — approved exclusion:** Cloud deployment — the history timeline is a local buildless site and was not presented as deployed.

## Verification

Verification date: **2026-10-12**.

- All four notebooks were executed from their containing directories with saved outputs.
- The portfolio contract passes with `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -v`.
- Local index links, quiz counts, approved exclusions, notebook execution state, and required lesson content are covered by the contract.
