"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-------------------------

"""

# let's first create a function that checks for a given integer if it's a palindrome or not
def is_palindrome(number=int):
    """
    In this function we build the given number backwards by 
    taking the last number from left to right and putting it 
    at the beggining and so on then compare the given number
    with the obtained result and tell if it's a palindrome or
    not.
    """
    # at the beggining the reverse variable is empty
    reverse = 0
    # we keep a copy of the given number because it's initial
    # value will be altered during the while loop
    original_number = number

    # iteration process
    while number > 0:
        reverse = (reverse * 10 + number % 10) # we multiply the previous reverse value
        # by 10 too keep the previous digit then we add the most right placed digit of the
        # orginal number
        # It's a bit abstract as you see it here but by playing around with the Python
        # interpreter you will understand better the trick ;)
        number=number//10  # here we truncate the last digit from the number 
    
    if reverse == original_number:  # final statement
        return True

# now we'll use two variables to multiply each 3 digits number by every other 3 digits numbers
# and get the product of each operation and test if it's a palindrome or not by using our 
# function, if yes we put it in a list containing evey palindrome found.

palindromes = []

for first_factor in range(100,1000):

    for second_factor in range(1,1000):

        if is_palindrome(first_factor * second_factor):  # we test if each product is a palindrome
            palindromes.append(first_factor * second_factor) # if so we append it to our list

largest_palindrome = 0  # at first our biggest palindrome is 0, value will increase later

# in this simple for loop we compare each palindrome to get the largest one 
for palindrome in palindromes:
    if palindrome > largest_palindrome:
        largest_palindrome = palindrome

# output the answer
print(largest_palindrome)
