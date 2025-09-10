# ==============================================================================
# A Beginner's Guide to Data Science with a New Dataset
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
# We'll now use the 'titanic' dataset from the `seaborn` library.
# This dataset contains information on passengers of the Titanic.

print("Loading the 'titanic' dataset...")
df = sns.load_dataset('titanic')

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

# Create a histogram to visualize the distribution of 'age'.
# This shows how frequently different age groups appear in the data.
plt.figure(figsize=(8, 5))
sns.histplot(df['age'].dropna(), kde=True, bins=15)
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Create a bar plot to see the survival rate for different passenger classes.
plt.figure(figsize=(8, 5))
sns.barplot(x='class', y='survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Create a scatter plot to see the relationship between 'age' and 'fare'.
# This helps us see if ticket prices correlate with passenger age.
plt.figure(figsize=(8, 5))
sns.scatterplot(x='age', y='fare', data=df)
plt.title('Relationship Between Age and Fare')
plt.xlabel('Age')
plt.ylabel('Fare ($)')
plt.show()

# Create a box plot to visualize the fare distribution for each class.
# This helps us identify outliers and the spread of data.
plt.figure(figsize=(8, 5))
sns.boxplot(x='class', y='fare', data=df)
plt.title('Fare Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare ($)')
plt.show()

print("\nData analysis and visualization complete!")

# ------------------------------------------------------------------------------
# Exercise for the beginner:
# Try to answer the following questions by modifying the code above or adding new code:
# 1. What is the average 'age' of men vs. women?
# 2. Create a scatter plot showing the relationship between 'age' and 'fare',
#    but this time, use different colors for 'survived' and 'not survived'.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Additional Exercises (More Practice!)
# ------------------------------------------------------------------------------
# 3. Find the most common passenger class for survivors.
# 4. Create a new column named 'family_size' that is the sum of `sibsp` and `parch`.
#    Print the first 5 rows of the DataFrame to see your new column.
# 5. Create a bar plot showing the survival rate for different family sizes.

# ------------------------------------------------------------------------------
# Solutions (Uncomment the code below to see the answers)
# ------------------------------------------------------------------------------

# print("\n--- Solutions ---")

# # Solution 1: Average age for men vs. women
# print("\nAverage age by gender:")
# print(df.groupby('sex')['age'].mean())

# # Solution 2: Scatter plot with colors for survival status
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x='age', y='fare', hue='survived', data=df)
# plt.title('Age vs. Fare (by Survival Status)')
# plt.xlabel('Age')
# plt.ylabel('Fare ($)')
# plt.show()

# # Solution 3: Most common class for survivors
# survived_data = df[df['survived'] == 1]
# most_common_class = survived_data['class'].mode()[0]
# print(f"\nThe most common class for survivors is: {most_common_class}")

# # Solution 4: Add 'family_size' column
# df['family_size'] = df['sibsp'] + df['parch']
# print("\nDataFrame with new 'family_size' column:")
# print(df.head())

# # Solution 5: Bar plot for survival rate by family size
# plt.figure(figsize=(8, 5))
# sns.barplot(x='family_size', y='survived', data=df)
# plt.title('Survival Rate by Family Size')
# plt.xlabel('Family Size')
# plt.ylabel('Survival Rate')
# plt.show()
