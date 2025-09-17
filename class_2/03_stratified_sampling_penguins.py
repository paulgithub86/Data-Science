# 📘 Perform stratified sampling on a categorical variable

import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the penguins dataset
penguins = sns.load_dataset("penguins").dropna()
print("🔹 Original dataset shape:", penguins.shape)

# Stratified sampling by 'species'
_, sample = train_test_split(
    penguins,
    test_size=0.2,
    stratify=penguins['species'],
    random_state=42
)

# Confirm balanced species
print("🔹 Sample counts by species:")
print(sample['species'].value_counts())

# === 🏠 HOMEWORK ===
# 1. Try changing stratify to 'island' instead of 'species'.
# 2. Visualize the stratified sample using seaborn.pairplot.
# 3. Compare with random sampling – is the distribution preserved?
