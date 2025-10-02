# 🐍 EDA In-Class Coding Sessions: Iris Dataset

Straight to the point: this repo has 8 small, focused Python scripts for hands-on EDA using the classic Iris dataset. Each script targets **one** concept. No bloat, no magic. Classwork questions live in code comments so you can assess on the spot.

[![Open in Colab](https://colab.research.googleusercontent.com/assets/colab-badge.svg)](#) <!-- replace # with your notebook link if you make one -->

---

## What’s Inside

* **01–08 standalone scripts**: Run any script after the one-time setup.
* **Google Colab / Jupyter friendly**: Zero config beyond the usual libs.
* **Built-in assessment**: Look for `# ---- Classwork ----` in each file.

```
.
├─ 00_setup.py                # Run this ONCE per session (or paste the block below)
├─ 01_inspect_structure.py
├─ 02_univariate_numeric.py
├─ 03_univariate_categorical.py
├─ 04_bivariate_continuous.py
├─ 05_bivariate_cat_vs_cont.py
├─ 06_multivariate_heatmap.py
├─ 07_feature_engineering.py
└─ 08_outliers_iqr.py
```

---

## Mandatory Setup (run once)

You **must** run this block **before** any `01_...` to `08_...` script. It loads libraries, the Iris dataset into a shared `df`, and sets a clean viz style.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])
df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
df = df.drop('target', axis=1)

# Set common visualization style
sns.set_style("whitegrid")

# Verify data loaded
print("DataFrame 'df' loaded successfully. Ready for analysis.")
print(df.head())
```

> Tip: Save the block as `00_setup.py` or paste it at the top of your notebook/session. Every numbered script assumes `df` already exists.

---

## Session Breakdown (what each file does)

| File | Primary Focus                         | Key Functions (examples)                                         | EDA Step                      |
| ---- | ------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| 01   | Data Inspection and Structure         | `.shape`, `.head()`, `.info()`, `.describe()`, `.isnull().sum()` | Data Cleaning Setup           |
| 02   | Univariate: Numerical Distribution    | `sns.histplot()`, `sns.boxplot()`, `.skew()`                     | Variable Distribution         |
| 03   | Univariate: Categorical Frequencies   | `.value_counts()`, `sns.countplot()`, `.nunique()`               | Variable Distribution         |
| 04   | Bivariate: Continuous vs. Continuous  | `.corr()`, `sns.scatterplot()`                                   | Relationship Analysis         |
| 05   | Bivariate: Categorical vs. Continuous | `.groupby().mean()`, `sns.violinplot()`                          | Relationship Analysis         |
| 06   | Multivariate: Correlogram Heatmap     | `.corr()`, `sns.heatmap()`                                       | Redundancy Check              |
| 07   | Data Transformation & Engineering     | arithmetic ops (`*`), `sns.histplot()`, `.drop()`                | Feature Creation              |
| 08   | Handling Outliers (IQR Rule)          | `.quantile()`, `.clip()`                                         | Outlier Detection & Treatment |

---

## How to Use

### Option A: Jupyter (local)

1. Clone the repo.
2. Start Jupyter in the repo root.
3. Run `00_setup.py` (or paste the setup block in a cell).
4. Execute any one of `01_...` to `08_...`.

### Option B: Google Colab

1. Upload the scripts or open them from GitHub in Colab.
2. Run the **Mandatory Setup** cell.
3. Run the target session script.

That’s it. Each script is **self-contained** after setup.

---

## Classwork & Assessment

* Every script has a clearly marked:

  ```python
  # ---- Classwork ----
  # Q1: ...
  # Q2: ...
  ```
* Students answer based on the **actual plots/outputs** they just ran.
* Keep answers short and grounded in the visuals/stats shown.

---

## Requirements

* Python 3.8+
* Packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

Install quickly:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Teaching Notes (use or ignore)

* **Consistency**: All scripts assume the same `df` and plotting style.
* **Time-boxed**: Each file is small enough for a 10–20 min in-class block.
* **Swap-in datasets**: Want a different dataset? Keep the same column names or adjust the scripts accordingly. Don’t expect them to magically adapt.

---

## Contributing

* Keep PRs small. One script/feature per PR.
* No giant utility layers; this is classroom code, not a framework.

---

## License

License of choice (MIT).

---

## Troubleshooting

* **Plots look weird?** You didn’t run the setup (style + `df`). Fix that first.
* **`KeyError: species`?** You modified the setup or dropped the column. Put it back or fix the downstream references.
* **Colab “module not found”**: Run `pip install ...` in a cell, then re-run the setup.

---
