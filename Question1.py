# Question 1

def simpleDiv(dividend, divisor):

    count = 0 

    while dividend >= divisor:
        dividend -= divisor
        count = count + 1

    return count