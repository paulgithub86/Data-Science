# ==============================================================================
# A Beginner's Guide to Data Science in Google Colab
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
# We'll use a built-in dataset from the `seaborn` library called 'tips'.
# This is a great way to start because you don't need to upload any files.
# It contains data about restaurant tips, like the total bill, tip amount,
# and other details.

print("Loading the 'tips' dataset...")
df = sns.load_dataset('tips')

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

# Create a histogram to visualize the distribution of 'total_bill'.
# This shows how frequently different bill amounts appear in the data.
plt.figure(figsize=(8, 5))
sns.histplot(df['total_bill'], kde=True, bins=15)
plt.title('Distribution of Total Bill Amounts')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

# Create a bar plot to see the average tip amount for different days of the week.
plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='tip', data=df)
plt.title('Average Tip Amount by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Tip ($)')
plt.show()

# Create a scatter plot to see the relationship between 'total_bill' and 'tip'.
# This helps us see if larger bills generally lead to larger tips.
plt.figure(figsize=(8, 5))
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Relationship Between Total Bill and Tip Amount')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

# Create a box plot to visualize the tip distribution for each day.
# This helps us identify outliers and the spread of data.
plt.figure(figsize=(8, 5))
sns.boxplot(x='day', y='tip', data=df)
plt.title('Tip Distribution by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Tip ($)')
plt.show()

print("\nData analysis and visualization complete!")

# ------------------------------------------------------------------------------
# Exercise for the beginner:
# Try to answer the following questions by modifying the code above or adding new code:
# 1. What is the average 'tip' for men vs. women?
# 2. Create a scatter plot showing the relationship between 'total_bill' and 'tip',
#    but this time, use different colors for 'smoker' and 'non-smoker'.
# ------------------------------------------------------------------------------
