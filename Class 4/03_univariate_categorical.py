# 03 — Univariate: Categorical Frequencies

# Load the DataFrame
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 03. Univariate Categorical Analysis ---")

categorical_col = 'species'

# 1. Count the number of unique categories
unique_count = df[categorical_col].nunique()
print(f"\nNumber of Unique Species: {unique_count}")


# 2. Get the frequency of each category
print(f"\nValue Counts for '{categorical_col}':")
print(df[categorical_col].value_counts())


# 3. Visualization: Count Plot (Bar Chart)
plt.figure(figsize=(8, 5))
sns.countplot(df, y=categorical_col, palette=['#ff6e54', '#dd5182', '#444e86'])
plt.title(f'Frequency of {categorical_col} Categories')
plt.show()


# ---- Classwork ----
# A) Is the 'species' variable balanced (equal counts for each category)? Why is this important for model training?
# B) If the dataset had 10 different flower species, what would df['species'].nunique() return?
# C) What percentage of the data belongs to the 'setosa' species?
