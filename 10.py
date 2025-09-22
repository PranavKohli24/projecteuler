def sum_primes(limit):
    # Initialize a boolean array for prime checking
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False

    # Sum all numbers that remain marked as prime
    return sum(i for i, prime in enumerate(is_prime) if prime)

# Sum of primes up to 2 million
limit = 2_000_000
prime_sum = sum_primes(limit)
print(f"Sum of primes up to {limit} is {prime_sum}")
