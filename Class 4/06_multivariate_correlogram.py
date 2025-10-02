# 06 — Multivariate: Correlogram Heatmap

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 06. Multivariate Correlogram ---")

# 1. Calculate the Correlation Matrix for all numerical features
# Exclude the categorical 'species' column
corr_matrix = df.drop(columns=['species']).corr()
print("\nCorrelation Matrix:")
print(corr_matrix)


# 2. Visualization: Heatmap
plt.figure(figsize=(7, 6))
sns.heatmap(corr_matrix, 
            annot=True,        # Show the correlation values on the map
            cmap='viridis',    # Color map
            fmt=".2f",         # Format numbers to 2 decimal places
            linewidths=.5,     # Lines between cells
            cbar=True)         # Color bar
plt.title('Correlogram (Correlation Heatmap)')
plt.show()


# ---- Classwork ----
# A) Which two numerical features show the strongest positive linear correlation?
# B) Identify the features with the weakest correlation (closest to zero).
# C) If two features are highly correlated (e.g., > 0.9), what potential issue might arise in a linear machine learning model?
