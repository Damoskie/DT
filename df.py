import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample dataset (you can replace this with your dataset)
df = sns.load_dataset("iris")

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Pairplot - Great for quick multivariate overview
sns.pairplot(df, hue="species", diag_kind="kde", markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# Violin Plot - Distribution by Category
plt.figure(figsize=(10, 6))
sns.violinplot(x="species", y="sepal_length", data=df, palette="Set2")
plt.title("Violin Plot of Sepal Length by Species")
plt.show()

# Boxen Plot - Advanced version of boxplot (better for larger datasets)
plt.figure(figsize=(10, 6))
sns.boxenplot(x="species", y="petal_width", data=df, palette="coolwarm")
plt.title("Boxen Plot of Petal Width by Species")
plt.show()

# Heatmap - Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Swarm Plot - Combine with box or violin
plt.figure(figsize=(10, 6))
sns.violinplot(x="species", y="petal_length", data=df, inner=None, palette="Pastel1")
sns.swarmplot(x="species", y="petal_length", data=df, color="k", alpha=0.6)
plt.title("Violin + Swarm Plot of Petal Length by Species")
plt.show()
