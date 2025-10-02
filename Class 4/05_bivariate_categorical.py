# 05 — Bivariate: Categorical vs. Continuous

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 05. Bivariate Categorical vs. Continuous Analysis ---")

cat_col = 'species'
num_col = 'sepal length (cm)'

# 1. Group-wise summary statistics (Mean, Median, Count)
print(f"\nGroup-wise Summary for '{num_col}' by '{cat_col}':")
group_summary = df.groupby(cat_col)[num_col].agg(['mean', 'median', 'count'])
print(group_summary)


# 2. Visualization: Violin Plot (combines box plot features with kernel density estimation)
plt.figure(figsize=(8, 6))
sns.violinplot(df, x=cat_col, y=num_col, palette=['#ff6e54', '#dd5182', '#444e86'])
plt.title(f'Distribution of {num_col} across {cat_col}')
plt.show()


# ---- Classwork ----
# A) Which species has the largest average 'sepal length (cm)'?
# B) Based on the violin plot, compare the variance (spread) of 'sepal length (cm)' for 'setosa' and 'virginica'.
# C) Why is using the mean in this analysis better than using the overall mean of the entire column?
