# Introduction and Regression Homework Design

## Goal

Create a complete, reviewable Python solution portfolio for the eight lessons in `1-Introduction` and `2-Regression` without modifying the original curriculum or generated translations.

## Scope

The portfolio covers every in-repository pre-lesson quiz, post-lesson quiz, lesson challenge, notebook exercise, and assignment for:

- `1-Introduction/1-intro-to-ML`
- `1-Introduction/2-history-of-ML`
- `1-Introduction/3-fairness`
- `1-Introduction/4-techniques-of-ML`
- `2-Regression/1-Tools`
- `2-Regression/2-Data`
- `2-Regression/3-Linear`
- `2-Regression/4-Logistic`

Python is the only implementation language. R alternatives are out of scope.

## Exclusions

Skip activities that require unverifiable personal or external participation:

- External environment-training courses and videos
- Running and reporting on an external Responsible AI notebook
- Interviewing a data scientist
- Cloud deployment

Skipped work must be listed in the portfolio index with its reason. The solutions must not invent personal observations, interviews, or execution results.

## Deliverables

Create `homework-solutions/` with this structure:

- `README.md`: checklist linking every deliverable and explaining every exclusion
- `quiz-answers.md`: answers and brief explanations for the Introduction and Regression pre/post quizzes
- `1-Introduction/<lesson>/answers.md`: written challenge and assignment answers, or a clear skip note
- `2-Regression/<lesson>/answers.md`: written challenge and assignment answers
- `2-Regression/<lesson>/notebook.ipynb`: executed notebook when the lesson or assignment requires code, experiments, models, or plots

The history timeline assignment may use a small local static HTML artifact rather than an external timeline service. Written artifacts remain Markdown unless the rubric explicitly requires a document; an applicable non-skipped `.docx` requirement must be delivered as `.docx`.

## Content Rules

- Reuse repository datasets, existing lesson patterns, and Scikit-learn datasets before adding anything new.
- Keep notebooks self-contained, explanatory, and runnable from their containing directory.
- Save meaningful plots, metrics, and model outputs in executed notebooks.
- Cite sources used for researched factual claims.
- Keep prose concise while meeting each exemplary rubric criterion.
- Do not edit `translations/`, lesson source files, or existing `solution/` files.

## Verification

- Run every created notebook from a clean kernel and save successful outputs.
- Check that regression models report appropriate metrics and explain their limitations.
- Validate local links in the portfolio index.
- Render any `.docx` artifact and visually inspect every page.
- Compare the final index against all eight lesson READMEs, assignment files, and relevant quiz entries.

## Completion Criteria

This phase is complete when every in-scope item is linked from `homework-solutions/README.md` and is either verified or explicitly skipped under the approved exclusion policy. Work outside `1-Introduction` and `2-Regression` must remain untouched.
