# Introduction and Regression Homework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a Python solution portfolio for every non-excluded quiz, challenge, notebook exercise, and assignment in `1-Introduction` and `2-Regression`.

**Architecture:** Add an isolated `homework-solutions/` tree that mirrors the eight source lessons and links all artifacts from one index. Written work stays in Markdown, the history timeline is a buildless local site, and each Regression lesson gets one self-contained executed notebook covering its lesson exercise, challenge, and assignment work.

**Tech Stack:** Markdown, HTML/CSS, Python 3.12, Jupyter, NumPy, pandas, Matplotlib, Seaborn, Scikit-learn, standard-library `unittest`

**Spec:** `docs/superpowers/specs/2026-10-12-introduction-regression-homework-design.md`

## Global Constraints

- Work only in `homework-solutions/`; do not edit curriculum, `solution/`, or `translations/` files.
- Implement Python only; do not create R duplicates.
- Skip external training, the Responsible AI notebook report, the data-scientist interview, and cloud deployment; identify each skip explicitly.
- Do not fabricate personal observations or execution results.
- Reuse `2-Regression/data/US-pumpkins.csv`, Scikit-learn datasets, and installed packages; add no dependency.
- Run notebooks from their containing directories and save all outputs.
- Use `/opt/anaconda3/bin/python` and `/opt/anaconda3/bin/jupyter`; set Matplotlib/Jupyter cache directories under `/tmp` during verification.

## Review Focus

- Notebook data paths must resolve when execution starts in the notebook's own directory; test all four that way in Task 10.
- Pumpkin preprocessing must exclude the target, handle missing values, and avoid train/test leakage; assert the pipeline fits only on training data in Task 9.
- Conclusions from the 20-row Linnerud dataset must be framed as exploratory, not causal; check the limitation in Task 6.
- Quiz answers must map exactly to English quiz IDs 1–16 (48 questions); pin both counts in Task 2.
- Approved skips must be visibly distinguished from accidentally missing work; pin every skip label in Task 10.

---

### Task 1: Portfolio Contract and Validator

**Files:**
- Create: `homework-solutions/README.md`
- Create: `homework-solutions/requirements.txt`
- Create: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: `PORTFOLIO_ROOT: pathlib.Path`, `REQUIRED_NOTEBOOKS: tuple[str, ...]`, and `assert_executed_notebook(test_case, relative_path)` in `test_portfolio.py` for later tasks.
- Consumes: Nothing.

- [ ] **Step 1: Write the failing scaffold test**

Add `PortfolioTests.test_index_and_manifest_exist`, asserting that `README.md` and `requirements.txt` exist under `PORTFOLIO_ROOT`.

- [ ] **Step 2: Run it and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the index and manifest do not exist.

- [ ] **Step 3: Add the minimal scaffold**

Create a title and incomplete checklist in `README.md`. Record compatible bounds in `requirements.txt`: `jupyter>=1,<2`, `matplotlib>=3.8,<4`, `nbclient>=0.8,<1`, `nbformat>=5.9,<6`, `numpy>=1.26,<3`, `pandas>=2.2,<3`, `scikit-learn>=1.7,<2`, and `seaborn>=0.13,<1`; do not install anything.

- [ ] **Step 4: Run the test and verify GREEN**

Run the command from Step 2. Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions
git commit -m "test: define homework portfolio contract"
```

### Task 2: Quiz Answer Key

**Files:**
- Create: `homework-solutions/quiz-answers.md`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Consumes: quiz IDs 1–16 from `quiz-app/src/assets/translations/en.json`.
- Produces: sixteen `## Quiz <id>:` headings and forty-eight `**Answer:**` entries.

- [ ] **Step 1: Add the failing quiz-count test**

Add `PortfolioTests.test_quiz_key_covers_ids_1_through_16`, asserting the heading IDs equal `range(1, 17)` and the answer marker count is 48.

- [ ] **Step 2: Run it and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because `quiz-answers.md` is missing.

- [ ] **Step 3: Write the answer key**

For each question, include the question, the `isCorrect == "true"` answer from the English JSON, and one original sentence explaining the concept.

- [ ] **Step 4: Run the test and verify GREEN**

