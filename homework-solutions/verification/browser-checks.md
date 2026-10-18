# Local homework browser verification

Verified on **2026-10-19 Asia/Singapore** (2026-10-18 17:25 UTC) using **Chrome for Testing 153.0.8010.12** in headless mode with a temporary profile. The tests allowed browser requests only to `127.0.0.1`; no personal browser profile, account, tabs, history, or credentials were used. The test browser and both test servers were closed afterwards.

The [machine-readable results](browser-results.json) record all ten passed check groups. Desktop screenshots use a 1440 × 1000 viewport; mobile screenshots use 390 × 844. All four screenshots were inspected for clipping, readable labels, and usable controls. This checks Chromium at those sizes; it is not a Safari, Firefox, native mobile, or screen-reader audit.

| App | Checks and observed result | Screenshots |
| --- | --- | --- |
| Pumpkin estimator, `http://127.0.0.1:5010` | Submitting month 10 displays USD 27.81 per bushel. Empty, fractional, and out-of-range values fail browser validation. A direct invalid POST returns HTTP 400 and an accessible error. The mobile page has no horizontal overflow. | [Desktop](pumpkin-desktop.png), [mobile](pumpkin-mobile.png) |
| Pantry recommender, `http://127.0.0.1:8766` | All 380 ingredients load. Empty selections show an error. Cumin, cardamom, and yogurt predict Indian cuisine and suggest turmeric, onion, and coriander. Search filters and restores choices; clearing removes selections and stale results. Real WASM inference succeeds. The mobile page has no horizontal overflow. | [Desktop](pantry-desktop.png), [mobile](pantry-mobile.png) |

The initial browser run caught a runtime-loader failure: a relative WASM asset directory was appended to the directory of `ort.min.js`, duplicating `node_modules/onnxruntime-web/dist/` and returning HTTP 404. The fix resolves that directory to an absolute URL relative to `app.mjs`. Repeating the same browser checks then passed, with no uncaught JavaScript errors. The separate Node inference/parity test remains part of verification.

To repeat the manual browser checks, start the apps using their lesson instructions. Port 5010 was used for the pumpkin verification because macOS Control Center occupied port 5000. Serve the pantry folder over HTTP, select the three ingredients above, run inference, try an empty selection and search with no matches, then clear the form. Check both viewport sizes and confirm the page has no horizontal scrolling.
