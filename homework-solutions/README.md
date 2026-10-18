# Machine Learning Homework Solutions

This portfolio contains the in-repository quizzes, challenges, notebook exercises, and assignments through `9-Real-World`, with the limits listed below. It primarily uses Python; the applied classification lesson uses JavaScript for browser inference. The curriculum, original solution files, and translations are unchanged.

The portfolio now includes 27 executed notebooks and all 52 quizzes in the English question bank. The remaining sections add forecasting studies, successful Q-learning experiments, an editable PowerPoint proposal, and a local model audit. The poetry assignment uses a documented substitute dataset. The translation exercise is executed through a documented replacement for the retired TextBlob API, and both pending web-app browser checks are complete. External RAI execution remains excluded.

## Environment

Use Python **3.10 or later**. Package bounds are recorded in [requirements.txt](requirements.txt). From the repository root, install them with:

```bash
/opt/anaconda3/bin/python -m pip install -r homework-solutions/requirements.txt
```

Each notebook runs from its own directory. Earlier sections used a 300-second cell timeout; the seven NLP notebooks used clean Jupyter kernels with a 1,200-second cell timeout and temporary cache directories. NLP also requires the corpus and dataset setup in its [data notes](6-NLP/data/README.md).

## Portfolio checklist

- [x] **Complete:** [Quiz answer key for English quiz IDs 1–16](quiz-answers.md)

### 1 — Introduction

- [x] **Complete:** [Introduction to machine learning challenge and assignment status](1-Introduction/1-intro-to-ML/answers.md)
- [x] **Complete:** [Machine learning history research](1-Introduction/2-history-of-ML/answers.md) and [local interactive timeline](1-Introduction/2-history-of-ML/timeline/index.html)
- [x] **Complete:** [Fairness challenge and assignment status](1-Introduction/3-fairness/answers.md)
- [x] **Complete locally:** [Machine learning techniques workflow, portfolio-based reflection, and assignment status](1-Introduction/4-techniques-of-ML/answers.md)

### 2 — Regression

- [x] **Complete:** Regression tools [written answers](2-Regression/1-Tools/answers.md) and [executed notebook](2-Regression/1-Tools/notebook.ipynb)
- [x] **Complete:** Regression data [written answers](2-Regression/2-Data/answers.md) and [executed notebook](2-Regression/2-Data/notebook.ipynb)
- [x] **Complete:** Linear and polynomial regression [written answers](2-Regression/3-Linear/answers.md) and [executed notebook](2-Regression/3-Linear/notebook.ipynb)
- [x] **Complete:** Logistic regression [written answers](2-Regression/4-Logistic/answers.md) and [executed notebook](2-Regression/4-Logistic/notebook.ipynb)

### 3 — Web App

- [x] **Complete locally:** Try a different model — [assignment answers and run instructions](3-Web-App/1-Web-App/answers.md), [training/export script](3-Web-App/1-Web-App/train.py), and [Flask app](3-Web-App/1-Web-App/app.py)
- [x] **Complete:** UFO exercise [executed notebook](3-Web-App/1-Web-App/notebook.ipynb), [Flask training-route challenge](3-Web-App/1-Web-App/ufo_app.py), and architecture review in the assignment answers above.
- [x] **Complete:** [Web App quiz answers, IDs 17–18](3-Web-App/1-Web-App/quiz-answers.md).

### 4 — Classification

- [x] **Complete:** Introduction [answers](4-Classification/1-Introduction/answers.md), [executed notebook](4-Classification/1-Introduction/notebook.ipynb), and [five-algorithm Word table](4-Classification/1-Introduction/classification-methods.docx).
- [x] **Complete:** Classifiers 1 [answers](4-Classification/2-Classifiers-1/answers.md), [executed notebook](4-Classification/2-Classifiers-1/notebook.ipynb), and [solver comparison Word document](4-Classification/2-Classifiers-1/solver-comparison.docx).
- [x] **Complete:** Classifiers 2 [answers](4-Classification/3-Classifiers-2/answers.md) and [executed parameter experiment](4-Classification/3-Classifiers-2/notebook.ipynb).
- [x] **Complete and browser-checked:** Applied classification [answers and instructions](4-Classification/4-Applied/answers.md), [executed ONNX notebook](4-Classification/4-Applied/notebook.ipynb), and [pantry recommender](4-Classification/4-Applied/index.html). Real browser inference, input handling, search, clearing, and desktop/mobile layouts were checked.
- [x] **Complete:** [Classification quizzes 19–26](4-Classification/quiz-answers.md).

### 5 — Clustering

- [x] **Complete:** Visualization [answers](5-Clustering/1-Visualize/answers.md) and [executed notebook with five scatterplots](5-Clustering/1-Visualize/notebook.ipynb).
- [x] **Complete:** K-Means [answers](5-Clustering/2-K-Means/answers.md) and [executed notebook including Ward and DBSCAN alternatives](5-Clustering/2-K-Means/notebook.ipynb).
- [x] **Complete:** [Clustering quizzes 27–30](5-Clustering/quiz-answers.md).

