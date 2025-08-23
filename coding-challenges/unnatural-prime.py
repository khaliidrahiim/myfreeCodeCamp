# Given an integer, determine if that number is a prime number or a negative prime number.

def is_unnatural_prime(n):

    if n == 0 or n == 1 or n == -1:
        return False
    
    # If n is a negative number, convert it to its positive equivalent.
    # This is done because the concept of primality is typically defined for positive integers.
    # The function handles the "negative prime" aspect by first checking the primality of its absolute value.
    if n < 0:
        n = -n

    # This loop iterates through all possible integer divisors of n, starting from 2.
    # It uses a common optimization: you only need to check for divisors up to the square root of n.
    # If a number has a divisor larger than its square root, it must also have one smaller than it.
    # For example, for n=100, sqrt(100)=10. The divisors are (2,50), (4,25), (5,20), (10,10).
    # We only need to check up to 10 to find a factor.
    # The `+ 1` is included because Python's `range()` function is exclusive of the end value.
    for i in range(2, int(n**0.5) + 1):
        
        # The modulo operator (%) calculates the remainder of a division.
        # If `n % i` equals 0, it means `i` is a divisor of `n` without a remainder.
        # A prime number's only positive divisors are 1 and itself.
        # If we find any other divisor, we know `n` is not prime.
        if n % i == 0:
            
            # If a divisor is found, the number is not prime, so the function
            # immediately returns `False` and stops executing.
            return False

    return n