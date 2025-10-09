# CS531 — Class 5 Assignment
# 04 — Poisson process & Exponential waits (≈8 min)
# Learning goals:
# - Simulate a homogeneous Poisson process via exponential inter-arrivals.
# - Aggregate counts per hour and compare to Poisson pmf; inspect waits vs Exp pdf.
# - (Stretch) Estimate λ via MLE from inter-arrival times.

import numpy as np, math, matplotlib.pyplot as plt
rng = np.random.default_rng(42)

def simulate_poisson_process(lam: float, T: float) -> np.ndarray:
    """Return sorted event times in (0, T] using exponential(1/lam) gaps."""
    times = []
    t = 0.0
    while True:
        w = rng.exponential(1.0 / lam)
        t += w
        if t > T:
            break
        times.append(t)
    return np.array(times)

def hour_bucket_counts(times: np.ndarray, T: float) -> np.ndarray:
    """Return counts per unit hour bucket over [0,T)."""
    bins = np.arange(0.0, T + 1.0, 1.0)
    counts, _ = np.histogram(times, bins=bins)
    return counts

def poisson_pmf(lam: float, k: np.ndarray) -> np.ndarray:
    """Poisson(λ) pmf vector at integer array k."""
    k = np.asarray(k, dtype=int)
    pmf = np.array([math.exp(-lam) * lam**int(ki) / math.factorial(int(ki)) for ki in k], dtype=float)
    return pmf

# ===== Student Work =====
lam, T = 4.0, 5.0
times = simulate_poisson_process(lam, T)
print("Total events:", len(times))

counts = hour_bucket_counts(times, T)
vals, freqs = np.unique(counts, return_counts=True)
emp = freqs / freqs.sum()

k = np.arange(0, counts.max() + 1)
pmf = poisson_pmf(lam, k)

plt.figure(figsize=(6, 3))
plt.stem(vals, emp, basefmt=" ", label="Empirical/hour counts")
plt.plot(k, pmf, marker="o", linestyle="--", label="Poisson(4)")
plt.xlabel("k"); plt.ylabel("P(X=k)"); plt.legend(); plt.tight_layout(); plt.show()

# Inter-arrival histogram vs Exp(λ) pdf
waits = np.diff(np.concatenate([[0.0], times]))
x = np.linspace(0, 3, 200)
pdf = lam * np.exp(-lam * x)
plt.figure(figsize=(6, 3))
plt.hist(waits, bins=20, density=True, alpha=0.6, label="Empirical waits")
plt.plot(x, pdf, label="Exp(λ=4) pdf")
plt.xlabel("wait time"); plt.ylabel("density"); plt.legend(); plt.tight_layout(); plt.show()

# ---- Optional stretch ----
# lam_hat = 1.0 / waits.mean()
# print("λ_hat (MLE) from waits:", lam_hat)

# ---- (Instructor) quick checks (uncomment) ----
# assert counts.shape[0] == int(T)
# assert waits.min() >= 0
