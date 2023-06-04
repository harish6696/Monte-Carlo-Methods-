import numpy as np
import matplotlib.pyplot as plt

#This code compares points generated in 2D using psudo-random numbers vs points generated using Halton sequence
def generate_pseudo_random_points(n):
    np.random.seed(42)  
    points = np.random.rand(n, 2)
    return points

def halton_sequence(n, base):
    sequence = []
    for i in range(n):
        x = 0.0
        f = 1.0 / base
        index = i
        while index > 0:
            x += f * (index % base)
            index = index // base
            f = f / base
        sequence.append(x)
    return sequence

def generate_halton_points(n, base_x, base_y):
    x_sequence = halton_sequence(n, base_x)
    y_sequence = halton_sequence(n, base_y)
    points = np.column_stack((x_sequence, y_sequence))
    return points

num_points = 100

pseudo_random_points = generate_pseudo_random_points(num_points)
halton_points = generate_halton_points(num_points, 2, 3)

# Plotting the points side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].scatter(pseudo_random_points[:, 0], pseudo_random_points[:, 1])
axes[0].set_title('Pseudo-random Points')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

axes[1].scatter(halton_points[:, 0], halton_points[:, 1])
axes[1].set_title('Halton Points')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

plt.tight_layout()
plt.show()

