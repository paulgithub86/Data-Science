# CS531 — Class 5 Assignment
# 03 — Geometric: waiting-time & memoryless (≈7 min)
# Learning goals:
# - Implement Geometric sampling (inverse-transform); verify mean/var; test memoryless property.

import numpy as np, math
rng = np.random.default_rng(42)

def geometric_inverse_transform(p: float, size: int) -> np.ndarray:
    """Return samples in {1,2,...} using inverse-transform: G = ceil(log(1-U)/log(1-p))."""
    U = rng.random(size)  # in [0,1)
    return np.ceil(np.log(1 - U) / np.log(1 - p)).astype(int)

def prob_tail_geometric(p: float, k: int) -> float:
    """Return P(G>k) = (1-p)^k."""
    return (1 - p) ** k

def memoryless_empirical(samples: np.ndarray, s: int, t: int) -> float:
    """Estimate P(G>s+t | G>s)."""
    mask = samples > s
    if mask.sum() == 0:
        return np.nan
    return (samples[mask] > (s + t)).mean()

# ===== Student Work =====
p = 0.2
m = 50_000
G = geometric_inverse_transform(p, m)

print("Empirical mean:", G.mean(), " theory:", 1/p)
print("Empirical var:", G.var(), " theory:", (1 - p) / (p ** 2))

for k in [5, 10]:
    print(f"P(G>{k}) empirical:", (G > k).mean(), " theory:", prob_tail_geometric(p, k))

s, t = 5, 7
lhs = memoryless_empirical(G, s, t)
rhs = (G > t).mean()
print("Memoryless empirical:", lhs, " RHS:", rhs)

# ---- Optional stretch ----
# 1) Show that P(G>s+t) ≈ P(G>s) P(G>t) for geometric (derive).
# 2) Replace p by an array of ps and vectorize the function.

# ---- (Instructor) quick checks (uncomment) ----
# assert abs(G.mean() - 1/p) < 0.2
# assert abs(lhs - rhs) < 0.02
