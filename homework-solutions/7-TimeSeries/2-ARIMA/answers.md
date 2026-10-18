# ARIMA forecasting

## Energy exercise

The [executed notebook](notebook.ipynb) follows the lesson's executable dates: **1,416 training hours** from 1 November–29 December 2014, then **48 test hours** on 30–31 December. The prose in the original lesson describes different months, so the dates are stated explicitly. Scaling fits the training data only, and metrics use the original load units.

The seasonal model is **SARIMA(4,1,0)(1,1,0,24)**. For each of 46 origins it forecasts the next three hours, then reveals the next actual observation and updates the filter state. Coefficients stay fixed; this is not a claim of refitting parameters at every origin.

| Horizon | SARIMA MAPE | Persistence MAPE | Previous-day MAPE |
| --- | ---: | ---: | ---: |
| 1 hour | 0.5690% | 3.4318% | 4.3264% |
| 2 hours | 1.2317% | 6.5698% | 4.1180% |
| 3 hours | 1.6909% | 9.3886% | 3.8840% |

The [forecast records](energy-forecasts.csv), [full metric table](energy-metrics.csv), and [plot](arima-energy.png) preserve the results. Adjacent origins overlap, and the short holdout does not establish year-round performance.

## Challenge — alternatives to MAPE

**MAE** expresses typical absolute error in target units. **RMSE** puts more weight on large mistakes. **MASE** divides test MAE by a naive training error scale, enabling comparisons across differently scaled series. Here that scale uses a 24-hour training difference. MASE below one is relative to that training scale; the separately measured test baseline can behave differently.

MAPE is undefined at zero actual values and unstable near zero. A low percentage error can also be misleading when a series has a large level. Compare methods on the same targets, origins, and horizons, and examine residuals and uncertainty alongside the aggregate error. See [Forecasting: Principles and Practice](https://otexts.com/fpp3/accuracy.html).

ARIMA's moving-average component models past innovations rather than a rolling average of observations. Differencing may reduce a trend or seasonal pattern but does not guarantee stationarity.

## Assignment — a new ARIMA model

The [executed assignment](assignment.ipynb) uses fresh Nile-flow data. It trains on **1871–1940**, selects among four orders on **1941–1950**, and tests once on **1951–1970**. Validation chooses **ARIMA(1,0,1)**; final refitting uses the first 80 years. The notebook includes ADF checks, a residual Ljung–Box check, model intervals, and the [forecast plot](nile-arima.png).

| Method | Test MAPE | Test MAE, 10^8 m³ |
| --- | ---: | ---: |
| ARIMA(1,0,1) | 12.3276% | 101.9723 |
| Last observed value | 11.9627% | 101.9500 |
| Recent 20-year mean | 11.8697% | 106.1650 |

ARIMA **does not beat the simple baselines on test MAPE** in this experiment. That result is retained rather than choosing an order after seeing the test set. The small sample and historical level change limit extrapolation. The [metrics](nile-metrics.csv) and [forecasts](nile-forecasts.csv) distinguish measured accuracy from a close training fit. Model intervals are pointwise and do not prove calibration from twenty observations.
