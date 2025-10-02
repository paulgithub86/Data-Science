# 02 — Univariate: Numerical Distribution

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 02. Univariate Numerical Analysis ---")

# We will focus on 'sepal length (cm)'

numerical_col = 'sepal length (cm)'

# 1. Calculate summary statistics including skewness
print(f"\nSummary Stats for '{numerical_col}':")
print(f"Mean: {df[numerical_col].mean():.2f}")
print(f"Median: {df[numerical_col].median():.2f}")
print(f"Skewness: {df[numerical_col].skew():.2f}")


# 2. Visualization: Histogram to show frequency distribution
plt.figure(figsize=(8, 4))
sns.histplot(df, x=numerical_col, kde=True, bins=20, color='#444e86')
plt.title(f'Distribution of {numerical_col}')
plt.show()


# 3. Visualization: Box Plot to identify central tendency, spread, and potential outliers
plt.figure(figsize=(8, 2))
sns.boxplot(df, x=numerical_col, color='#955196')
plt.title(f'Box Plot of {numerical_col}')
plt.show()


# ---- Classwork ----
# A) Is the distribution of 'sepal length (cm)' positively or negatively skewed? What does this mean for the tail?
# B) Does the box plot show any clear outliers for 'sepal length (cm)'?
# C) How does the Mean compare to the Median for this feature?
