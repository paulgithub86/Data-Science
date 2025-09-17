# 📘 Load a structured CSV and perform simple random sampling

import pandas as pd
import numpy as np

# Load CSV from URL (Iris dataset)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("🔹 Original dataset shape:", df.shape)

# Simple Random Sampling (SRS) - sample 20 rows
sample_df = df.sample(n=20, random_state=42)
print("🔹 Sampled dataset shape:", sample_df.shape)

# Show sample
sample_df.head()

# === 🏠 HOMEWORK ===
# 1. Try changing n=20 to other values like 10, 50.
# 2. Use sample(frac=0.2) instead of n.
# 3. What happens if you set random_state=None each time?
