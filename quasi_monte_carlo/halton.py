import numpy as np
import matplotlib.pyplot as plt

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


# Example usage
num_points = 100
base_x = 2
base_y = 3

points = generate_halton_points(num_points, base_x, base_y)

# Plotting the points
plt.scatter(points[:, 0], points[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Halton Points')
plt.show()
