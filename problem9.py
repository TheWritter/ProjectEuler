"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import itertools

# we create a list containing all positive integers up to a limit
# empty at the start
numbers_list = []
# same thing with a list containing all tuples of Pythagorean triplets
pythagorean_triplets_list = []

# here we will work with a and b < 998 before a + b + c = 1000

# in a first moment we will identify all Pythagorean triplets
# using the above function
def pythagorean_triplets_identificator(triplets_list, limit):
    """ 
    The variable list is used to append all triplets
    found together and finally return it
    """
    for number in range(1,limit):  # we first create a list of all natural integers below our fixed limit
        numbers_list.append(number)

    for couple in itertools.combinations(numbers_list, 2):  # use itertools function to find all couples
        # of two values below the limit
            if math.sqrt(couple[0]**2 + couple[1]**2).is_integer():  # we test if the square root we got is an integer
                triplets_list.append([couple[0], couple[1], int(math.sqrt(couple[0]**2 + couple[1]**2))]) 
                # if so we append our triplet to the list 
    return triplets_list  # we finally return the complete list

# NOTE: The following part can be WAY more efficient by harvesting the triplets to test that may suit
# our needs, for example we will not test triplets containing a value larger than 1000 so we use less memory
# and spend less time

for triplet in pythagorean_triplets_identificator(pythagorean_triplets_list, 997):
    if sum(triplet) == 1000:  # we calculate the sum and test
        print(triplet[0]*triplet[1]*triplet[2])  # we print out what we need
        break  # once we found what we're looking for we can exit
