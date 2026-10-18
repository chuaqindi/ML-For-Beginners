# Lesson continuation progress

## Homework requirement follow-up — 2026-10-19

The renewed "do homework" request was treated as a check for missed requirements. Comparing the source assignments and challenge sections with the portfolio found two omissions in the earlier completion report.

- [x] Replace the skipped workflow reflection with an evidence-based reflection on this portfolio's current stage, likely difficulties, and repeatable tasks. The external data-scientist interview remains excluded.
- [x] Complete both Q-learning walk challenges: enforce a 100-move cap, prevent revisits when requested, and report being trapped when no unvisited destination remains. Move the existing apple-seeking transition into `world.py` so the notebook, walk, and tests use the same rules.
- [x] Re-execute the full Q-learning notebook with five clean saved code-cell outputs. Preserve the earlier apple and resource-world results. Save 1,000 additional walk paths and a two-policy comparison: ordinary walk wins 183/500; no revisits wins 155/500 and is trapped 17/500, with zero repeated positions.
- [x] Add three focused walk tests and update the old portfolio check that required the reflection to remain skipped, retaining the interview-exclusion check. All **34 Python tests pass**. The existing upstream TextBlob lexicon `ResourceWarning` remains; there are no failures.
- [x] Confirm all 27 source assignments have answer files, all authored Markdown links resolve, all 52 quiz keys match, and all recorded walk paths obey their limits.

No browser was opened for this follow-up. Original curriculum files and translations remain unchanged. Approved external-participation/deployment exclusions and **do not run `git push`** still apply.

## Closing the remaining gaps — 2026-10-19

User request: "do the homework," following the report of pending browser checks and the retired translation API. Preserve all approved exclusions and **do not run `git push`**.

- [x] Execute four English-to-French translations using the documented MyMemory GET API and save complete responses with UTC timestamps. Distinguish translation-memory matches from the novel sentence's `MT!` / `neural` result. The retired TextBlob method itself remains retired; this is an explicit backend replacement.
- [x] Re-execute the translation/sentiment notebook with pinned TextBlob 0.19.0. All five code cells have clean saved outputs; the novel and poetry findings are unchanged.
- [x] Check the pumpkin form, native input validation, server rejection, and desktop/mobile layout in an isolated headless Chrome for Testing profile.
- [x] Reproduce and fix the pantry browser's duplicated WASM asset path by resolving it relative to `app.mjs`. Then pass real browser inference, empty-selection handling, search, clearing, and desktop/mobile checks.
- [x] Inspect all four browser screenshots and save the [browser evidence](verification/browser-checks.md). The temporary browser and local test servers were closed; no personal Chrome profile was used.
- [x] Final verification: all 31 Python tests pass, the Node WASM/parity checks pass, all 52 quiz keys match, all authored Markdown links resolve, and `git diff --check` is clean. The Python run emitted one upstream TextBlob 0.19.0 `ResourceWarning` for its lexicon file; there were no test failures.

The user asked what Google Chrome accessed. The browser visited only `http://127.0.0.1:5010` and `http://127.0.0.1:8766`, with a temporary Chrome for Testing profile and browser requests restricted to `127.0.0.1`. MyMemory requests were separate Python calls containing only the four public teaching sentences.

## Current continuation — 2026-10-19

The renewed "do the homework" request continues through the remaining sections. **Do not run `git push`.** Existing approval preferences and participation/deployment exclusions still apply.

- [x] Time Series: five executed notebooks, written answers, fresh Nile and CO2 models, three-dataset visualization, and quizzes 41–44/51–52.
- [x] Reinforcement Learning: resource-aware world and random-walk comparison, CartPole, Mountain Car, saved policies and simulations, and quizzes 45–48.
- [x] Real-World ML: seven-slide editable proposal with measured prototype results, written research, local model-audit notebook, and quizzes 49–50.
- [x] Preserve the external RAI dashboard execution exclusion and distinguish it from the actual local audit.
- [x] Finish presentation visual review and final portfolio checks: LibreOffice rendered all seven slides, every slide and the 13 new plots were inspected, 31 tests passed, all 27 notebooks have clean saved outputs, and all 52 quiz keys match the English bank. Native PowerPoint rendering remains untested.

Measured final evaluations: resource-world Q-learning 500/500 wins versus random walk 16/500; CartPole 200 steps on all 100 test seeds; Mountain Car 100/100 successes, mean 140.44 and maximum 162 steps. Forecasting retains the Nile ARIMA's loss to a simpler baseline rather than selecting a model after inspecting its test results.

## Previous continuation — 2026-10-18

User request: "do the homework." Continued with the next unfinished section, the five NLP lessons, following the existing portfolio format and exclusions. The user also requested approval defaults without prompts and explicitly instructed: **do not run `git push`**.

- Both NLP bots and seven analysis notebooks are implemented and executed.
- Written assignments, quiz IDs 31–40, data provenance, and local reproduction instructions are included.
- The unavailable 597-poem CSV is replaced explicitly by the same author's published 361-poem sample with precomputed Microsoft scores.
- Historical compatibility gap: current TextBlob removed `translate()`; no live translation output is claimed.
- Full hotel processing uses all 515,738 rows, retaining negation for VADER and excluding no-text rows from clustering.
- Movie-review held-out accuracy: VADER 65.0%, TF-IDF/logistic regression 85.6%, majority baseline 50.0%.
- No Git push was performed. Time Series and later sections remain pending.

## Earlier timed session

Previous user request: continue lessons until the five-hour limit runs out. That deadline has passed; the current continuation is a separate request.

- Started: 2026-10-18 01:59:21 Asia/Singapore (2026-10-17 17:59:21 UTC).
- Stop deadline: 2026-10-18 06:59:21 Asia/Singapore (2026-10-17 22:59:21 UTC).
- Work in curriculum order, beginning with Classification.
- Preserve curriculum and translations. Put solutions in this portfolio.
- Continue Python solutions; use JavaScript where the applied lesson explicitly requires browser inference.
- Retain approved exclusions: external participation and cloud deployment.
- Mark a lesson complete only after its artifacts are executed or otherwise verified.

## Work queue

- [x] Classification introduction: cleaning, plots, training-only balancing, challenge, five-algorithm document, quizzes.
- [x] Classifiers 1: logistic models and probabilities, solver comparison document, quizzes.
- [x] Classifiers 2: model comparison, parameter experiment, explanation, quizzes.
- [x] Applied classification: ONNX notebook, local recommender, expanded inputs, new recommender assignment, quizzes, and browser verification.
- [x] Clustering lessons: executed both notebooks, inspected plots, completed assignments and quizzes.
- [x] NLP lessons: two bots, seven executed notebooks, written assignments and quizzes; dataset substitution and retired translation API recorded above.
- [x] Time series lessons.
- [x] Reinforcement learning.
- [x] Real-world assignments, local model audit, and presentation visual review.

## Environment notes

Additional lesson dependencies are being staged in `/private/tmp/mlfb-extra` to avoid modifying the existing Python environment. Use `PYTHONPATH=/private/tmp/mlfb-extra` when running these notebooks. The installed base imbalanced-learn was incompatible with Scikit-learn 1.7.2, so a compatible release and sklearn-compat were added to the staging directory.

Applied classification passes native/WASM parity checks and the closing browser verification above. The earlier Computer Use limitation was resolved by using the cached Chrome for Testing binary in a separate headless profile; no personal Chrome session was accessed. All new work stays in `homework-solutions/`; no Git push was performed.
