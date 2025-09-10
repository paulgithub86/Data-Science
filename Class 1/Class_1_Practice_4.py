# ==============================================================================
# A Beginner's Guide to Data Science with the Penguins Dataset
# ==============================================================================

# This script demonstrates a variety of data visualization techniques using Python.
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
# 2. Load and Prepare the Dataset
# ------------------------------------------------------------------------------
# We'll now use the 'penguins' dataset from the `seaborn` library.
# This dataset contains measurements for three species of penguins.

print("Loading the 'penguins' dataset...")
df = sns.load_dataset('penguins')

# We'll drop rows with missing values to ensure our visualizations are clean.
df.dropna(inplace=True)

# ------------------------------------------------------------------------------
# 3. Explore the Data (Initial Analysis)
# ------------------------------------------------------------------------------
# Data exploration is a crucial first step to understand what's in your data.

# See the first 5 rows of the DataFrame to get a quick look at the data structure.
print("\n--- First 5 rows of the dataset ---")
print(df.head())

# Get a concise summary of the DataFrame.
print("\n--- DataFrame Information ---")
print(df.info())

# Get descriptive statistics for numerical columns, like mean, min, max, etc.
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Check for missing values in the dataset again after dropping.
print("\n--- Missing Values Check ---")
print(df.isnull().sum())

# ------------------------------------------------------------------------------
# 4. Data Visualization
# ------------------------------------------------------------------------------
# Visualizing data helps us spot patterns and relationships that are hard to
# see in raw numbers. We will create a variety of different plot types.

# Bar Plot: Shows the count of penguins on each island.
plt.figure(figsize=(8, 5))
sns.countplot(x='island', data=df, palette='viridis')
plt.title('Count of Penguins by Island')
plt.xlabel('Island')
plt.ylabel('Count')
plt.show()

# Violin Plot: Combines a box plot with a kernel density plot. It is
# great for visualizing the distribution of a numeric variable across
# different categories.
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='body_mass_g', data=df, palette='muted')
plt.title('Distribution of Body Mass by Species')
plt.xlabel('Species')
plt.ylabel('Body Mass (g)')
plt.show()

# Scatter Plot with Hue: Shows the relationship between two numerical
# variables, with different colors for each species. This helps to
# visually separate the data by category.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='flipper_length_mm', y='body_mass_g', hue='species', style='species', data=df, s=100)
plt.title('Flipper Length vs. Body Mass (by Species)')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.legend(title='Species')
plt.show()

# Pair Plot: Creates a grid of plots, showing the relationships between
# all pairs of numerical variables and the distributions of each variable.
# It is an excellent tool for a quick overview of the data.
print("\n--- Generating a Pair Plot... This may take a moment. ---")
sns.pairplot(df, hue='species', markers=['o', 's', 'D'], height=3)
plt.suptitle('Pair Plot of Penguin Characteristics', y=1.02, fontsize=16)
plt.show()

print("\nData analysis and visualization complete!")

# ------------------------------------------------------------------------------
# Exercise for the beginner:
# Try to answer the following questions by modifying the code above or adding new code:
# 1. What is the average 'body_mass_g' for each gender ('sex')?
# 2. Create a box plot showing the distribution of `bill_length_mm` for each species.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Additional Exercises (More Practice!)
# ------------------------------------------------------------------------------
# 3. Find the island with the largest average `flipper_length_mm`.
# 4. Create a new column named 'body_mass_kg' by converting `body_mass_g` to kilograms.
#    Print the first 5 rows of the DataFrame to see your new column.
# 5. Create a histogram of `bill_depth_mm`, using different colors for each species.

# ------------------------------------------------------------------------------
# Solutions (Uncomment the code below to see the answers)
# ------------------------------------------------------------------------------

# print("\n--- Solutions ---")

# # Solution 1: Average body mass by gender
# print("\nAverage body mass by gender:")
# print(df.groupby('sex')['body_mass_g'].mean())

# # Solution 2: Box plot for bill length by species
# plt.figure(figsize=(8, 5))
# sns.boxplot(x='species', y='bill_length_mm', data=df, palette='viridis')
# plt.title('Bill Length Distribution by Species')
# plt.xlabel('Species')
# plt.ylabel('Bill Length (mm)')
# plt.show()

# # Solution 3: Find island with largest average flipper length
# island_avg_flipper_length = df.groupby('island')['flipper_length_mm'].mean()
# max_flipper_length_island = island_avg_flipper_length.idxmax()
# print(f"\nThe island with the largest average flipper length is: {max_flipper_length_island}")

# # Solution 4: Add 'body_mass_kg' column
# df['body_mass_kg'] = df['body_mass_g'] / 1000
# print("\nDataFrame with new 'body_mass_kg' column:")
# print(df.head())

# # Solution 5: Histogram for bill depth with species hue
# plt.figure(figsize=(8, 5))
# sns.histplot(data=df, x='bill_depth_mm', hue='species', multiple='stack', palette='pastel')
# plt.title('Distribution of Bill Depth by Species')
# plt.xlabel('Bill Depth (mm)')
# plt.ylabel('Count')
# plt.show()
