
import matplotlib.pyplot as plt
import numpy as np

NUM_SAMPLES = 10000
MEAN = 0
STANDARD_DEVIATION = 1
MIN_X = -4
MAX_X = 4
def uniform_distr(low: float, high: float):
    return 1 / (high - low)
def normal_dist(x: np.ndarray, mean: float, standard_deviation: float):
    return (1/ (standard_deviation * np.sqrt(2 * np.pi))* np.exp(-0.5 * ((x - mean) / standard_deviation) ** 2))
x = np.linspace(MIN_X, MAX_X, NUM_SAMPLES)
y_true = normal_dist(x, MEAN, STANDARD_DEVIATION)

def rejection_sampling(num_samples: int, min_x: float, max_x: float):
    x = np.random.uniform(min_x, max_x, num_samples)
    k = 4.5
    u = np.random.uniform(np.zeros_like(x), uniform_distr(min_x, max_x) * k)
    (idx,) = np.where(u < normal_dist(x, MEAN, STANDARD_DEVIATION))
    return x[idx], len(idx) / num_samples

y_sampled, acceptance_prob = rejection_sampling(NUM_SAMPLES * 10, MIN_X, MAX_X)
print(f"Acceptance probability: {acceptance_prob}")
function_str = r'$\frac{1}{\sqrt{2 \pi}} \exp\left(-\frac{1}{2} \left(x\right)^2\right)$'
plt.plot(x, y_true, "r-",label='Target distribution')
plt.hist(y_sampled, bins=30, density=True , label='Sampled Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Rejection Sampling \n Target function: '+function_str)
plt.legend()
plt.show()
