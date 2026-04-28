# ECRI Statistics Foundations

### Chapter 7: Modelling

## Exercise 1: Correlation

1. Load data from the three csv files inside the `data/` directory.
   - `data/1_force_wire.csv`
   - `data/2_accelerated_motion.tsv`
   - `data/3_harmonic_motion.json`

2. For each dataset, store `col1` as x and `col2` as y, then do a scatter plot of the two variables and discuss the relationship.

3. Implement a manual calculation of the Pearson correlation coefficient.

4. Verify implementation with pandas `.corr()` function.

## Exercise 2: Curve Fitting

1. Load the `data/3_harmonic_motion.json` dataset from the data/ directory.

2. Do a scatter plot of the first two columns and discuss the relationship.

3. Implement a linear, polynomial, and sinusoidal fit with the `np.polyfit()`, `np.polyval(coeffs_linear, x_vals)` and `curve_fit` functions

4. Decide the best fitting curve by computing the Residual Sum of Squares (RSS) on the three attempts.

## Exercise 3: Anscombe’s Quartet

1. Load the four anscombe csv files from the data/ directory.
   - `data/anscombe1.csv`
   - `data/anscombe2.csv`
   - `data/anscombe3.csv`
   - `data/anscombe4.csv`

2. Compute mean, variance and correlation for each of them.

3. Do a scatter plot of each of them.

4. Discuss the result and limitations of summary statistics.

