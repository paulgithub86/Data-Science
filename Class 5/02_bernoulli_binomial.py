# CS531 — Class 5 Assignment
# 02 — Bernoulli & Binomial: simulation vs theory (≈7 min)
# Learning goals:
# - Simulate Bernoulli / Binomial; compare empirical pmf with theory; compute tail probability.

import numpy as np, matplotlib.pyplot as plt
from math import comb

rng = np.random.default_rng(42)

def theoretical_binomial_pmf(n: int, p: float, k: np.ndarray) -> np.ndarray:
    """Return Binomial(n,p) pmf evaluated at array k."""
    k = np.asarray(k, dtype=int)
    pmf = np.zeros_like(k, dtype=float)
    mask = (k >= 0) & (k <= n)
    km = k[mask]
    pmf[mask] = np.array([comb(n, int(ki)) * (p**ki) * ((1-p)**(n-ki)) for ki in km])
    return pmf

def empirical_pmf(samples: np.ndarray):
    """Return (vals, probs) from integer samples."""
    vals, counts = np.unique(samples, return_counts=True)
    probs = counts / counts.sum()
    return vals, probs

def estimate_tail_prob(samples: np.ndarray, thr: int) -> float:
    """Estimate P(X>=thr) empirically from samples."""
    return (samples >= thr).mean()

# ===== Student Work =====
p = 0.3
n = 1000
bern = (rng.random(n) < p).astype(int)
print("Bernoulli sample mean:", bern.mean(), " (theory:", p, ")")

m = 10_000
X = rng.binomial(n=10, p=p, size=m)
vals, emp = empirical_pmf(X)
ks = np.arange(vals.min(), vals.max() + 1)
theory = theoretical_binomial_pmf(10, p, ks)

plt.figure(figsize=(6, 3))
plt.stem(vals, emp, basefmt=" ", label="Empirical")
plt.plot(ks, theory, marker="o", linestyle="--", label="Theory")
plt.xlabel("k"); plt.ylabel("P(X=k)"); plt.title("Binomial(10,0.3)")
plt.legend(); plt.tight_layout(); plt.show()

est_tail = estimate_tail_prob(X, thr=5)
exact_tail = theoretical_binomial_pmf(10, p, np.arange(5, 11)).sum()
print("P(X>=5): empirical =", est_tail, " exact =", exact_tail)

# ---- Optional stretch ----
# 1) Repeat for p in {0.1, 0.5} and comment on symmetry vs skew.
# 2) Show convergence: increase m and plot |empirical - theory|_1.

# ---- (Instructor) quick checks (uncomment) ----
# assert abs(est_tail - exact_tail) < 0.03
