
"""
What does the code do?
- takes the input from function do_stuff and then 
converts the second argument into an integer then 
if it is less than 2 (2 is the number of characters)
we print 'No' otherwise we run through the for loop 
from 2 to 1-number and if number%i equals 0 we print 
we print no otherwise we return yes 

Basically we're checking if the divisors of something with
length number are other than 0, 1, and 2.
"""

""" The error is mismatched quotations for the final print 
statement that prints ('Yes') fixed that by changing the quotations 
so that they match"""

import sys
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print("Yes")
# Test the function
do_stuff()


