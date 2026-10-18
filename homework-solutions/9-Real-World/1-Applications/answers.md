# Real-world ML applications

## Assignment — ML scavenger hunt

The required [PowerPoint presentation](ml-scavenger-hunt.pptx) proposes **LoadWatch**, an hourly electricity-demand forecast for an operations team considering flexible loads. It explains the operating decision, available data, model, evaluation, workflow, limitations, and pilot criteria. Text and evidence tables remain editable. This is a hypothetical hackathon proposal, not a deployed product or an invented customer study.

All seven slides pass package and layout checks and were rendered with LibreOffice 25.8.2.2 for visual inspection. Native PowerPoint rendering was not checked.

The bonus model is the already [executed energy SVR](../../7-TimeSeries/3-SVR/notebook.ipynb), with its [fitted pipeline](../../7-TimeSeries/3-SVR/energy-svr.joblib) and [test metrics](../../7-TimeSeries/3-SVR/energy-metrics.csv). Reusing it avoids training a redundant model solely for the presentation.

Training covers September–October 2014, November selects among fifteen configurations, and December supplies **744 unseen hourly targets**. The selected linear SVR uses the previous 24 observed loads and reports **1.073% MAPE**, against **3.903%** for persistence and **4.792%** for a previous-day baseline. These are rolling one-hour forecasts. The deck makes no claim about actual savings, emissions reductions, or field reliability.

A prospective pilot would evaluate later seasons, peak-load errors, and alert burden with real operators before using the forecasts for equipment scheduling. Operators retain control and a fallback. The [local audit](../2-Debugging-ML-Models/notebook.ipynb) supplies measured error analysis and model explanations for the same fixed prototype.

## Challenge — another sector

**Manufacturing and predictive maintenance** provide an additional application. A classifier can relate operating conditions such as temperature, speed, torque, and tool wear to a machine-failure label. The [UCI AI4I 2020 dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) is a published **synthetic** benchmark reflecting that setting. It supports investigation, not a claim of deployment at a real factory.

Use features available before the decision, exclude failure-mode indicators that reveal the label, and evaluate precision/recall against maintenance workload and missed-failure costs. Split by machine and time when real identifiers become available. Failure classification at a recorded observation is distinct from a validated forecast of remaining useful life. A synthetic benchmark cannot establish factory reliability by itself.

## Knowledge checks

Regression, clustering, classification, NLP, and forecasting each address different questions. A transaction outlier is not automatically fraud; a readmission cluster does not establish a clinical cause. A useful prototype needs relevant data, an appropriate baseline, held-out evaluation, and a clear operational decision. External videos and cloud deployment remain under the approved exclusions; no outside participation is fabricated.
