import pandas as pd
import matplotlib.pyplot as plt

files = [
    "data/anscombe1.csv",
    "data/anscombe2.csv",
    "data/anscombe3.csv",
    "data/anscombe4.csv"
]

# =============================
# Summary statistics
# =============================
for f in files:
    df = pd.read_csv(f)
    x = df["x"]
    y = df["y"]

    print(f"\n{f}")
    print("Mean (x, y):", x.mean(), y.mean())
    print("Variance (x, y):", x.var(), y.var())
    print("Correlation:", x.corr(y))

# =============================
# Scatter plots
# =============================
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

for i, f in enumerate(files):
    df = pd.read_csv(f)
    x = df["x"]
    y = df["y"]

    ax = axs[i // 2, i % 2]
    ax.scatter(x, y, s=20, edgecolors='black')
    ax.set_title(f)

plt.tight_layout()
plt.show()