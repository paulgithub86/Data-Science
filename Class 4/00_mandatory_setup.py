import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Load and Prepare the Iris Dataset ---
# Load the Iris dataset from scikit-learn
iris = load_iris()

# Create the DataFrame
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])

# Map numerical target to species names
df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
df = df.drop('target', axis=1)

# Set common visualization style for all subsequent sessions
sns.set_style("whitegrid")

# Verify data loaded
print("--- 00. Mandatory Setup Complete ---")
print("DataFrame 'df' loaded successfully. Columns:")
print(df.columns.tolist())
print("-" * 35)

# A function to ensure subsequent files can be run independently in a local environment if needed
def load_df():
    """Returns the initialized Iris DataFrame for subsequent sessions."""
    return df.copy() 

# ---- Classwork ----
# 1. Inspect the output of df.head(). How many features (columns) are numerical?
# 2. What is the role of the 'target' column before it is dropped?
