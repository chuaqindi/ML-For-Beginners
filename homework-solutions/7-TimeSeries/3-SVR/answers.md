# SVR forecasting

## Exercise and hyperparameter challenge

The [executed notebook](notebook.ipynb) keeps the lesson's lag-window SVR approach and addresses its inconsistent split descriptions with explicit dates: **September–October 2014 for training, November for validation, and December for final testing**. The final model refits on September–November before evaluating all **744 December hours**.

Fifteen experiments compare lookbacks of **4, 12, and 24 hours**, linear and RBF kernels, and different values of C, gamma, and epsilon. A four-hour lookback corresponds to the lesson's five-value window containing four inputs and one target. Input and target scalers fit inside each training estimator. Each row's inputs are strictly earlier than its target, and preceding training observations supply the first test window.

Validation selects a **linear SVR with 24 lags, C=10, epsilon=0.02**. Gamma is irrelevant to the selected linear kernel. Its November validation MAPE is **1.2021%**.

| Method | December test MAPE | MAE, dataset load units | RMSE |
| --- | ---: | ---: | ---: |
| Selected SVR | 1.0730% | 36.6868 | 52.9028 |
| Last observed hour | 3.9030% | 131.2796 | 172.4979 |
| Same hour, previous day | 4.7919% | 162.2056 | 216.1451 |

The [validation table](energy-validation.csv), [test metrics](energy-metrics.csv), and [forecast plot](svr-energy.png) preserve the comparisons. [Training rows](model-training.csv), [test predictions](model-test.csv), and the fitted [pipeline](energy-svr.joblib) support the later real-world proposal and model audit. The notebook verifies that reloading its own saved model gives identical predictions.

These are rolling **one-hour-ahead** forecasts using newly observed loads. They are not a single forecast for the whole month. Earlier or fitted portions of a whole-series plot would not measure unseen performance. No test result selected the hyperparameters.

## Assignment — a new SVR model

The [executed assignment](assignment.ipynb) uses monthly Mauna Loa CO2, aggregated from the complete weekly snapshot. Missing months use earlier values only. Training ends in 1997, validation covers 1998–1999, and the **24 test months** cover 2000–2001.

The same fifteen kernel/parameter/window experiments use lookbacks of **3, 6, and 12 months**. Validation selects a linear model with **12 lags, C=10, epsilon=0.02**.

| Method | Test MAPE | MAE, ppmv | RMSE, ppmv |
| --- | ---: | ---: | ---: |
| Selected SVR | 0.10846% | 0.40144 | 0.48371 |
| Last observed month | 0.28363% | 1.04917 | 1.19474 |
| Same month, previous year | 0.35512% | 1.31437 | 1.37401 |

See [experiments](co2-validation.csv), [metrics](co2-metrics.csv), [forecasts](co2-forecasts.csv), and the [residual plot](svr-co2.png). The large positive concentration level makes percentage errors small, so MAE and baselines remain important. This historical holdout does not establish current sensor or climate-forecast performance.