Run the command from Step 2. Expected: PASS with 16 quizzes and 48 answers.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/quiz-answers.md homework-solutions/tests/test_portfolio.py
git commit -m "docs: answer introduction and regression quizzes"
```

### Task 3: Introduction to ML Answers

**Files:**
- Create: `homework-solutions/1-Introduction/1-intro-to-ML/answers.md`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: `## Challenge` with a Mermaid relationship diagram and problem examples; `## Assignment — Skipped` with the approved external-training reason.
- Consumes: Nothing.

- [ ] **Step 1: Add a failing structure test**

Add `PortfolioTests.test_intro_ml_has_diagram_and_skip`, asserting the file contains a Mermaid fence, both required headings, and `external training`.

- [ ] **Step 2: Run it and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the answer file is missing.

- [ ] **Step 3: Write the minimal complete answer**

Explain AI as the umbrella, ML as pattern learning, deep learning as neural-network ML, and data science as the broader data practice. Give at least two suitable problem examples per field and record the non-graded external setup assignment as skipped.

- [ ] **Step 4: Run the suite and verify GREEN**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/1-Introduction homework-solutions/tests/test_portfolio.py
git commit -m "docs: complete introduction to ML homework"
```

### Task 4: History Research and Local Timeline

**Files:**
- Create: `homework-solutions/1-Introduction/2-history-of-ML/answers.md`
- Create: `homework-solutions/1-Introduction/2-history-of-ML/timeline/index.html`
- Create: `homework-solutions/1-Introduction/2-history-of-ML/timeline/styles.css`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: an accessible, responsive, buildless timeline with at least eight dated events, source links, and two embedded multimedia elements.
- Consumes: facts and links already cited in the lesson; no hosting identity or deployment.

- [ ] **Step 1: Add failing timeline tests**

Add `PortfolioTests.test_history_timeline_has_events_and_media`, asserting eight `data-year` attributes, two `<iframe` elements, a linked stylesheet, a `<main>` landmark, and source links.

- [ ] **Step 2: Run it and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the history artifacts are missing.

- [ ] **Step 3: Write the history answer and timeline**

Focus the challenge on the Dartmouth workshop and its participants in cultural context. Build the local timeline from early neural models through modern ML, using semantic HTML and a single CSS file; label deployment as excluded rather than completed.

- [ ] **Step 4: Verify GREEN and preview locally**

Run the unit suite, then run `/opt/anaconda3/bin/python -m http.server 8765 --directory homework-solutions/1-Introduction/2-history-of-ML/timeline` and inspect desktop/mobile layout and keyboard-readable structure using the Sites local-only workflow. Expected: tests PASS and the local page renders without console or asset errors.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/1-Introduction/2-history-of-ML homework-solutions/tests/test_portfolio.py
git commit -m "docs: add machine learning history timeline"
```

### Task 5: Fairness and ML-Process Answers

**Files:**
- Create: `homework-solutions/1-Introduction/3-fairness/answers.md`
- Create: `homework-solutions/1-Introduction/4-techniques-of-ML/answers.md`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: a concrete fairness scenario with mitigations; a Mermaid ML lifecycle flowchart; explicit skip notes for the external RAI run, personal reflection, and interview.
- Consumes: Nothing.

- [ ] **Step 1: Add failing coverage tests**

Add separate tests asserting the fairness answer names allocation, data representation, subgroup evaluation, appeal, and monitoring, and the techniques answer contains the seven lesson workflow stages plus a Mermaid fence and approved skip labels.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because both answer files are missing.

- [ ] **Step 3: Write both answers**

Use a lending example for the fairness challenge and describe preventative controls without claiming a dashboard was run. Diagram question definition, data collection/preparation, method selection, training, evaluation, tuning, and prediction; omit invented personal claims.

