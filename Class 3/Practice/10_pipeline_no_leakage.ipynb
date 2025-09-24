import numpy as np, pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge

np.random.seed(2025)

# ----- data -----
n = 120
age = np.random.randint(20, 66, size=n)
educ = np.random.choice([12,14,16,18], size=n, p=[0.3,0.3,0.3,0.1])
region = np.random.choice(["North","South","East","West"], size=n)
income = 10 + 0.9*age + 0.8*(educ-12) + np.where(region=="North", 5, 0) + np.random.normal(0,6,size=n)

df = pd.DataFrame({"Age":age, "Educ":educ, "Region":region, "Income":income})

# Induce MAR: some targets (Income) missing
mask_mar = ((df["Age"]<28) | (df["Region"]=="South")) & (np.random.rand(n) < 0.35)
df.loc[mask_mar, "Income"] = np.nan

X = df[["Age","Educ","Region"]]
y = df["Income"]

# ----- BAD (leaky) setup: impute features globally + fill target with global mean -----
X_bad = X.copy()
# cast to float BEFORE injecting NaNs to avoid FutureWarning
X_bad[["Age","Educ"]] = X_bad[["Age","Educ"]].astype("float64")
# inject ~10% feature NaNs, then impute using full data (leakage)
X_bad[["Age","Educ"]] = X_bad[["Age","Educ"]].mask(np.random.rand(n,2) < 0.10)
global_imputer = SimpleImputer(strategy="median").fit(X_bad[["Age","Educ"]])
X_bad[["Age","Educ"]] = global_imputer.transform(X_bad[["Age","Educ"]])
X_bad = pd.get_dummies(X_bad, columns=["Region"], drop_first=True)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
# leaky baseline fills y with the global mean (this is intentionally bad practice)
bad_score_fill = cross_val_score(Ridge(alpha=1.0), X_bad, y.fillna(y.mean()),
                                 cv=kf, scoring="neg_mean_absolute_error").mean()

# (optional) a "less bad" baseline that DROPS missing y but still leaks in features
idx_obs = y.notna()
bad_score_drop = cross_val_score(Ridge(alpha=1.0),
                                 X_bad.loc[idx_obs], y.loc[idx_obs],
                                 cv=kf, scoring="neg_mean_absolute_error").mean()

# ----- GOOD pipeline: no leakage; drop rows with missing target -----
num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
cat_pipe = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore", drop="first"))
])
ct = ColumnTransformer([
    ("num", num_pipe, ["Age","Educ"]),
    ("cat", cat_pipe, ["Region"])
])
pipe = Pipeline([
    ("prep", ct),
    ("model", Ridge(alpha=1.0))
])

good_score = cross_val_score(pipe, X.loc[idx_obs], y.loc[idx_obs],
                             cv=kf, scoring="neg_mean_absolute_error").mean()

print(f"Leaky baseline (y mean-filled): {bad_score_fill:.3f}  (less negative looks 'better' due to leakage)")
print(f"Leaky baseline (drop y-missing): {bad_score_drop:.3f}")
print(f"Pipeline (no leakage, drop y-missing): {good_score:.3f}")

# ---- Classwork ----
# A) Replace Ridge with RandomForestRegressor; compare scores and variance across folds.
#    Hint: from sklearn.ensemble import RandomForestRegressor; set model in 'pipe'.
# B) Move imputation OUTSIDE the pipeline and re-run (expect optimistic scores).
# C) Add an 'Income_missing' indicator to X BEFORE dropping y-missing rows, then drop rows where y is missing,
#    and include that indicator in the pipeline. Does it help?
