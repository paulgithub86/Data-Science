# CS531 Coding Practice — Answer Key

## 01 — Stats Basics

- Original: mean=24.56, var=94.78, sd=9.74
- With outlier: mean=66.56, var=17619.28, sd=132.74
- MAD(original)=8.00, MAD(outlier)=8.00
- SD blows up with outlier; MAD stable.

## 02 — Missingness Mechanisms

- MCAR p=0.1: bias≈-0.06, run-SD≈1.53
- MCAR p=0.3: bias≈0.15, run-SD≈2.59
- MCAR p=0.6: bias≈nan, run-SD≈nan
- MAR: corr(missing,Age)=-0.580; CC mean=50.0 vs truth 44.5 (biased high).
- Δ-sweep means≈ [42.6, 42.0, 41.0, 40.0]

## 03 — Simple Imputation

- CC mean=50.0; mean-impute→ mean=50.0, sd=5.75; group-median→ mean=49.4, sd=6.63.
- Indicator often carries signal under MAR; include it in downstream model.

## 04 — kNN Imputer

- MAE (no scaling): {1: 9.25, 3: 13.99, 5: 16.63, 7: 16.67}
- With scaling: {1: 9.25, 3: 15.39, 5: 17.83, 7: 18.01}
- With Age^2 (scaled): {1: 9.25, 3: 16.58, 5: 17.72, 7: 17.73}

## 05 — Regression Imputation + Stochastic Residuals

- 50-run pooled mean≈41.55; pooled SD≈15.58 (variance preserved).

## 06 — MICE (IterativeImputer)

- Truth mean=44.50
- M=5: pooled_mean=50.47, Within=55.26, Between=2.9428, Total=58.79
- M=10: pooled_mean=50.73, Within=51.79, Between=1.8594, Total=53.84
- sample_posterior=False: Between→0.0000 (collapse)
- Add Age^2: pooled_mean=50.34 (small shift expected)

## 07 — Outliers

- IQR fences: lo=2.50, hi=92.50; flagged=[1 1 1 1 1 1 1 1 1 1].
- Mean/SD before=90.50/144.46; after winsorize=49.75/19.81.
- Robust-Z(500)≈24.42 (>3).

## 08 — Tidy Reshape

- Subject medians: math=85.0, phys=75.0, chem=82.0
- Wide after impute:
id  chem  math  phys
s1  85.0  80.0  70.0
s2  82.0  90.0  88.0
s3  78.0  85.0  75.0
- Tidy rule satisfied in long form.

## 09 — Data Quality Audit

- Issue counts: {'age_bad': 4, 'email_bad': 1, 'income_na': 4, 'id_dups': 3, 'stale': 17}
- After dedup by latest: unique ids=29 rows=29

## 10 — Pipeline (No Leakage)

- Leaky Ridge (neg MAE): -6.256
- Pipeline Ridge (neg MAE): -5.628
- Pipeline RF (neg MAE): -5.837
- Expect: leaky looks better than it should; pipeline is trustworthy.