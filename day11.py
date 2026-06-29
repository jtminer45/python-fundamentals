#Day 11 Project — Real World Data Cleaning
#today you're using a real messy dataset from Kaggle — global tech salaries.
#Requirements:

#Load the dataset and print its shape, columns, and first 5 rows
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Titanic dataset — classic, messy, perfect for cleaning
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())
print(df.shape)

#Check and print missing values per column and percentage missing
print(df.isnull().sum())
print(df.isnull().sum() / len(df) * 100)

#Check and print duplicate rows
print(df.duplicated().sum())
print(df.dtypes)

#Clean the data using a clean_dataframe() function that handles all five problems we covered
def clean_dataframe(df):

#missing values, wrong types, duplicates, formatting, outliers
  df['Age'] = df['Age'].fillna(df['Age'].median())
  df['Cabin'] = df['Cabin'].fillna("Unknown")
  df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
  df.dropna(subset = ['Cabin'])
  
  df["Name"] = df["Name"].astype(str)
  df["Age"] = df["Age"].astype(int)
  df["Pclass"] = df["Pclass"].astype(str)
  
  df["Name"] = df["Name"].str.strip()
  df["Embarked"] = df["Embarked"].str.replace("C", "Cherbourg")
  df["Embarked"] = df["Embarked"].str.replace("S", "Southampton")
  df["Embarked"] = df["Embarked"].str.replace("Q", "Queenstown")
  df["Pclass"] = df["Pclass"].str.replace("1" , "1st")
  df["Pclass"] = df["Pclass"].str.replace("2" , "2nd")
  df["Pclass"] = df["Pclass"].str.replace("3" , "3rd")
  
  
  Q1 = df["Fare"].quantile(0.25)
  Q3 = df["Fare"].quantile(0.75)
  IQR = Q3 - Q1

  df = df[(df["Fare"] >= Q1 - 1.5 * IQR) & (df["Fare"] <= Q3 + 1.5 * IQR)]

  df = df.drop_duplicates()

  return df

#After cleaning print shape again to show how many rows were removed
df = clean_dataframe(df)
print(df.shape)

#Answer these questions in print statements from the cleaned data:

#What is the average salary?
#What is the highest paid job title?
#Which country pays the most on average?
#How many unique job titles are there?
print(f"Average age: {df['Age'].mean():.1f}")
print(f"Overall survival rate: {df['Survived'].mean() * 100:.1f}%")
print(f"\nSurvival rate by class:\n{df.groupby('Pclass')['Survived'].mean() * 100}")
print(f"\nAverage fare by class:\n{df.groupby('Pclass')['Fare'].mean()}")
print(f"\nCleaned data saved to cleaned_titanic.csv")

#save cleaned data to cleaned_salaries.csv
df.to_csv("cleaned_titanic.csv", index=False)

#Plot a bar chart of top 10 highest paying job titles
survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
survival_by_class.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Survival Rate (%)")
plt.tight_layout()
plt.savefig("survival_by_class.png")
plt.show()