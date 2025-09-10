# ==============================================================================
# A Beginner's Guide to Data Science with the Iris Dataset
# ==============================================================================

# This script demonstrates fundamental data science concepts using Python.
# It's designed for beginners and can be run directly in Google Colab.

# ------------------------------------------------------------------------------
# 1. Setup and Imports
# ------------------------------------------------------------------------------
# First, we need to import the necessary libraries.
# `pandas` is for data manipulation and analysis.
# `numpy` is for numerical operations.
# `matplotlib.pyplot` and `seaborn` are for creating data visualizations.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# We will also set a style for the plots to make them look nice.
sns.set_style("whitegrid")

# ------------------------------------------------------------------------------
# 2. Load the Dataset
# ------------------------------------------------------------------------------
# We'll now use the 'iris' dataset from the `seaborn` library.
# This dataset contains measurements of sepal and petal dimensions for three species of iris flowers.

print("Loading the 'iris' dataset...")
df = sns.load_dataset('iris')

# ------------------------------------------------------------------------------
# 3. Explore the Data (Initial Analysis)
# ------------------------------------------------------------------------------
# Data exploration is a crucial first step to understand what's in your data.

# See the first 5 rows of the DataFrame to get a quick look at the data structure.
print("\n--- First 5 rows of the dataset ---")
print(df.head())

# Get a concise summary of the DataFrame. This tells us about data types,
# non-null values, and memory usage.
print("\n--- DataFrame Information ---")
print(df.info())

# Get descriptive statistics for numerical columns, like mean, min, max, etc.
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Check for missing values in the dataset.
print("\n--- Missing Values Check ---")
print(df.isnull().sum())


# ------------------------------------------------------------------------------
# 4. Data Visualization
# ------------------------------------------------------------------------------
# Visualizing data helps us spot patterns and relationships that are hard to
# see in raw numbers.

# Create a histogram to visualize the distribution of 'sepal_length'.
# This shows how frequently different sepal lengths appear in the data.
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_length'], kde=True, bins=15)
plt.title('Distribution of Sepal Lengths')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Create a bar plot to see the average petal width for each species.
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal_width', data=df)
plt.title('Average Petal Width by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Width (cm)')
plt.show()

# Create a scatter plot to see the relationship between 'sepal_length' and 'sepal_width'.
# This helps us see if these two measurements are correlated.
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df)
plt.title('Relationship Between Sepal Length and Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Create a box plot to visualize the sepal length distribution for each species.
# This helps us identify outliers and the spread of data.
plt.figure(figsize=(8, 5))
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Sepal Length Distribution by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()

print("\nData analysis and visualization complete!")

# ------------------------------------------------------------------------------
# Exercise for the beginner:
# Try to answer the following questions by modifying the code above or adding new code:
# 1. What is the average 'sepal_length' for each of the three species?
# 2. Create a scatter plot showing the relationship between 'petal_length' and 'petal_width',
#    but this time, use different colors for each 'species'.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Additional Exercises (More Practice!)
# ------------------------------------------------------------------------------
# 3. Find the species that has the largest average 'petal_length'.
# 4. Create a new column named 'sepal_area' which is the product of `sepal_length` and `sepal_width`.
#    Print the first 5 rows of the DataFrame to see your new column.
# 5. Create a box plot showing the distribution of 'sepal_area' for each species.

# ------------------------------------------------------------------------------
# Solutions (Uncomment the code below to see the answers)
# ------------------------------------------------------------------------------

# print("\n--- Solutions ---")

# # Solution 1: Average sepal length for each species
# print("\nAverage sepal length by species:")
# print(df.groupby('species')['sepal_length'].mean())

# # Solution 2: Scatter plot with colors for each species
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df)
# plt.title('Petal Length vs. Petal Width (by Species)')
# plt.xlabel('Petal Length (cm)')
# plt.ylabel('Petal Width (cm)')
# plt.show()

# # Solution 3: Find species with largest average petal length
# species_avg_petal_length = df.groupby('species')['petal_length'].mean()
# max_petal_length_species = species_avg_petal_length.idxmax()
# print(f"\nThe species with the largest average petal length is: {max_petal_length_species}")

# # Solution 4: Add 'sepal_area' column
# df['sepal_area'] = df['sepal_length'] * df['sepal_width']
# print("\nDataFrame with new 'sepal_area' column:")
# print(df.head())

# # Solution 5: Box plot for sepal area by species
# plt.figure(figsize=(8, 5))
# sns.boxplot(x='species', y='sepal_area', data=df)
# plt.title('Sepal Area Distribution by Species')
# plt.xlabel('Species')
# plt.ylabel('Sepal Area (cm²)')
# plt.show()
