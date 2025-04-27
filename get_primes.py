"""
from math import floor , sqrt
def is_prime(num):
    if num < 2:
        return False
    for x in range(2,floor(sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True
num_list = range(1,1000)
primes = filter(is_prime,num_list)
print(list(primes))
"""