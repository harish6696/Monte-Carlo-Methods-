import numpy as np
import matplotlib.pyplot as plt

def exponential_pdf(x, lam):
    # Probability density function (PDF) of the exponential distribution
    return lam * np.exp(-lam * x)

def inverse_transform_sampling(lam, n_samples):
    # Generate samples from the exponential distribution using inverse transform sampling
    U = np.random.uniform(0, 1, n_samples)
    X = -np.log(1 - U) / lam
    return X

# Parameters
lambda_val = 0.5   # Lambda value for the exponential distribution
n_samples = 1000  # Number of samples to generate

# Generate samples using inverse transform sampling
samples = inverse_transform_sampling(lambda_val, n_samples)

# Plot histogram of generated samples
plt.hist(samples, bins=30, density=True, label='Sampled Distribution')

# Plot the probability density function (PDF)
x = np.linspace(0, 10, 1000)  # Range of x values for the PDF plot
pdf = exponential_pdf(x, lambda_val)
plt.plot(x, pdf, 'r', label='Target Distribution')

plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Inverse Transform Sampling from exponential distribution \n Target function : $\lambda e^{-\lambda x}$')
plt.legend()
plt.show()
