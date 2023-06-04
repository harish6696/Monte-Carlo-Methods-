import numpy as np
import matplotlib.pyplot as plt

def target_distribution(x):
    """Target distribution defined as a Gaussian"""
    mean = 2  # Mean of the Gaussian
    std = 2  # Standard deviation of the Gaussian
    return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))

def proposal_distribution(x, step_size):
    """Simple proposal distribution centered at x"""
    return np.random.normal(x, step_size)

def metropolis_hastings_sampling(num_samples, step_size):
    samples = []
    x = 0  # Initial state of the Markov chain

    for _ in range(num_samples):
        # Generate a proposal sample
        x_proposed = proposal_distribution(x, step_size)

        # Calculate the acceptance ratio
        acceptance_ratio = (
            target_distribution(x_proposed) / target_distribution(x)
        )

        # Accept or reject the proposal sample
        if np.random.uniform(0, 1) < acceptance_ratio:
            x = x_proposed

        samples.append(x)

    return samples

# Number of samples to generate
num_samples = 10000

# Step size for the proposal distribution
step_size = 1.0

# Generate samples using the Metropolis-Hastings algorithm
samples = metropolis_hastings_sampling(num_samples, step_size)

# Plotting the samples
plt.hist(samples, bins=50, density=True, label='Sampled Distribution')
x_range = np.linspace(-5, 10, 1000)
plt.plot(x_range, target_distribution(x_range), 'r', label='Target Distribution')
plt.legend()
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Metropolis-Hastings Sampling for a Gaussian')
plt.show()
