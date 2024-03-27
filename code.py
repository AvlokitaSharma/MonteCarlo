import numpy as np

def estimate_pi(num_samples):
    # Generate random points
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)
    
    # Check if points are inside the quarter circle
    inside_circle = x**2 + y**2 <= 1
    
    # Estimate pi
    pi_estimate = 4 * np.sum(inside_circle) / num_samples
    return pi_estimate

# Example: Estimate π using 1,000,000 samples
num_samples = 1000000
pi_estimate = estimate_pi(num_samples)
print(f"Estimated π: {pi_estimate}")
