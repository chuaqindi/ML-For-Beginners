# Responsible AI dashboard review and local model audit

## Assignment status and evidence

**External dashboard notebook execution — skipped under the approved exclusion for the External Responsible AI notebook.** The assignment links [Azure's sample notebooks](https://github.com/Azure/RAI-vNext-Preview/tree/main/examples/notebooks). No Azure notebook, cloud workspace, or dashboard session is claimed as run.

The accompanying [local notebook](notebook.ipynb) actually executes related debugging techniques using pandas and scikit-learn on the fixed energy SVR. This paper distinguishes that local evidence from the published dashboard's capabilities. The prototype is a historical electricity-load model; it is not a decision system about individuals.

## Dashboard components

Microsoft's [dashboard overview](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2) describes tools for investigating errors, comparing cohorts, exploring data, interpreting predictions, inspecting counterfactual cases, and causal analysis. Their outputs answer different questions. Error concentration identifies a group to investigate, feature importance describes predictive reliance, and a what-if prediction does not by itself establish an intervention's causal effect.

The curriculum's four core components map to the following local measurements. They are independent demonstrations, rather than screenshots or output from the RAI dashboard.

## Error analysis and model overview

The frozen model predicts all **744 December 2014 hours** after training and validation on earlier data. Its aggregate MAE is **36.6868 dataset load units**, with **1.0730% MAPE**. Persistence has MAE **131.2796**, and the previous-day baseline **162.2056**. The notebook verifies that the loaded model reproduces the exported predictions.

| Cohort | Hours | MAE | MAPE | Underprediction rate |
| --- | ---: | ---: | ---: | ---: |
| Weekdays | 552 | 36.8106 | 1.0669% | 58.15% |
| Weekends | 192 | 36.3308 | 1.0905% | 44.79% |
| Outside 16:00–20:00 | 589 | 34.5585 | 1.0568% | 53.65% |
| 16:00–20:00 | 155 | 44.7741 | 1.1343% | 58.71% |

Peak-window MAE is higher than the aggregate, although its percentage error differs less because the underlying load levels differ. The [cohort table](cohort-metrics.csv) includes denominators. A shallow error tree and [hourly error plot](error-analysis.png) describe where December errors occur. Because the tree is fitted to these observed test errors, its discovered rules would need later data for confirmation.

## Data analysis and representation

The [hour representation table](hour-representation.csv) checks coverage before interpreting an hourly disparity. December has 31 observations per calendar hour, while weekday/weekend groups have different sample sizes. This single historical series lacks demographic attributes, property identifiers, tariffs, and operator responses. It cannot establish demographic fairness or reliable performance for a population of buildings. Balanced hourly coverage does not guarantee that unusual weather or holidays are adequately represented.

## Global and local interpretation

The notebook computes [permutation importance](feature-importance.csv) on the held-out period and plots [MAE changes after shuffling each lag](feature-importance.png). This measures model reliance in that sample. Correlated lag features can substitute for one another, and a negative or small estimate may reflect sampling variation rather than irrelevance.

The selected SVR has a linear kernel, so the notebook also constructs an **exact local decomposition** into its intercept and scaled feature contributions. Their sum is checked against the actual prediction. The [local explanation](local-explanation.csv) depends on the scaler's reference, and positive and negative contributions can cancel. An algebraic contribution is not a causal effect.

The [sensitivity scenarios](sensitivity-scenarios.csv) change one previous-hour reading while holding other lags fixed. They illustrate conditional model behavior, but the resulting history may be physically inconsistent. Neither those examples nor permutation importance prove that changing a recorded lag would change real electricity demand. A causal analysis would require explicit assumptions, an appropriate design, and evidence about interventions.

## Challenge and conclusions

Responsible model use requires more than a small average error or a diverse development team. Define the decision and affected users, examine label quality and missing populations, evaluate relevant groups with support counts, and provide a way to challenge harmful outputs. For a lending or hiring model, exclusion and appealing errors would matter directly; the aggregate energy data here cannot test those individual-level concerns.

For this prototype, the next justified checks are later-season backtests, uncertainty calibration, and review of peak-hour underprediction with operators. Those are proposed next steps, not completed trials. The original model stays fixed during this audit. If these findings lead to a revision, reserve a later untouched period to evaluate it. External dashboard participation and deployment remain excluded, and no corresponding observations are fabricated.
