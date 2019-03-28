"""
10001 st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

In this problem we'll create a function that determine if an integer is prime or not,
if yes we add it to a dict object and use index number to find out the 10001 key and
print it out.

That's it :)
"""
import math

primes_list = []  # the list that will contain the first 10001 prime numbers
num = 2  # we start at 2 

def prime_tester(number):
    
    # at first we assume the number is prime
    number_is_prime = True
    # we run a for loop starting from 2 to the integer part of the square root of the given number
    # because a number that is not prime always has a factor different of 1 that is lower than his
    # square root integer part.
    for divisor in range(2, int(math.sqrt(number))+1):
        
        if number % divisor == 0:  # if we found a possible divisor 
            number_is_prime = False  # the number is not anymore prime

    return number_is_prime  # we finally return the state of the number


while len(primes_list) < 10002:  # we use a while loop so we test numbers until we get 10 001 primes

    if prime_tester(num):  # if the tested number is prime
        primes_list.append(num)
    num += 1  # we increase the num variable to test all positive integers until we reach the 10001st index place

print(primes_list[10001])  # print out the answer 
