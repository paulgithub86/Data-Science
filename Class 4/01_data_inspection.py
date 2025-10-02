# 01 — Data Inspection and Structure

# Load the DataFrame (assuming 00_mandatory_setup.py was run)
# Note: In a Jupyter environment, 'df' persists. We re-import for isolated runnability.
try:
    df = load_df() 
except NameError:
    print("Please run 00_mandatory_setup.py first to define 'load_df()'.")
    exit()

print("--- 01. Data Inspection ---")

# 1. Check the dimensions (rows, columns)
print("\nDataFrame Shape (Rows, Cols):", df.shape)

# 2. Display the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Check data types and non-null counts
print("\nColumn Information (Types and Non-Nulls):")
df.info()

# 4. Generate descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# 5. Check for missing values (Completeness Audit)
print("\nMissing Value Counts per Column:")
print(df.isnull().sum())


# ---- Classwork ----
# A) Based on df.info(), do any columns currently have missing values (NaN)?
# B) Based on df.describe(), what is the average 'sepal length (cm)'?
# C) Why is 'species' not included in the output of df.describe() by default?
