# 08 — Handling Outliers (IQR Rule)

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 08. Outlier Handling (IQR Rule) ---")

# Create a temporary working column and deliberately introduce an outlier
outlier_col = 'sepal width (cm)'
df_outlier = df.copy()
df_outlier.loc[149, outlier_col] = 10.0 # Introduce a clear outlier for demonstration

# 1. Calculate Q1, Q3, and IQR
Q1 = df_outlier[outlier_col].quantile(0.25)
Q3 = df_outlier[outlier_col].quantile(0.75)
IQR = Q3 - Q1
print(f"\nQ1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")


# 2. Define IQR fences
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR
print(f"Lower Fence (1.5*IQR): {lower_fence:.2f}")
print(f"Upper Fence (1.5*IQR): {upper_fence:.2f}")


# 3. Identify and count outliers
outliers = df_outlier[~df_outlier[outlier_col].between(lower_fence, upper_fence)]
print(f"\nNumber of Outliers detected: {len(outliers)}")
print("Outlier row(s) detected:")
print(outliers[[outlier_col, 'species']])


# 4. Outlier Treatment: Capping (Winsorization)
# Capping replaces the outlier value with the closest fence value.
df_capped = df_outlier.copy()
df_capped[outlier_col] = df_capped[outlier_col].clip(lower=lower_fence, upper=upper_fence)

print(f"\nValue at original index 149 before capping: {df_outlier.loc[149, outlier_col]:.2f}")
print(f"Value at original index 149 after capping: {df_capped.loc[149, outlier_col]:.2f} (Capped to Upper Fence)")


# ---- Classwork ----
# A) Calculate the lower and upper fences using the 3.0 * IQR rule (Extreme Outliers). How many outliers are detected now?
# B) Instead of capping, how would you write the code to remove the outliers entirely (Dropping)?
# C) Why is capping generally preferred over dropping in time series data?
