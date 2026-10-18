# TimeSeries quiz answers

Expected answers from the English question bank, with qualifications where the lesson simplifies a concept.

## Quiz 41: Intro to Time Series: Pre-Lecture Quiz

1. Time Series Forecasting is useful in  
   **Answer:** both the above  
   Both listed applications can use historical observations for forecasting.
2. A time series is a sequence taken at:  
   **Answer:** successive equally spaced points in time  
   This is the regularly sampled case used in the lesson. Time series can also be irregularly sampled.
3. Time series can be used in:  
   **Answer:** earthquake prediction  
   Seismic observations can be analyzed as time series. This answer does not establish reliable earthquake prediction.

## Quiz 42: Intro to Time Series: Post-Lecture Quiz

1. Time series trends are  
   **Answer:** Measurable increases and decreases over time  
   A trend describes a sustained change in level over time.
2. Outliers are  
   **Answer:** points far away from standard data variance  
   Unusual observations merit investigation; they need not be errors or noise.
3. Time Series Forecasting is most useful for  
   **Answer:** Econometrics  
   Econometrics is an example, rather than a universal ranking of the usefulness of forecasting.

## Quiz 43: Time Series ARIMA: Pre-Lecture Quiz

1. ARIMA stands for  
   **Answer:** AutoRegressive Integrated Moving Average  
   ARIMA combines autoregression, differencing, and moving-average innovations.
2. Stationarity refers to  
   **Answer:** data whose distribution does not change when shifted in time  
   This describes strict stationarity. Weak stationarity instead constrains means, variances, and lag covariances.
3. Differencing  
   **Answer:** eliminates trend and seasonality  
   This is the quiz answer. Differencing can reduce trend or seasonal patterns, but does not guarantee their removal or stationarity.

## Quiz 44: Time Series ARIMA: Post-Lecture Quiz

1. ARIMA is used to make a model fit the special form of time series data  
   **Answer:** as closely as possible  
   A close training fit alone does not establish forecast accuracy; chronological held-out evaluation is still needed.
2. Use SARIMAX to  
   **Answer:** manage seasonal ARIMA models  
   Statsmodels SARIMAX supports seasonal components and optional explanatory variables.
3. 'Walk-Forward' validation involves  
   **Answer:** re-training a model progressively as it is validated  
   Only observations available at each origin may inform its forecast. State updating with fixed parameters and full refitting are distinct variants.

## Quiz 51: Time Series SVR: Pre-Lecture Quiz

1. SVM stands for  
   **Answer:** Support Vector Machine  
   SVM is the support vector machine family.
2. Which of these ML techniques is used to predict continuous values?  
   **Answer:** Regression  
   Regression predicts numerical targets, unlike a categorical classification target.
3. Which of these models is popularly used for time series forecasting?  
   **Answer:** ARIMA  
   ARIMA is one classical time-series model; compare it with simple forecast baselines.

## Quiz 52: Time Series SVR: Post-Lecture Quiz

1. By which of these methods does an SVR learn?  
   **Answer:** Finding the best fit hyperplane that has the maximum number of data points  
   This is the quiz wording. More precisely, epsilon-SVR trades model flatness against errors outside an epsilon-insensitive band.
2. What is the purpose of a kernel in SVMs?  
   **Answer:** To transform the dataset to a higher dimension space  
   A kernel represents inner products in a feature space, often implicitly. It need not explicitly construct a higher-dimensional array.
3. Which of these models consider the non-linearity in the dataset?  
   **Answer:** SVR using RBF kernel  
   An RBF kernel can model nonlinear relationships, although kernel choice still needs validation.
