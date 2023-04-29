#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import functions

result=0
    
#sum of all multiples of 3 below 1000.
result = result + functions.findSumEnhanced(1000,3)
print(result)
#sum of all multiples of 5 below 1000.
result = result + functions.findSumEnhanced(1000,5)
print(result)
#multiples of 3 and 5 are double counted so need to remove them
result = result - functions.findSumEnhanced(1000,15)

print(result)