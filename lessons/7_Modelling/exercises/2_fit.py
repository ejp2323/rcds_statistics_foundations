import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# =============================
# Load data
# =============================
data = pd.read_json("data/sinusoidal.json")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Convert to numpy (cleaner handling)
x_vals = x.to_numpy()
y_vals = y.to_numpy()

# =============================
# Scatter plot
# =============================
plt.figure()
plt.scatter(x_vals, y_vals, s=10, edgecolors='black')
plt.title("Sinusoidal data")

# =============================
# 1. Linear fit
# =============================
coeffs_linear = np.polyfit(x_vals, y_vals, 1)
y_linear = np.polyval(coeffs_linear, x_vals)

# =============================
# 2. Polynomial fit (degree 5)
# =============================
degree = 5
coeffs_poly = np.polyfit(x_vals, y_vals, degree)
y_poly = np.polyval(coeffs_poly, x_vals)

# =============================
# 3. Sinusoidal fit
# =============================
def sinusoidal(x, A, omega, phi):
    return A * np.sin(omega * x + phi)

initial_guess = [5, 1, 0]
params, _ = curve_fit(sinusoidal, x_vals, y_vals, p0=initial_guess)
y_sin = sinusoidal(x_vals, *params)

# =============================
# RSS computation
# =============================
def rss(y_true, y_pred):
    return np.sum((y_true - y_pred)**2)

rss_linear = rss(y_vals, y_linear)
rss_poly = rss(y_vals, y_poly)
rss_sin = rss(y_vals, y_sin)

print("\nResidual Sum of Squares (RSS)")
print("Linear:", rss_linear)
print(f"Polynomial (degree {degree}):", rss_poly)
print("Sinusoidal:", rss_sin)

# =============================
# Plot fitted curves
# =============================
idx = np.argsort(x_vals)

plt.plot(x_vals[idx], y_linear[idx], label="Linear fit")
plt.plot(x_vals[idx], y_poly[idx], label=f"Polynomial")
plt.plot(x_vals[idx], y_sin[idx], label="Sinusoidal fit")

plt.legend()
plt.show()