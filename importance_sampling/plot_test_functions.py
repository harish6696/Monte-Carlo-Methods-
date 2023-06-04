import numpy as np
import matplotlib.pyplot as plt

# Define the interval [0, π/2]
x = np.linspace(0, np.pi/2, 100)

# Function 1: sin(x)
y1 = np.sin(x)

# Function 2: 8x/π²
y2 = (8 * x) / (np.pi**2)

# Function 3: 2/π
y3 = 2 / np.pi * np.ones(x.shape)

# Plotting the functions
plt.plot(x, y1, label='original_function: sin(x)',linestyle='solid' )
plt.plot(x, y2, label='q(x): 8x/π²', linestyle='dashed')
plt.plot(x, y3, label='p(x): 2/π', linestyle='dashed')

# Set the x-axis and y-axis labels
plt.xlabel('x')
plt.ylabel('y')

# Set the title of the plot
plt.title('Importance Sampling Test Setup')

# Display the legend
plt.legend()

# Display the plot
plt.show()
