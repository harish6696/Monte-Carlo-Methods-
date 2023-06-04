import numpy as np
import matplotlib.pyplot as plt

def regular_monte_carlo_integration(f, a, b, num_samples):
    # Generate random samples within the integration range
    x = np.random.uniform(a, b, num_samples)
    # Calculate the function values at the sampled points
    f_values = f(x)
    # Estimate the integral using the mean of the function values
    integral = np.mean(f_values) * (b - a)
    return integral

def importance_sampling_integration(f, g, a, b, num_samples):
    # Generate random samples from the importance distribution
    x = np.random.uniform(a, b, num_samples)
    # Calculate the weights based on the ratio of the target PDF to the importance PDF
    weights = f(x) / g(x)
    # Estimate the integral using the weighted mean of the function values
    integral = np.mean(f(x) / weights) * (b - a)
    return integral

def target_distribution(x):
    # target distribution function
    return np.sin(x)

def importance_distribution(x):
    # importance distribution function
    return np.cos(x)

# Integration range
a = 0
b = np.pi


num_iterations = 100

num_samples = 1000

# Initialize lists to store the integration results
regular_monte_carlo_integrals = []
importance_sampling_integrals = []

# Perform the integration over multiple iterations
for i in range(num_iterations):
    # Regular Monte Carlo integration
    mc_integral = regular_monte_carlo_integration(target_distribution, a, b, num_samples)
    regular_monte_carlo_integrals.append(mc_integral)
    
    # Importance sampling integration
    is_integral = importance_sampling_integration(target_distribution, importance_distribution, a, b, num_samples)
    importance_sampling_integrals.append(is_integral)

# Plotting the results
iterations = range(1, num_iterations + 1)

plt.plot(iterations, regular_monte_carlo_integrals, label='Regular Monte Carlo')
plt.plot(iterations, importance_sampling_integrals, label='Importance Sampling')
plt.xlabel('Iterations')
plt.ylabel('Integration Result')
plt.legend()
plt.show()

