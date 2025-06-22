import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Generate sample data
np.random.seed(42)
data = {
    'Normal Distribution': np.random.normal(loc=0, scale=1, size=1000),
    'Uniform Distribution': np.random.uniform(low=-2, high=2, size=1000),
    'Exponential Distribution': np.random.exponential(scale=1.0, size=1000)
}

df = pd.DataFrame(data)

# Plot histograms using seaborn
plt.figure(figsize=(15, 5))

for i, column in enumerate(df.columns, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[column], bins=30, kde=True, color='skyblue')
    plt.title(f'{column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
