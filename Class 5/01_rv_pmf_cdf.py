# CS531 — Class 5 Assignment
# 01 — Discrete RV: PMF & CDF (≈7 min)
# Learning goals:
# - Build intuition for pmf/cdf; compute E[X], Var(X); visualize pmf vs cdf.
#
# Deliverables:
# - Implement pmf_expectation, pmf_variance, cdf_from_pmf, plot_pmf_and_cdf.
# - Confirm E[X]=1.1, Var(X)=0.49 for p={0:0.2,1:0.5,2:0.3}.

import math, numpy as np, matplotlib.pyplot as plt

# Given PMF (must sum to 1)
p = {0: 0.2, 1: 0.5, 2: 0.3}

def pmf_expectation(pmf: dict) -> float:
    """Return E[X] for a discrete rv defined by dict pmf {k: P(X=k)}."""
    return sum(k * v for k, v in pmf.items())

def pmf_variance(pmf: dict) -> float:
    """Return Var(X) using Var = E[X^2] - (E[X])^2."""
    mu = pmf_expectation(pmf)
    ex2 = sum((k**2) * v for k, v in pmf.items())
    return ex2 - mu**2

def cdf_from_pmf(pmf: dict, xs) -> dict:
    """Return dict {x: F(x)} with F(x)=P(X<=x)."""
    F = {}
    for x in xs:
        F[x] = sum(v for k, v in pmf.items() if k <= x)
    return F

def plot_pmf_and_cdf(pmf: dict):
    """Two-panel figure: pmf (stem) and cdf (step)."""
    # PMF keys sorted for plotting
    k_sorted = sorted(pmf.keys())
    pmf_vals = [pmf[k] for k in k_sorted]

    # Build CDF values at support points (right-continuous step)
    cdf_vals = []
    running = 0.0
    for k in k_sorted:
        running += pmf[k]
        cdf_vals.append(running)

    fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    # PMF
    ax[0].stem(k_sorted, pmf_vals, basefmt=" ")
    ax[0].set_title("PMF"); ax[0].set_xlabel("k"); ax[0].set_ylabel("P(X=k)")
    ax[0].set_ylim(bottom=0)

    # CDF
    ax[1].step(k_sorted, cdf_vals, where="post")
    ax[1].set_title("CDF"); ax[1].set_xlabel("x"); ax[1].set_ylabel("F(x)")
    ax[1].set_ylim(-0.05, 1.05)

    plt.tight_layout(); plt.show()

# ===== Student Work =====
xs = [-1, 0, 1, 2, 3]
F = cdf_from_pmf(p, xs)
mu = pmf_expectation(p)
var = pmf_variance(p)
print("E[X] =", mu, "  Var(X) =", var)
print("CDF grid:", F)
plot_pmf_and_cdf(p)

# ---- Optional stretch ----
# 1) Change the pmf (keep support {0,1,2}) and see how cdf changes.
# 2) Add a function to validate pmf (nonnegative, sums≈1) and call it before plotting.

# ---- (Instructor) quick checks (uncomment in class) ----
# assert abs(mu - 1.1) < 1e-9
# assert abs(var - 0.49) < 1e-9
# assert abs(F[-1] - 0.0) < 1e-12 and abs(F[3] - 1.0) < 1e-12
