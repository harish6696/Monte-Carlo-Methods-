import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n_samples):
    points_inside_circle = 0
    points_total = n_samples

    # Generate random points within the square [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)

    # Calculate the distance of each point from the origin
    distances = np.sqrt(x**2 + y**2)

    # Count the points inside the unit circle
    points_inside_circle = np.sum(distances <= 1)

    # Estimate pi using the ratio of points inside the circle to the total points
    pi_estimate = 4 * (points_inside_circle / points_total)
    
    return pi_estimate, x, y, distances

n_samples_1 = 10000
n_samples_2 = 50000

pi_estimate_1, x_1, y_1, distances_1 = estimate_pi(n_samples_1)
pi_estimate_2, x_2, y_2, distances_2 = estimate_pi(n_samples_2)

# Generate points on the unit circle
theta = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

# Plotting the points inside and outside the unit circle, and the circle equation
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot for n_samples_1
axs[0].scatter(x_1, y_1, color='blue', alpha=0.5, label='Outside Circle')
axs[0].scatter(x_1[distances_1 <= 1], y_1[distances_1 <= 1], color='red', alpha=0.5, label='Inside Circle')
axs[0].plot(circle_x, circle_y, color='black', label='Circle (Analytic)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title(f'Estimated π = {pi_estimate_1:.4f}\n(n_samples = {n_samples_1})')
axs[0].legend()
axs[0].set_aspect('equal')

# Plot for n_samples_2
axs[1].scatter(x_2, y_2, color='blue', alpha=0.5, label='Outside Circle')
axs[1].scatter(x_2[distances_2 <= 1], y_2[distances_2 <= 1], color='red', alpha=0.5, label='Inside Circle')
axs[1].plot(circle_x, circle_y, color='black', label='Circle (Analytic)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_title(f'Estimated π = {pi_estimate_2:.4f}\n(n_samples = {n_samples_2})')
axs[1].legend()
axs[1].set_aspect('equal')

plt.tight_layout()
plt.show()

print(f"Estimated value of π (n_samples = {n_samples_1}): {pi_estimate_1}")
print(f"Estimated value of π (n_samples = {n_samples_2}): {pi_estimate_2}")
