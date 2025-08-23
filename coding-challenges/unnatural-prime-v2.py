# Given an integer, determine if that number is a prime number or a negative prime number.

def is_unnatural_prime(n):
    """
    Checks if an integer is a prime or a negative prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself. This function extends the concept
    to negative integers (e.g., -2, -3, -5 are considered "negative primes").

    Args:
        n: The integer to check.

    Returns:
        True if n is a prime or a negative prime, False otherwise.
    """
    # Prime numbers must be greater than 1 (or less than -1).
    # 0, 1, and -1 are not prime by definition.
    if n == 0 or n == 1 or n == -1:
        return False

    # We check the primality of the absolute value of n.
    # Using abs() is a more concise way to handle negative inputs.
    positive_n = abs(n)

    # Iterate from 2 up to the square root of the number to find any divisors.
    for i in range(2, int(positive_n**0.5) + 1):
        # If we find a number that divides positive_n evenly, it's not prime.
        if positive_n % i == 0:
            return False

    # If the loop completes without finding any divisors, the number is prime.
    return True

