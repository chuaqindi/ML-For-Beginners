# Time-series data and reproduction

The lesson notebooks read the repository's original `7-TimeSeries/data/energy.csv` directly without modifying it. It contains 26,304 hourly timestamps with `load` and `temp`, from 2012–2014. Forecast features use past load only; no future weather or load values enter a prediction. Plots label load in dataset units because the CSV itself does not specify a physical unit.

The three assignment snapshots were exported from the installed **statsmodels 0.14.2** package:

| Snapshot | Original source documentation | Contents |
| --- | --- | --- |
| [co2.csv](co2.csv) | [Mauna Loa weekly CO2](https://www.statsmodels.org/stable/datasets/generated/co2.html) | 2,284 weekly timestamps, with 2,225 observed concentrations and 59 missing values. Concentrations are in ppmv. |
| [sunspots.csv](sunspots.csv) | [Annual sunspot activity](https://www.statsmodels.org/stable/datasets/generated/sunspots.html) | 309 annual observations, 1700–2008. |
| [nile.csv](nile.csv) | [Nile flow at Aswan](https://www.statsmodels.org/stable/datasets/generated/nile.html) | 100 annual observations, 1871–1970, in 10^8 m³. |

Statsmodels identifies these datasets as public domain. They are historical snapshots, not live conditions. To regenerate a snapshot in Python, call `statsmodels.api.datasets.<name>.load_pandas().data` and save it as CSV, retaining the CO2 date index. The supplied snapshots let all time-series notebooks run offline.

SHA-256:

```text
6e492cee41c1c5491c3d955316bf969d86e9d22ed825556ce2915c960ecd813e  co2.csv
4425242e45763740928ab4e1f7357fee786cd0780f0f3bf2673c0fe4211d6957  sunspots.csv
5bc2a189305d45958d08a37a52c37d35ab08667b6c8a4ab5c2c764a9bdd6b142  nile.csv
```

Install the portfolio [requirements](../../requirements.txt) in Python **3.10 or later** and execute each notebook from its containing directory. Five notebooks cover the introduction, energy ARIMA, fresh-data ARIMA assignment, energy SVR, and fresh-data SVR assignment. Model selection uses validation periods preceding the final tests. Run the SVR energy notebook before the real-world audit, which reuses its exported pipeline and data.