### 6 — Natural Language Processing

- [x] **Complete locally:** Introduction [written answers and bot-analysis paper](6-NLP/1-Introduction-to-NLP/answers.md), [basic bot](6-NLP/1-Introduction-to-NLP/bot.py), and [executed experiment](6-NLP/1-Introduction-to-NLP/notebook.ipynb).
- [x] **Complete locally:** Common tasks [answers](6-NLP/2-Tasks/answers.md), [improved bot](6-NLP/2-Tasks/bot.py), and [executed NLP tasks and conversation](6-NLP/2-Tasks/notebook.ipynb). Scripted tests are recorded; no test on a friend is claimed.
- [x] **Complete with documented dataset substitution:** Sentiment and poetic license [answers](6-NLP/3-Translation-Sentiment/answers.md) and [executed novel/poetry notebook](6-NLP/3-Translation-Sentiment/notebook.ipynb), using the author's available 361-poem Microsoft-scored sample.
- [x] **Complete with documented API replacement:** Four live English-to-French translations in the notebook above, with [saved service responses and provenance](6-NLP/3-Translation-Sentiment/translation-responses.json). MyMemory replaces the retired `TextBlob.translate()` backend; translation-memory matches are distinguished from the explicitly neural result.
- [x] **Complete:** Hotel data exploration [answers](6-NLP/4-Hotel-Reviews-1/answers.md), [executed full-dataset notebook](6-NLP/4-Hotel-Reviews-1/notebook.ipynb), and [executed NLTK book exercises](6-NLP/4-Hotel-Reviews-1/nltk-exercises.ipynb).
- [x] **Complete:** Hotel sentiment and clustering [answers](6-NLP/5-Hotel-Reviews-2/answers.md), [executed filtering and sentiment notebook](6-NLP/5-Hotel-Reviews-2/notebook.ipynb), and [executed movie-review assignment](6-NLP/5-Hotel-Reviews-2/assignment.ipynb).
- [x] **Complete:** [NLP quizzes 31–40](6-NLP/quiz-answers.md), including notes about historical APIs and simplified questions.
- [x] **Recorded:** [NLP data sources, checksums, licences, and reproduction instructions](6-NLP/data/README.md). The full hotel download and generated hotel tables are local, reproducible files ignored by Git.

### 7 — Time Series

- [x] **Complete:** Introduction [answers](7-TimeSeries/1-Introduction/answers.md) and [executed energy exercise and three-dataset assignment](7-TimeSeries/1-Introduction/notebook.ipynb).
- [x] **Complete:** ARIMA [answers](7-TimeSeries/2-ARIMA/answers.md), [executed energy forecast](7-TimeSeries/2-ARIMA/notebook.ipynb), and [executed Nile-flow assignment](7-TimeSeries/2-ARIMA/assignment.ipynb). The answers retain the case where ARIMA loses to a baseline.
- [x] **Complete:** SVR [answers](7-TimeSeries/3-SVR/answers.md), [executed energy tuning experiment](7-TimeSeries/3-SVR/notebook.ipynb), and [executed CO2 assignment](7-TimeSeries/3-SVR/assignment.ipynb).
- [x] **Complete:** [Time-series quizzes 41–44 and 51–52](7-TimeSeries/quiz-answers.md).
- [x] **Recorded:** [Time-series data snapshots, provenance, and reproduction instructions](7-TimeSeries/data/README.md).

### 8 — Reinforcement Learning

- [x] **Complete:** Q-learning [answers](8-Reinforcement/1-QLearning/answers.md) and [executed apple, walk-challenge, and resource-world comparisons](8-Reinforcement/1-QLearning/notebook.ipynb), retaining random-walk evaluation. The [walk challenge results](8-Reinforcement/1-QLearning/walk-challenge-results.csv) demonstrate the move cap and no-revisit rule, including trapped paths.
- [x] **Complete:** Gym [answers](8-Reinforcement/2-Gym/answers.md), [executed CartPole exercise and challenges](8-Reinforcement/2-Gym/notebook.ipynb), and [executed Mountain Car assignment](8-Reinforcement/2-Gym/assignment.ipynb).
- [x] **Complete:** [Reinforcement quizzes 45–48](8-Reinforcement/quiz-answers.md).
- [x] **Verified:** The notebooks share a [tabular learner](8-Reinforcement/qlearning.py) and explicit [world rules and bounded walk](8-Reinforcement/world.py), with focused terminal-state, move-limit, no-revisit, and resource-rule tests.

### 9 — Real-World Machine Learning

