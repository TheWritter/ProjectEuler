"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
---------------------------
For this problem, we'll establish the prime factor decomposition for the 
requested integer then check which prime factor is the largest and output it
"""
# the target integer is put in a variable for more readability
integer = 600851475143
# list that will contain all prime factors to compare them and get the answer
prime_factors = []
prime_divisor = 2

while integer > 1:
    # we start by testing the first prime number
    # and we establish all factors that can be 
    # written on the form 2k, k being a positive integer

    while integer % prime_divisor == 0:
        prime_factors.append(prime_divisor)
        integer = integer / prime_divisor
    
    prime_divisor += 1 # we'll test every positive number with this method but we'll
    # only retrieve prime factors

print(max(prime_factors))
