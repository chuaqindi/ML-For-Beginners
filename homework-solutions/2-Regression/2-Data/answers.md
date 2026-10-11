# Regression data homework

## Matplotlib

Matplotlib is the more explicit option: I created the figure, axes, marks, labels, and layout directly. That extra control is useful when a chart needs precise styling or an unusual composition. In the notebook, the Matplotlib scatter plot exposes the relationship between day of year and normalized bushel price, while the histogram shows the price distribution and its long upper tail.

## Seaborn

Seaborn was easier for rapid exploration because its functions accept dataframe column names and supply statistical defaults. A regression scatter plot adds a fitted trend in one call, a box plot compares the monthly distributions, and a heatmap summarizes the numeric correlations. Matplotlib still handles the final labels and layout, so the two libraries work well together rather than being mutually exclusive.

## Challenge — plots suited to regression

Scatter plots are the first choice for regression because they reveal the direction, shape, spread, clusters, and outliers in the relationship between a feature and a numeric target. A regression line makes an assumed linear trend visible, but it should not replace inspection of the points. A residual plot is the most useful follow-up: curvature suggests the model missed a nonlinear pattern, changing spread suggests non-constant variance, and extreme residuals expose poorly fitted observations. Distribution plots help detect skew and outliers, box plots compare a numeric target across categories, and correlation heatmaps screen several numeric variables at once. Correlation alone is not predictive accuracy and can miss seasonal or other nonlinear structure.

## Assignment — ease-of-use comparison

For these pumpkin explorations, Seaborn was easier because `regplot`, `boxplot`, and `heatmap` express the statistical intent directly and work with the cleaned dataframe. Matplotlib required more setup but offered finer control. I would use Seaborn for quick regression exploration, then customize its Matplotlib axes when presentation details matter.
