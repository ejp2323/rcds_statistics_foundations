import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# Helper: manual Pearson correlation
# =====================================================
def pearson_manual(x, y):
    x_bar = x.mean()
    y_bar = y.mean()
    
    cov = np.sum((x - x_bar) * (y - y_bar)) / (len(x) - 1)
    std_x = x.std()
    std_y = y.std()
    
    return cov / (std_x * std_y)


# =============================
# 1. Linear dataset
# =============================
linear = pd.read_csv("data/linear.csv")

x = linear.iloc[:, 0]  # all rows, first column
y = linear.iloc[:, 1]  # all rows, second column

print("\nLinear dataset")
print("Mean (x, y):", x.mean(), y.mean())
print("Variance (x, y):", x.var(), y.var())

r_manual = pearson_manual(x, y)
r_library = x.corr(y)

print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)

# Scatter
plt.figure()
plt.scatter(x, y, s=10, edgecolors='black')
plt.scatter(x.mean(), y.mean(), marker='x', s=100)
plt.title("Linear - Scatter plot")


# =============================
# 2. Quadratic dataset
# =============================
quadratic = pd.read_csv("data/quadratic.tsv", sep="\t")

x = quadratic.iloc[:, 0]
y = quadratic.iloc[:, 1]

print("\nQuadratic dataset")
print("Mean (x, y):", x.mean(), y.mean())
print("Variance (x, y):", x.var(), y.var())

r_manual = pearson_manual(x, y)
r_library = x.corr(y)

print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)

# Scatter
plt.figure()
plt.scatter(x, y, s=10, edgecolors='black')
plt.scatter(x.mean(), y.mean(), marker='x', s=100)
plt.title("Quadratic - Scatter plot")


# =============================
# 3. Sinusoidal dataset
# =============================
sinusoidal = pd.read_json("data/sinusoidal.json")

x = sinusoidal.iloc[:, 0]
y = sinusoidal.iloc[:, 1]

print("\nSinusoidal dataset")
print("Mean (x, y):", x.mean(), y.mean())
print("Variance (x, y):", x.var(), y.var())

r_manual = pearson_manual(x, y)
r_library = x.corr(y)

print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)

# Scatter
plt.figure()
plt.scatter(x, y, s=10, edgecolors='black')
plt.scatter(x.mean(), y.mean(), marker='x', s=100)
plt.title("Sinusoidal - Scatter plot")


# =============================
# Show all plots
# =============================
plt.show()