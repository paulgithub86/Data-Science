# CS531 — Class 5 Assignment
# 06 — Normal: CDF & interval probabilities (≈8 min)
# Learning goals:
# - Implement φ and Φ via erf; compute interval probability; visualize.

import numpy as np, math, matplotlib.pyplot as plt

def phi(x: float) -> float:
    """Standard normal pdf."""
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)

def Phi(x: float) -> float:
    """Standard normal cdf via erf."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def interval_prob(mu: float, sigma: float, a: float, b: float) -> float:
    """P(a<=X<=b) for X~N(mu,sigma^2)."""
    za = (a - mu) / sigma
    zb = (b - mu) / sigma
    return Phi(zb) - Phi(za)

# ===== Student Work =====
mu, sigma = 10.0, 2.0
a, b = 8.0, 13.0
prob = interval_prob(mu, sigma, a, b)
print(f"P({a} ≤ X ≤ {b}) =", prob)

# Plot pdf with shaded interval
xs = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = (1 / (sigma * math.sqrt(2 * math.pi))) * np.exp(-(xs - mu) ** 2 / (2 * sigma ** 2))
mask = (xs >= a) & (xs <= b)

plt.figure(figsize=(6, 3))
plt.plot(xs, pdf)
plt.fill_between(xs[mask], pdf[mask], alpha=0.4)
plt.xlabel("x"); plt.ylabel("density"); plt.title("Normal(μ=10, σ=2)")
plt.tight_layout(); plt.show()

# ---- Optional stretch ----
# print("P(|X-μ|≤σ) ≈", interval_prob(mu, sigma, mu - sigma, mu + sigma))

# ---- (Instructor) quick checks (uncomment) ----
# assert 0.6 < interval_prob(mu, sigma, mu - sigma, mu + sigma) < 0.7
