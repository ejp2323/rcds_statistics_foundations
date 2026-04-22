import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

n = 100

# -----------------------------
# 1. Linear dataset (Force vs Position)
# F = kx + noise
# -----------------------------
x = np.linspace(0, 10, n)
k = 2.5
noise1 = np.random.normal(0, 2, n)
F = k * x + noise1

linear_df = pd.DataFrame({
    "position": x,
    "force": F
})

linear_df.to_csv("linear.csv", index=False)

# -----------------------------
# 2. Quadratic dataset (Accelerated motion)
# x(t) = (1/2) a t^2 + noise
# -----------------------------
t = np.linspace(0, 10, n)
a = 1.2
noise2 = np.random.normal(0, 5, n)
position_quad = 0.5 * a * t**2 + noise2

quadratic_df = pd.DataFrame({
    "time": t,
    "position": position_quad
})

quadratic_df.to_csv("quadratic.tsv", sep="\t", index=False)

# -----------------------------
# 3. Sinusoidal dataset (Harmonic motion)
# x(t) = A sin(ωt) + noise
# -----------------------------
t2 = np.linspace(0, 10, n)
A = 5
omega = 2 * np.pi / 5
noise3 = np.random.normal(0, 0.8, n)
position_sin = A * np.sin(omega * t2) + noise3

sinusoidal_df = pd.DataFrame({
    "time": t2,
    "position": position_sin
})

# Save as JSON (other format)
sinusoidal_df.to_json("sinusoidal.json", orient="records", indent=2)

print("Datasets generated:")
print(" - linear.csv")
print(" - quadratic.tsv")
print(" - sinusoidal.json")


import pandas as pd

# Anscombe's quartet (hard-coded classic dataset)
x1 = [10,8,13,9,11,14,6,4,12,7,5]
y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2 = x1
y2 = [9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]

x3 = x1
y3 = [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

x4 = [8,8,8,8,8,8,8,19,8,8,8]
y4 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89]

# Create dataframes
df1 = pd.DataFrame({"x": x1, "y": y1})
df2 = pd.DataFrame({"x": x2, "y": y2})
df3 = pd.DataFrame({"x": x3, "y": y3})
df4 = pd.DataFrame({"x": x4, "y": y4})

# Save as CSV
df1.to_csv("anscombe1.csv", index=False)
df2.to_csv("anscombe2.csv", index=False)
df3.to_csv("anscombe3.csv", index=False)
df4.to_csv("anscombe4.csv", index=False)

print("Anscombe datasets saved as\n - anscombe1.csv\n - anscombe2.csv\n - anscombe3.csv\n - anscombe4.csv")