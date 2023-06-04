import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Determine the normalizing constant (nc), remember our target function should be a probability distribution.
# So we divide the target function by the nc to obtain a PDF whose area upon integration yields 1
def nc(x):
    return np.exp(-0.2 * x ** 2) + np.exp(-0.2 * (x - 10) ** 2)

x_range = np.linspace(-100, 100, 1000)
nc_values = nc(x_range)
nc_value = simps(nc_values, x_range)


def target_distribution(x):
    """Target distribution that we want to sample from"""
    return (np.exp(-0.2 * x ** 2) + np.exp(-0.2 * (x - 10) ** 2)) /nc_value

def proposal_distribution(x):
    """Simple proposal distribution centered at x"""
    return np.random.normal(x, 4)

def metropolis_hastings_sampling(num_samples):
    samples = []
    x = 4  # Initial state of the Markov chain

    for _ in range(num_samples):
        # Generate a proposal sample
        x_proposed = proposal_distribution(x)

        # Calculate the acceptance ratio
        acceptance_ratio = min((target_distribution(x_proposed) / target_distribution(x)), 1)

        # Accept or reject the proposal sample
        if np.random.random() < acceptance_ratio:
            x = x_proposed

        samples.append(x)

    return samples

# Number of samples to generate
num_samples = 1000000

# Generate samples using the Metropolis-Hastings algorithm
samples = metropolis_hastings_sampling(num_samples)

# Define the x range for plotting
x_range = np.linspace(-10, 20, 100)

# Calculate the target distribution values for the x range
target_values = target_distribution(x_range)

# Plotting the samples
plt.hist(samples[1000:], bins=60, density=True, label='Sampled Distribution')
plt.plot(x_range, target_values, 'r', label='Target Distribution')
plt.legend()
plt.xlabel('x')
plt.ylabel('Probability Density')
function_str=r'$e^{-0.2x^2} + e^{-0.2(x-10)^2}$'
plt.title('Metropolis-Hastings Sampling \n  Target Distribution: '+function_str)
plt.show()