- [ ] **Step 4: Run the suite and verify GREEN**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/1-Introduction homework-solutions/tests/test_portfolio.py
git commit -m "docs: complete fairness and techniques homework"
```

### Task 6: Regression Tools Notebook

**Files:**
- Create: `homework-solutions/2-Regression/1-Tools/answers.md`
- Create: `homework-solutions/2-Regression/1-Tools/notebook.ipynb`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: an executed notebook comparing at least two diabetes features and visualizing Linnerud exercise/physiology relationships; a descriptive Linnerud answer that states the 20-row limitation.
- Consumes: `sklearn.datasets.load_diabetes`, `sklearn.datasets.load_linnerud`.

- [ ] **Step 1: Register the notebook and add failing tests**

Add the path to `REQUIRED_NOTEBOOKS`; add `test_linnerud_answer_is_exploratory`, asserting the answer covers situps/waist plus the small-sample and non-causal limitations.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the notebook and answer are absent.

- [ ] **Step 3: Create and execute the notebook**

Use deterministic splits (`random_state=42`), linear regression, R²/RMSE, labeled plots, and assertions for expected shapes and finite metrics. Compare the lesson's diabetes BMI feature with blood pressure, then plot the nine Linnerud feature-target relationships with fitted lines.

- [ ] **Step 4: Verify GREEN**

From `homework-solutions/2-Regression/1-Tools`, run `env MPLCONFIGDIR=/tmp/mlfb-mpl JUPYTER_RUNTIME_DIR=/tmp/mlfb-jupyter IPYTHONDIR=/tmp/mlfb-ipython /opt/anaconda3/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebook.ipynb`, then run the unit suite from the repository root. Expected: no error outputs and every code cell executed.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/2-Regression/1-Tools homework-solutions/tests/test_portfolio.py
git commit -m "feat: complete regression tools homework"
```

### Task 7: Regression Data Notebook

**Files:**
- Create: `homework-solutions/2-Regression/2-Data/answers.md`
- Create: `homework-solutions/2-Regression/2-Data/notebook.ipynb`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: executed pumpkin-data exploration using both Matplotlib and Seaborn, with at least two substantive visualizations and an ease-of-use comparison.
- Consumes: `../../../2-Regression/data/US-pumpkins.csv` from the notebook directory.

- [ ] **Step 1: Add failing notebook/content tests**

Register the notebook and add `test_data_answers_compare_plotting_libraries`, asserting named Matplotlib and Seaborn sections and regression-appropriate plot guidance.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the notebook and answer are absent.

- [ ] **Step 3: Create and execute the notebook**

Clean bushel records, normalize fractional-bushel prices, assert a nonempty numeric price column, and show scatter/regression, distribution, categorical comparison, and correlation views. Explain why scatter/regression/residual plots best expose regression relationships.

- [ ] **Step 4: Verify GREEN**

From `homework-solutions/2-Regression/2-Data`, run `env MPLCONFIGDIR=/tmp/mlfb-mpl JUPYTER_RUNTIME_DIR=/tmp/mlfb-jupyter IPYTHONDIR=/tmp/mlfb-ipython /opt/anaconda3/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebook.ipynb`, then run the unit suite from the repository root. Expected: PASS, with saved plots and no warnings or errors.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/2-Regression/2-Data homework-solutions/tests/test_portfolio.py
git commit -m "feat: complete regression data homework"
```

### Task 8: Linear and Polynomial Regression Notebook

**Files:**
- Create: `homework-solutions/2-Regression/3-Linear/answers.md`
- Create: `homework-solutions/2-Regression/3-Linear/notebook.ipynb`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: executed pumpkin feature/correlation experiments and a fresh Scikit-learn diabetes regression model comparing linear and polynomial techniques with R², MAE, and RMSE.
- Consumes: pumpkin CSV path from Task 7 and `sklearn.datasets.load_diabetes`.

- [ ] **Step 1: Add failing notebook/content tests**

Register the notebook and add `test_linear_answers_explain_model_choice_and_accuracy`, asserting the answer discusses correlation versus predictive accuracy, technique choice, and limitations.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the notebook and answer are absent.

- [ ] **Step 3: Create and execute the notebook**

Compare Month and DayOfYear pumpkin models under the same deterministic split. Build a fresh diabetes model, compare degree-1 and degree-2 pipelines without fitting preprocessing on test data, report all three metrics, choose the simpler model unless the polynomial test metrics materially improve, and assert finite results.

- [ ] **Step 4: Verify GREEN**

From `homework-solutions/2-Regression/3-Linear`, run `env MPLCONFIGDIR=/tmp/mlfb-mpl JUPYTER_RUNTIME_DIR=/tmp/mlfb-jupyter IPYTHONDIR=/tmp/mlfb-ipython /opt/anaconda3/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebook.ipynb`, then run the unit suite. Expected: PASS with saved finite metrics and plots.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/2-Regression/3-Linear homework-solutions/tests/test_portfolio.py
git commit -m "feat: complete linear regression homework"
```

