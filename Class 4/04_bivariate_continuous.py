# 04 — Bivariate: Continuous vs. Continuous

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 04. Bivariate Continuous Analysis ---")

# Focus on the relationship between Petal Length and Petal Width

x_col = 'petal length (cm)'
y_col = 'petal width (cm)'

# 1. Calculate the Pearson Correlation Coefficient
correlation = df[[x_col, y_col]].corr().loc[x_col, y_col]
print(f"\nCorrelation ({x_col} vs {y_col}): {correlation:.3f}")


# 2. Visualization: Scatter Plot
plt.figure(figsize=(8, 6))
# Add 'species' as a hue to see group separation (multivariate view)
sns.scatterplot(df, x=x_col, y=y_col, hue='species', palette=['#ff6e54', '#dd5182', '#444e86'])
plt.title(f'Relationship between {x_col} and {y_col}')
plt.show()


# ---- Classwork ----
# A) Describe the strength and direction of the correlation between the two variables.
# B) Based on the scatter plot, which species group exhibits the highest correlation between petal length and width?
# C) If the correlation was close to -1.0, what would the scatter plot look like?
