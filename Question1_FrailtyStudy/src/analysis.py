import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure results directory exists
os.makedirs("../results", exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv("../data/clean_data.csv")

# Compute Summary Statistics
summary_stats = df.describe()

# Save summary statistics to a text file
summary_path = "../results/summary_statistics.txt"
with open(summary_path, "w") as f:
    f.write(summary_stats.to_string())

print(f"Summary statistics saved at: {summary_path}")

# Create a Box Plot of Grip Strength grouped by Frailty
plt.figure(figsize=(8, 6))
sns.boxplot(x="Frailty", y="Grip Strength", data=df, palette="Set2")
plt.title("Grip Strength Distribution by Frailty")
plt.xlabel("Frailty (Y = Yes, N = No)")
plt.ylabel("Grip Strength (kg)")

# Save the visualization
plot_path = "../results/visualization.png"
plt.savefig(plot_path)
plt.show()

print(f"Visualization saved at: {plot_path}")

print("Analysis completed successfully!")
