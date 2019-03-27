"""
Sum Square Difference
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-----------------------
This problem is quite simple, we just have to calculate the sum of the squares and the square of the sul
then find the difference
"""

squares_sum = 0
square_of_the_sum = 0

for number in range(1,101):
    squares_sum += number**2
    square_of_the_sum += number

square_of_the_sum = square_of_the_sum**2

difference = square_of_the_sum - squares_sum
print(difference)
