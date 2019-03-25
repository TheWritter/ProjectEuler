"""
Multiples of 3 and 5 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
-----------------------------------
In this problem we'll simply use a for loop by testing all numbers between
1 and 1000 and if the rest of their division by 3 OR 5 is 0 we add them
to the list
"""
total_sum = 0

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

print(total_sum)
