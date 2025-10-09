# CS531 — Class 5 Assignment
# 05 — Expectation: Linearity & LOTUS (≈8 min)
# Learning goals:
# - Compute E[g(X)] for discrete pmf via LOTUS; connect to Var(X).
# - Numerically integrate E[g(X)] for continuous pdfs.

import numpy as np, math

def E_discrete(pmf_k: np.ndarray, pmf_p: np.ndarray, g) -> float:
    """Return E[g(X)] for discrete X with support pmf_k and probs pmf_p."""
    return float(np.sum(pmf_p * np.vectorize(g)(pmf_k)))

def poisson_pmf_up_to(lam: float, K: int) -> tuple[np.ndarray, np.ndarray]:
    """Return (ks, pmf) for k=0..K."""
    ks = np.arange(0, K + 1)
    pmf = np.array([math.exp(-lam) * lam**int(k) / math.factorial(int(k)) for k in ks], dtype=float)
    return ks, pmf

def E_continuous_trapz(x: np.ndarray, pdf: np.ndarray, g) -> float:
    """Return E[g(X)] ≈ ∫ g(x) f(x) dx via trapezoidal rule on grid x."""
    gx = np.vectorize(g)(x)
    return float(np.trapz(gx * pdf, x))

# ===== Student Work =====
# 1) X ~ Poisson(λ=3): compute E[X], E[X^2], Var(X).
lam = 3.0
ks, pmf = poisson_pmf_up_to(lam, K=20)
EX  = E_discrete(ks, pmf, g=lambda k: k)
EX2 = E_discrete(ks, pmf, g=lambda k: k**2)
Var = EX2 - EX**2
print("Poisson(3): E[X]~", EX, " E[X^2]~", EX2, " Var~", Var)

# 2) Continuous: X ~ Exp(λ=2). Estimate E[sqrt(X)].
lam2 = 2.0
xs = np.linspace(0, 5, 20001)
fx = lam2 * np.exp(-lam2 * xs)
EXg = E_continuous_trapz(xs, fx, g=np.sqrt)
print("Exp(2): E[sqrt(X)] ≈", EXg)

# ---- Optional stretch ----
# 1) Derive closed form E[X^2] for Poisson (= λ^2 + λ) and compare.
# 2) Try g(x)=x^q for q in {0.5, 1.5, 2.5} on Exp(λ).

# ---- (Instructor) quick checks (uncomment) ----
# assert abs(Var - lam) < 0.05
