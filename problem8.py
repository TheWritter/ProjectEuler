"""
Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
----------------------------
In this problem we consider a given 1 thousand digits number. IF we want to find the largest product
of 13 adjacent digits we need to test each combination of digits in this large number and only keep 
the largest obtained product
"""

large_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def product_calculator(number, row):
    """
    This function takes a number and a row in input
    and will calculate the product of all combination possible
    with X (row) adjacent digits and only return the largest. 
    :param number: is the number we want to analyze
    :row: is an integer that symbolize the number of digits we want to use
    """
    # our counter will have two extremum 
    min_range = 0
    max_range = row 
    # at start we calculate the range [0,13]
    # containing the first 13 adjacent digits
    # and each new product we'll increase the value 
    # of our extremum by 1 until max_range reaches
    # the 1000 value which of course does not exist
    product = 1 
    # at start product is equal to 1
    products_list = []
    # we also need a products list to put every product in it
    # and return the largest one using the max function (we're working with integers)
    number_list = [int(digit) for digit in str(number)]
    # here we turn our large number into a list to manipulate it 
    while max_range <= len(number_list):
        
        for digit in number_list[min_range:max_range]:
            product *= int(digit)  # we convert our digit into an integer cause we have it
            # under the form of a string

        products_list.append(product)
        min_range += 1
        max_range += 1
        product    = 1
        
    return max(products_list)

print(product_calculator(large_number, 13))
