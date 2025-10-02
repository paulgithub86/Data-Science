# 07 — Data Transformation and Engineering

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 07. Feature Engineering ---")

# Create a copy to avoid modifying the original 'df' state for later sessions
df_eng = df.copy()

# 1. Feature Creation: Calculate a new feature 'petal_area' (Length * Width)
df_eng['petal_area'] = df_eng['petal length (cm)'] * df_eng['petal width (cm)']

# 2. Feature Creation: Calculate a ratio feature 'sepal_ratio' (Length / Width)
df_eng['sepal_ratio'] = df_eng['sepal length (cm)'] / df_eng['sepal width (cm)']

print("\nDataFrame with new features:")
print(df_eng[['petal length (cm)', 'petal width (cm)', 'petal_area', 'sepal_ratio']].head())

# 3. Visualization: Check the distribution of the new 'petal_area' feature
plt.figure(figsize=(8, 4))
sns.histplot(df_eng, x='petal_area', kde=True, bins=20, color='#ffa600')
plt.title('Distribution of New Feature: Petal Area')
plt.show()


# ---- Classwork ----
# A) Does the distribution of 'petal_area' appear more or less normal than the individual length/width distributions (Session 02)?
# B) Calculate the correlation between the new 'petal_area' feature and 'sepal length (cm)'. Is it stronger or weaker than the original?
# C) Why might 'sepal_ratio' be a better feature for classification than 'sepal length (cm)' alone?
