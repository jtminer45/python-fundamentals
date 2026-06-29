#Day 12 Project — Full EDA Report on Real Data
#using the same Titanic dataset from yesterday — already cleaned. Load your cleaned_titanic.csv.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_titanic.csv")

#Load cleaned data and print shape, info, describe
print(df.shape)
print(df.info())
print(df.describe())

#Distribution plots for Age, Fare — histogram with KDE curve
sns.histplot(df[['Age', 'Fare']], bins=10, kde=True)
plt.title("Age-Fare Distrubtion")
plt.tight_layout()
plt.savefig("age_fare_distubtion.png")
plt.show()

#Count plots for Survived, Pclass, Sex — how balanced are the classes?
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.countplot(x="Survived", data=df, ax=axes[0])
axes[0].set_title("Survival Count")
sns.countplot(x="Pclass", data=df, ax=axes[1])
axes[1].set_title("Passenger Class Count")
sns.countplot(x="Sex", data=df, ax=axes[2])
axes[2].set_title("Sex Count")
plt.tight_layout()
plt.savefig("count_plots.png")
plt.show()

#Survival rate breakdown by Sex, Pclass, and Embarked using groupby
print(f"Survival by Sex:\n{df.groupby('Sex')['Survived'].mean() * 100}")
print(f"Survival by Pclass:\n{df.groupby('Pclass')['Survived'].mean() * 100}")
print(f"Survival by Embarked:\n{df.groupby('Embarked')['Survived'].mean() * 100}")

sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df)
plt.title("Survival Rate by Class and Sex")
plt.tight_layout()
plt.savefig("survival_by_class_sex.png")
plt.show()

#Correlation heatmap of all numeric columns
correlation = df[["PassengerId", "Survived", "Age", "SibSp", "Parch", "Fare"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("heatmap_all_numeric_data.png")
plt.show()

##Scatter plot of Age vs Fare coloured by Survived
plt.figure(figsize=(10, 7))
survived = df[df["Survived"] == 1]
died = df[df["Survived"] == 0]
plt.scatter(died["Age"], died["Fare"], alpha=0.5, s=50, label="Died", color="red")
plt.scatter(survived["Age"], survived["Fare"], alpha=0.5, s=50, label="Survived", color="green")
plt.title("Age vs Fare coloured by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_age_fare_survival.png")
plt.show()

#Box plot of Fare by Pclass
sns.boxplot(x="Fare", y="Pclass", data=df)
plt.title("Fare vs Pclass")
plt.tight_layout()
plt.savefig("box_plot_fare_pclass.png")
plt.show()

#Write 5 observations as comments in your code — what does the data actually tell you?


#Save all plots as PNG files

