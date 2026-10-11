# Linear and polynomial regression homework

## Challenge — correlation and model accuracy

The notebook compares Month and DayOfYear using the same pumpkin train/test rows. Their full-data correlations with normalized bushel price are weak (about **−0.149** and **−0.167**). DayOfYear has the slightly stronger correlation, but that does not imply useful predictive accuracy: on held-out data, the Month linear model has R² **−0.013**, MAE **9.176**, and RMSE **10.459**, while DayOfYear has R² **−0.003**, MAE **9.105**, and RMSE **10.405**. Both negative R² values mean a test-set mean prediction would perform better. Correlation measures a pairwise linear association on the available sample; predictive accuracy measures how well a fitted model generalizes to unseen rows. Neither establishes causation.

The similar poor results also show a limitation of testing only calendar position. Variety, package, city, market conditions, and repeated observations may explain more of the price variation. A random split can place closely related market records in both sets, so a time-aware evaluation would be preferable for a real forecasting claim.

## Assignment — fresh diabetes model

I compared degree-1 (ordinary linear) and degree-2 polynomial pipelines on Scikit-learn's diabetes dataset. The split is fixed with `random_state=42`, and polynomial expansion plus scaling are fit inside each pipeline using only the training rows. On the held-out set, the linear technique scores R² **0.485**, MAE **41.549**, and RMSE **53.370**. The polynomial technique is worse on all three metrics: R² **0.424**, MAE **44.030**, and RMSE **56.425**.

I therefore choose the simpler linear model. The polynomial model adds many interaction and squared terms but supplies no material test improvement, so its extra flexibility is not justified. Important limitations remain: the selected model explains only about half the held-out variance; the 442-row observational dataset is small; its target is a constructed disease-progression measure; and the experiment does not establish clinical causality or validate use on another population.
