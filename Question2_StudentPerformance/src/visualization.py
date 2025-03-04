import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("../data/student_data.csv")

# Ensure results directory exists
os.makedirs("../results", exist_ok=True)

# 1. Histogram of Math Scores
plt.figure(figsize=(8,6))
sns.histplot(df['math score'], bins=15, kde=True, color="blue")
plt.title("Distribution of Math Scores")
plt.savefig("../results/plot1.png")
plt.show()

# 2. Box Plot of Reading Scores by Gender (Fixed Warning)
plt.figure(figsize=(8,6))
sns.boxplot(x='gender', y='reading score', data=df, hue='gender', palette="Set2")
plt.title("Reading Scores by Gender")
plt.savefig("../results/plot2.png")
plt.show()

# 3. Scatter Plot: Math vs Reading Score
plt.figure(figsize=(8,6))
sns.scatterplot(x='math score', y='reading score', data=df, color="green")
plt.title("Math Score vs Reading Score")
plt.savefig("../results/plot3.png")
plt.show()

# 4. Bar Chart: Writing Score by Parental Education
plt.figure(figsize=(10,6))
avg_writing = df.groupby('parental level of education')['writing score'].mean().reset_index()
sns.barplot(x='parental level of education', y='writing score', data=avg_writing, palette="muted")
plt.xticks(rotation=45)
plt.title("Average Writing Score by Parental Education")
plt.savefig("../results/plot4.png")
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['math score', 'reading score', 'writing score']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Scores")
plt.savefig("../results/plot5.png")
plt.show()

print("Visualizations generated and saved!")
