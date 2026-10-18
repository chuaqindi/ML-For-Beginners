# Applied classification and a pantry recommender

## Lesson exercise

The [executed notebook](notebook.ipynb) trains the lesson's linear SVC (`C=10`, probability estimates enabled), using a grouped split of original recipes instead of splitting previously oversampled data. It scores **0.7889 accuracy** and **0.7608 macro F1** on 488 held-out recipes. The model has 380 binary ingredient inputs. Their names and order are checked against the curriculum's `ingredient_indexes.csv`.

The notebook exports [model.onnx](model.onnx) with sklearn-onnx and verifies **all** held-out labels and probabilities against Scikit-learn. Its graph contains an `SVMClassifier` and a cast; the input is `[batch, 380]`, with string-label and five-probability outputs. Printing the graph and tensor metadata provides the model-structure inspection without requiring a separate Netron installation. The browser uses the label output, because an SVC's predicted label need not equal the class with the largest calibrated probability.

## Challenge and new recommender assignment

The [local web app](index.html) expands the lesson's seven hard-coded ingredient checkboxes to all 380 model features, with search and selected-count feedback. Every request constructs a fresh feature vector, preventing old selections from leaking into later predictions.

The new task is **pantry completion**: after predicting a cuisine, recommend up to three absent ingredients ranked by their prevalence in that cuisine's training recipes. The method is transparent, excludes already-selected ingredients, and breaks ties alphabetically. For cumin, cardamom, and yogurt, this fitted model selects Indian cuisine and suggests **turmeric, onion, and coriander**. This demonstrates an actual recommendation output rather than merely renaming the classification app. Suggestions are associations, not complete recipes, authenticity judgments, or allergy checks.

The recommender uses only training recipes to calculate ingredient prevalence. It is a simple popularity baseline, not a personalized model or an experimentally validated measure of taste. The full feature mapping, class order, prevalence values, and held-out metrics are exported in [metadata.json](metadata.json).

## Run locally

From the repository root:

```bash
npm install --prefix homework-solutions/4-Classification/4-Applied
/opt/anaconda3/bin/python -m http.server 8766 --bind 127.0.0.1 --directory homework-solutions/4-Classification/4-Applied
```

Open <http://127.0.0.1:8766>. Select ingredients and press **Suggest additions**. The exported model and metadata are included; retraining is unnecessary to use the app. All runtime assets are served locally from the pinned npm package, so inference does not send the ingredient selection to an external service. Installation requires network access. The page must be served over HTTP rather than opened as a `file:` URL.

To regenerate the artifacts, execute the notebook from this directory with the portfolio Python dependencies installed. It overwrites `model.onnx`, `metadata.json`, and `fixtures.json` deterministically for the fixed seed and environment.

## Verification

```bash
npm test --prefix homework-solutions/4-Classification/4-Applied
```

The test uses the real ONNX Runtime Web WebAssembly backend under Node, comparing three held-out fixtures with Python labels and probabilities. It also checks empty/unknown input rejection, fresh vectors after changed selections, selected-ingredient exclusion, and the case where every ingredient is already present. The notebook verifies the full test-set conversion, finite outputs, feature order, and recommendation invariants.

Browser verification completed on **2026-10-19 Asia/Singapore** using a separate headless Chrome for Testing profile. It exposed a duplicated runtime-asset path: the relative WASM directory was resolved from the ONNX runtime script's own directory. Resolving it to an absolute URL relative to `app.mjs` fixes model loading without changing inference or model artifacts.

The browser loaded all 380 inputs, ran real WASM inference, reproduced the Indian-cuisine example, filtered ingredient searches, rejected empty selections, and cleared previous results. Desktop and mobile screenshots were inspected; the 390px mobile page has no horizontal overflow. See the [browser report and screenshots](../../verification/browser-checks.md). The browser context allowed only the two local servers and used no personal browser profile. Cloud hosting remains excluded.

## Review and sources

The model is trained offline and loaded once in the browser. Inference applies its fitted parameters to a new feature vector. Keeping model, feature metadata, and runtime versions together prevents mismatched inputs or assets. See [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) and [deployment guidance](https://onnxruntime.ai/docs/tutorials/web/deploy.html).

Dataset credit: Microsoft ML-For-Beginners, `4-Classification/data/cuisines.csv`, originally [Asian and Indian Cuisines on Kaggle](https://www.kaggle.com/hoandan/asian-and-indian-cuisines), as credited in the curriculum. [Quiz answers](../quiz-answers.md).
