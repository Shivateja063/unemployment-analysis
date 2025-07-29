
# VISUALISING AND ANALYZING THE UNEMPLOYMENT RATE DATASET

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Mount Google Drive if running in Colab (uncomment if needed)
# from google.colab import drive
# drive.mount('/content/drive')

# Load dataset
path = 'data/output.csv'  # Change path accordingly if using locally
df = pd.read_csv(path)

# Basic dataset exploration
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print("Shape of DataFrame:", df.shape)

# Check missing values
print("Missing values:
", df.isnull().sum())

# Number of unique states and counties
print("Unique States:", df['State'].nunique())
print("Unique Counties:", df['County'].nunique())

# Highest unemployment rate by county
max_rate_county = df.groupby('Rate').max()
print("Max unemployment rate county:
", max_rate_county)

# Check for missing states
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Idaho', 'Hawaii', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

print("Missing states:")
for state in states:
    if state not in df['State'].unique():
        print(state)

# San Juan County - highest unemployment example
san_juan = df[(df['County'] == 'San Juan County') & (df['State'] == 'Colorado')]
print(san_juan)

# Plot San Juan County across 1990–1995
for year in range(1990, 1996):
    plt.figure(figsize=(10, 4))
    subset = san_juan[san_juan['Year'] == year]
    sns.pointplot(x='Month', y='Rate', data=subset)
    plt.title(f'San Juan County Unemployment Rate - {year}')
    plt.ylabel('Unemployment Rate')
    plt.xlabel('Month')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# State frequency count
plt.figure(figsize=(12, 6))
sns.barplot(x=df['State'].value_counts().index, y=df['State'].value_counts().values)
plt.xticks(rotation='vertical')
plt.title('Number of Records per State')
plt.ylabel('Count')
plt.xlabel('State')
plt.tight_layout()
plt.show()

# Highest unemployment by state
group = df.groupby("State")["Rate"].max().reset_index()
plt.figure(figsize=(14, 6))
sns.pointplot(x='State', y='Rate', data=group)
plt.xticks(rotation='vertical')
plt.title("Max Unemployment Rate by State")
plt.tight_layout()
plt.show()

# Texas and Colorado during recession years
recession_years = [1990, 1991, 2001, 2007, 2008, 2009]
for state in ['Texas', 'Colorado']:
    st_df = df[df['State'] == state]
    for year in recession_years:
        if year in st_df['Year'].unique():
            plt.figure(figsize=(10, 4))
            ydf = st_df[st_df['Year'] == year]
            sns.pointplot(x='Month', y='Rate', data=ydf)
            plt.title(f'{state} Unemployment Rate - {year}')
            plt.ylabel('Rate')
            plt.xlabel('Month')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

# Counties with lowest unemployment
lowest = df.set_index('County').sort_values(by='Rate')
print("Lowest Unemployment Rate Counties:
", lowest['Rate'].head(20))

# Max unemployment rate by year
by_year = df.groupby("Year")["Rate"].max().reset_index()
plt.figure(figsize=(14, 6))
sns.pointplot(x='Year', y='Rate', data=by_year)
plt.title("Max Unemployment Rate by Year")
plt.tight_layout()
plt.show()