### Task 9: Logistic Regression Notebook

**Files:**
- Create: `homework-solutions/2-Regression/4-Logistic/answers.md`
- Create: `homework-solutions/2-Regression/4-Logistic/notebook.ipynb`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Produces: an executed full-pumpkin multiclass color model and a separate breast-cancer logistic-regression challenge, each with confusion matrix and F1-based evaluation.
- Consumes: pumpkin CSV path and `sklearn.datasets.load_breast_cancer`.

- [ ] **Step 1: Add failing notebook/content tests**

Register the notebook and add `test_logistic_answers_cover_cleaning_standardization_and_imbalance`, asserting those three topics plus model limitations are discussed.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL because the notebook and answer are absent.

- [ ] **Step 3: Create and execute the notebook**

For pumpkins, retain all rows with a known color, discard only empty/unnamed fields, derive date parts, stratify the split, and fit a `Pipeline(ColumnTransformer(...), LogisticRegression(class_weight="balanced", max_iter=2000))`. Impute and standardize numeric columns, impute and one-hot categorical columns with unknown-category handling, report macro F1 and a confusion matrix, and assert the target never enters preprocessing. For the challenge, standardize breast-cancer features inside a pipeline and report accuracy, F1, ROC AUC, and confusion matrix.

- [ ] **Step 4: Verify GREEN**

From `homework-solutions/2-Regression/4-Logistic`, run `env MPLCONFIGDIR=/tmp/mlfb-mpl JUPYTER_RUNTIME_DIR=/tmp/mlfb-jupyter IPYTHONDIR=/tmp/mlfb-ipython /opt/anaconda3/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebook.ipynb`, then run the unit suite. Expected: finite metrics, no convergence warning, and no error outputs.

- [ ] **Step 5: Commit**

```bash
git add homework-solutions/2-Regression/4-Logistic homework-solutions/tests/test_portfolio.py
git commit -m "feat: complete logistic regression homework"
```

### Task 10: Index, Re-execution, and Final Audit

**Files:**
- Modify: `homework-solutions/README.md`
- Modify: `homework-solutions/tests/test_portfolio.py`

**Interfaces:**
- Consumes: every artifact produced by Tasks 2–9.
- Produces: a complete linked checklist with statuses `Complete` or `Skipped — approved exclusion`.

- [ ] **Step 1: Add failing final-contract tests**

Add `test_index_links_every_required_artifact`, `test_all_approved_skips_are_labeled`, and `test_all_required_notebooks_execute_cleanly`. Resolve each relative Markdown link and require exactly four approved skip categories from the spec.

- [ ] **Step 2: Run and verify RED**

Run: `/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -p 'test_portfolio.py' -v`

Expected: FAIL while the index is incomplete.

- [ ] **Step 3: Complete the index**

Link all lesson answers, four notebooks, the timeline, and the quiz key. Record scope, environment command, verification date, and each approved skip without claiming cloud deployment.

- [ ] **Step 4: Re-execute and verify everything**

Execute all four notebooks from their own directories with a 300-second timeout and writable `/tmp` cache directories. Then run:

```bash
/opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -v
git diff --check
git status --short
```

Expected: all tests PASS, no notebook errors, no whitespace errors, and only intended files changed.

- [ ] **Step 5: Perform visual and rubric QA**

Preview the history timeline at desktop and mobile sizes. Inspect every notebook's saved plots and final metrics. Compare the index once against all eight source READMEs, assignment files, and quiz IDs 1–16.

- [ ] **Step 6: Commit**

```bash
git add homework-solutions
git commit -m "docs: finalize introduction and regression portfolio"
```
