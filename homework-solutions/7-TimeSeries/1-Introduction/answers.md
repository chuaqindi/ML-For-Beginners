# Introduction to time series

## Exercise

The [executed notebook](notebook.ipynb) loads all **26,304 hourly energy observations** from 2012–2014, checks timestamps, missing hours, and missing values, and plots both the complete series and 1–7 July 2014. It also plots the average daily profile and autocorrelation. The original dataset and curriculum are unchanged.

The data exhibit daily and weekly repetition and a changing seasonal level. A repeated pattern can be useful forecasting signal. An unusual observation needs investigation before treating it as an error. In the lesson's CO2 example, concentration is the changing variable and the date is its time index. Time series can have irregular intervals even though the quiz emphasizes regular sampling.

## Assignment — visualize three other datasets

The same notebook includes three complete [local snapshots with provenance](../data/README.md):

| Dataset | Sampling and observations | Visible characteristics |
| --- | --- | --- |
| Mauna Loa CO2 | 2,284 weekly timestamps, including 59 missing measurements | Rising level and annual variation. Missing weeks remain visible as gaps. |
| Sunspot activity | 309 annual values, 1700–2008 | Multi-year cycles with changing length and amplitude. These are not within-year seasonal effects. |
| Nile flow at Aswan | 100 annual values, 1871–1970 | Year-to-year variation and an apparent level change near 1898. A plot does not establish the cause. |

See the [three-series plot](three-time-series.png), [CO2 seasonal detail](co2-seasonality.png), [energy overview](energy-overview.png), and [load patterns](energy-patterns.png). The CO2 forecast preparation uses monthly aggregation followed by forward filling from earlier months only. The descriptive within-year plot does not supply features to the forecasting models.

## Challenge — areas that benefit from forecasting

Potential applications include exhibit attendance in the arts, output and unemployment in econometrics, river flow and population cycles in ecology, product demand in retail, equipment telemetry in industry, liquidity and volatility in finance, electricity demand in energy, traffic and transit demand in transport, and public-service call volumes. These are application ideas, not claims that one model has been validated for every use. Each needs an appropriate horizon, cost of error, chronological evaluation, and a record of information available when the forecast is made.
