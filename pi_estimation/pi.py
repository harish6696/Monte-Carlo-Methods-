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
    
    # Plotting the points inside and outside the unit circle
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='blue', alpha=0.5, label='Outside Circle')
plt.scatter(x[distances <= 1], y[distances <= 1], color='red', alpha=0.5, label='Inside Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monte Carlo Estimation of π')
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
    
    return pi_estimate, x, y

n_samples = 10000
pi_estimate, x, y = estimate_pi(n_samples)



print(f"Estimated value of π: {pi_estimate}")

