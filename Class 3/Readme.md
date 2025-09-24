# Create a README.md summarizing the 10 notebooks, with an announcement that 1–8 are essential and 9–10 are bonus.
readme = """# CS531 — Data Cleaning & Imputation: 1-Hour Coding Practice

> **Announcement:** The **first 8 notebooks are essential** for everyone. **Notebooks 9 and 10 are bonus** for highly motivated students who want extra challenge and polish.

This pack contains 10 Colab-ready notebooks (easy → hard). Each notebook has a brief explanation and a **Classwork** section you can finish in a few minutes. Total time ≈ **60 minutes** if you complete 1–8; add ~15–20 minutes for 9–10.

---

## How to use
1. Open each `.ipynb` in Google Colab (or local Jupyter).
2. Run all cells top-to-bottom.
3. Do the **Classwork** block at the bottom of each notebook.
4. If you’re fast, attempt the bonus notebooks (9–10).

**Prereqs:** Basic Python + NumPy/Pandas; for some notebooks you’ll need scikit-learn and matplotlib (Colab already has them).

---

## 01 — Stats Basics: Mean, Variance, Standard Deviation (Essential)
**What you learn:** Compute mean, sample variance, and SD from scratch and via NumPy; see how an outlier distorts SD but not MAD.  
**Connects to slides:** Foundations before missingness and outliers.  
**Classwork:** Inject an outlier (42→420), recompute; implement `mad(xs)`; compare SD vs MAD.
**Expected:** Mean/SD jump with outlier; MAD barely changes.

## 02 — Missingness Mechanisms: MCAR, MAR, MNAR (Essential)
**What you learn:** Simulate MCAR/MAR/MNAR on the toy (Age, Educ, Income) table and measure bias of complete-case mean.  
**Connects:** Mechanisms matter. Deletion OK only under MCAR.  
**Classwork:** MCAR p ∈ {0.1,0.3,0.6} (bias spread); show MAR correlation with Age; MNAR Δ-adjustment idea.
**Expected:** MCAR unbiased on average; MAR/MNAR complete-case mean biased high here.

## 03 — Simple Imputation: Mean/Median/Group-wise (Essential)
**What you learn:** Global mean/median kill variance; group-wise median reduces bias; add a missingness indicator.  
**Connects:** Variance distortion warning; indicators can help under MAR.  
**Classwork:** Fit a tiny regression using the indicator; compare bias and SD across strategies.
**Expected:** Group-wise usually beats global mean; indicator has signal.

## 04 — kNN Imputation (Essential)
**What you learn:** Use `KNNImputer`; tune `k`; importance of scaling.  
**Connects:** Local structure vs global plug-ins.  
**Classwork:** Try k = 1,3,5,7; add z-scaling; try `Age^2`.
**Expected:** Scaling improves MAE; best k is small here; extra features help only if relevant.

## 05 — Regression Imputation + Stochastic Residuals (Essential)
**What you learn:** Impute with `Income ~ Age + Educ` and **add random residual** to preserve variance.  
**Connects:** Why single deterministic imputation underestimates uncertainty.  
**Classwork:** Repeat 50 times; pool mean/variance (Rubin intuition).
**Expected:** Stochastic approach restores SD; pooled mean close to truth.

## 06 — Multiple Imputation (MICE) via IterativeImputer (Essential)
**What you learn:** Run m=5 imputations; compute within/between/total variance; see posterior sampling effect.  
**Connects:** Proper uncertainty accounting.  
**Classwork:** Vary m; toggle `sample_posterior`; add `Age^2` predictor.
**Expected:** Turning off posterior collapses between-imputation variance; total variance drops.

## 07 — Outliers: Z, Robust-Z (MAD), IQR Rule (Essential)
**What you learn:** Detect outliers with robust-Z and IQR; show winsorization (clipping) effect.  
**Connects:** Robust stats before modeling.  
**Classwork:** Winsorize dataset with a 500 outlier; compare detection rules.
**Expected:** Means stabilize after clipping; robust-Z flags extreme point (>3).

## 08 — Tidy Data: Melt & Pivot (Essential)
**What you learn:** Convert wide→long→wide; handle missing scores deliberately.  
**Connects:** Tidy principles (variables/rows/cells).  
**Classwork:** Impute subject medians before pivot; add a `term` column and build a subject×term matrix.
**Expected:** Long form passes tidy rules; pivot back cleanly.

---

## 09 — Data Quality Audit (Bonus)
**What you learn:** Run a compact audit over **Accuracy, Completeness, Consistency, Validity, Uniqueness, Timeliness** with flags + counts.  
**Classwork:** Write `audit_report(df)`; define SLAs (e.g., ≤10% missing `income`); deduplicate by latest timestamp.
**Expected:** Some SLAs fail; dedup by newest resolves duplicate IDs.

## 10 — Model-Aware Pipeline (No Leakage) + CV (Bonus)
**What you learn:** Proper scikit-learn `Pipeline` with `ColumnTransformer`, imputation, scaling, and encoding **inside** CV; compare to a leaky setup.  
**Classwork:** Swap Ridge→RandomForest; move imputation outside pipeline to see score inflation; add `Income_missing` indicator and reassess.
**Expected:** Leaky baseline looks “better” (optimistically high). Pipeline gives honest (more negative) MAE.

---

## Tips for success
- **Never impute the target `y`.** Drop rows with missing targets for supervised tasks.
- Fit imputers and scalers **inside** CV folds (via pipeline).
- Log which rows/columns were imputed and why (provenance matters).
- Prefer robust stats (median/MAD) when you suspect outliers.

---

## File list
- `01_stats_basics.ipynb`
- `02_missingness_masks.ipynb`
- `03_simple_imputation.ipynb`
- `04_knn_imputation.ipynb`
- `05_regression_imputation.ipynb`
- `06_mice_iterative_imputer.ipynb`
- `07_outliers_univariate.ipynb`
- `08_tidy_reshape.ipynb`
- `09_data_quality_audit.ipynb`  *(bonus)*
- `10_pipeline_no_leakage.ipynb` *(bonus)*

"""
