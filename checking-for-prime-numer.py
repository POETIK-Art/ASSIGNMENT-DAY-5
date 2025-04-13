import matplotlib.pyplot as plt

# Efficient primality test using trial division up to sqrt(n)
def is_prime(n):
    steps = 0
    if n <= 1:
        return False, steps
    if n <= 3:
        return True, steps + 1
    if n % 2 == 0 or n % 3 == 0:
        return False, steps + 1

    i = 5
    while i * i <= n:
        steps += 1
        if n % i == 0 or n % (i + 2) == 0:
            return False, steps
        i += 6

    return True, steps

# Sum all primes in a range and collect step data for plotting
def analyze_primes(start=3, end=1000):
    prime_sum = 0
    digit_lengths = []
    step_counts = []
    estimated_c_steps = []

    for n in range(start, end + 1):
        prime, steps = is_prime(n)
        if prime:
            prime_sum += n

        digit_len = len(str(n))
        digit_lengths.append(digit_len)
        step_counts.append(steps)
        estimated_c_steps.append(max(1, steps // 50))

    # Plot steps per number of digits
    plt.figure(figsize=(10, 6))
    plt.plot(range(start, end + 1), step_counts, label='Python Steps', color='blue')
    plt.plot(range(start, end + 1), estimated_c_steps, label='Estimated C Steps (1/50th)', color='red', linestyle='--')
    plt.xlabel('Number Tested')
    plt.ylabel('Steps Taken (Primality Test)')
    plt.title(f'Steps to Test Primality Between {start} and {end}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return prime_sum

# Example usage
if __name__ == "__main__":
    prime_total = analyze_primes(3, 1000)
    print(f"Sum of all prime numbers between 3 and 1000 is {prime_total}.")
