import matplotlib.pyplot as plt
import numpy as np

# Sample data: Time or independent variable (e.g., hours, days, etc.)
time = np.linspace(0, 10, 100)  # 100 points between 0 and 10 (time span)

# Dependent variable (e.g., stock prices, temperature, etc.)
data = np.sin(time)  # Using sine function just as an example (you can replace this with your data)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, data, label="Sinusoidal Data", color='b', marker='o', linestyle='-', markersize=5)

# Adding titles and labels
plt.title("Line Plot: Data Over Time", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Data Value", fontsize=12)

# Adding grid for better readability
plt.grid(True)

# Show legend
plt.legend()

# Display the plot
plt.show()
