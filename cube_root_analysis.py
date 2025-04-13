import time
import matplotlib.pyplot as plt
import math

# Efficient cube root using binary search
def cube_root(n):
    # Keep track of steps
    steps = 0

    # Handle negative numbers by working with absolute and adjusting sign later
    is_negative = n < 0
    n_abs = abs(n)

    # Binary search boundaries
    low, high = 0, n_abs
    
    # Edge cases for 0 and 1
    if n_abs == 0 or n_abs == 1:
        return -n_abs if is_negative else n_abs, steps

    # Perform binary search
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_cubed = mid * mid * mid

        if mid_cubed == n_abs:
            return -mid if is_negative else mid, steps
        elif mid_cubed < n_abs:
            low = mid + 1
        else:
            high = mid - 1

    # If not a perfect cube, return closest integer cube root (floor)
    return -high if is_negative else high, steps

# Benchmark and plot step counts vs number of digits
def analyze_steps(max_digits=10):
    digit_lengths = []
    step_counts = []
    estimated_c_steps = []

    for d in range(1, max_digits + 1):
        # Test the max number with d digits
        number = 10**d - 1
        _, steps = cube_root(number)
        
        digit_lengths.append(d)
        step_counts.append(steps)

        # Estimate C steps (approx 50x faster than Python, depending on environment)
        estimated_c_steps.append(steps // 50)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(digit_lengths, step_counts, label='Python Steps', marker='o')
    plt.plot(digit_lengths, estimated_c_steps, label='Estimated C Steps (1/50th)', marker='x')
    plt.xlabel('Number of Digits in Input Integer')
    plt.ylabel('Steps Taken (Binary Search Iterations)')
    plt.title('Steps to Compute Cube Root vs Input Size')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    num = -74088  # example input
    root, steps = cube_root(num)
    print(f"Cube root of {num} is {root}, found in {steps} steps.")

    # Analyze and plot
    analyze_steps(max_digits=12)