- [x] **Complete and visually checked:** Applications [answers](9-Real-World/1-Applications/answers.md) and [editable PowerPoint proposal](9-Real-World/1-Applications/ml-scavenger-hunt.pptx). The bonus prototype reuses the executed energy SVR. All seven slides were rendered and inspected.
- [x] **Complete locally:** Model-debugging [paper and assignment status](9-Real-World/2-Debugging-ML-Models/answers.md) and [executed local audit](9-Real-World/2-Debugging-ML-Models/notebook.ipynb). The external RAI dashboard notebook remains under the approved exclusion and is not presented as run.
- [x] **Complete:** [Real-world quizzes 49–50](9-Real-World/quiz-answers.md). The English question bank contains no separate model-debugging quiz entries.

## Approved exclusions

- [ ] **Skipped — approved exclusion:** External environment-training courses and videos — completion would require participation outside this repository.
- [ ] **Skipped — approved exclusion:** External Responsible AI notebook — includes the model-debugging dashboard sample run. A separate local audit is provided, and no external run or personal observations were fabricated.
- [ ] **Skipped — approved exclusion:** Data-scientist interview — no interview or personal reflection was fabricated.
- [ ] **Skipped — approved exclusion:** Cloud deployment — the history timeline and pumpkin app are local artifacts and are not presented as deployed.

## Verification

Latest verification date: **2026-10-19**. The nine notebooks for Time Series, Reinforcement Learning, and the local model audit were executed in the earlier continuation. The translation/sentiment notebook was re-executed with TextBlob 0.19.0 after completing its live translation exercise. The Q-learning notebook was re-executed after adding both walk challenges; its earlier apple and resource-world results are unchanged. Regression notebooks were executed on **2026-10-12**.

- All 27 notebooks were executed from their containing directories with saved outputs; the new notebooks contain no error or stderr outputs.
- All **34 tests** pass with `PYTHONPATH=/private/tmp/mlfb-translation-textblob:/private/tmp/mlfb-extra /opt/anaconda3/bin/python -m unittest discover -s homework-solutions/tests -v` in the staged environment. After installing the requirements normally, omit the temporary `PYTHONPATH`.
- Local index links, quiz counts, approved exclusions, notebook execution state, and required lesson content are covered by the contract.
- The pumpkin model export/reload and Flask predictions/input validation pass. Its browser form, validation, and desktop/mobile layouts were checked; the [browser report and screenshots](verification/browser-checks.md) also cover the pantry recommender and its corrected WASM asset URL.
- The UFO training route, before-training response, predictions, data cleaning, and input validation pass. The notebook checks export/reload equivalence and training-only scaling.
- NLP checks cover both bot command lines, whitespace/case handling, question-word boundaries, sentiment, topic memory, and all 30 quiz answers against the English question bank. Notebook assertions cover dataset shape, parsing, missing-text handling, negation, and disjoint training/test data.
- Live translation checks validate service status, nonempty changed output, segment size, and the novel sentence's explicit neural-result provenance before saving all four responses. The public service requires internet access and can change its wording.
- Full hotel sentiment processing used all 515,738 rows. On the movie assignment's 500 held-out reviews, VADER scored 65.0% accuracy and TF-IDF plus logistic regression scored 85.6%, against a 50.0% majority baseline.
- Forecasting uses chronological validation and test periods, train-only scaling, past-only lag windows, baseline comparisons, and saved metrics. December energy SVR MAPE is 1.0730%; the CO2 assignment MAPE is 0.10846%.
- Reinforcement checks verify one-use apples, fatigue and energy rules, battle thresholds, discretization boundaries, and correct terminal Bellman targets. CartPole reaches 200 steps on all 100 final seeds. Mountain Car reaches the flag on all 100 final seeds, with a maximum of 162 steps.
- The additional walk experiment records 1,000 episode paths. All paths respect the 100-move cap; all 500 no-revisit paths contain unique positions. The 17 trapped games and lower no-revisit success rate are retained and explained. Tests also force a 100-step loop, a trapped path, and immediate goal/hazard termination.
- The local audit reproduces the frozen model's predictions and checks that its exact linear feature decomposition sums to the prediction. Cohort and sensitivity results remain descriptive.
- The seven-slide PowerPoint passes package, relationship, geometry, font, and editable-table checks. Its measured results match the prototype CSV. LibreOffice 25.8.2.2 rendered all seven pages, and every slide was visually checked for clipping and table alignment; native PowerPoint rendering was not checked.
- The 13 new plots and both reinforcement-learning animations were inspected. All relative file links in the authored Markdown files resolve, and all 52 quiz keys match the English question bank.

Classification verification: four notebooks executed; two Word assignments rendered and visually checked; Python/WASM inference parity, real browser inference, and desktop/mobile recommender checks passed. See [session progress](SESSION-PROGRESS.md) for the completed continuation and approved exclusions.
