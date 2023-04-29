#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Prime factor is a factor that is a prime number.
#In other words: any of the prime numbers that can be multiplied to give the original number.
#Example: The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).
#We showed you how to do the factorization by starting at the smallest prime and working upwards.

import functions
from timeit import default_timer

print('basic solution:')
start = default_timer()
result = functions.primeFactorsOf(600851475143)[-1]
end = default_timer()
time = end - start
print('result:' + str(result))
print(' time to calcualte result:' + str(time) + ' seconds')

print('solution handling 2 as special case:')
start = default_timer()
result = functions.primeFactorsOfEnhancedToHandle2(600851475143)[-1]
end = default_timer()
time = end - start
print('result:' + str(result))
print(' time to calcualte result:' + str(time) + ' seconds')

print('solution using square root and 2 as special case:')
start = default_timer()
result = functions.primeFactorsOfEnhancedToUseSqaureRoot(600851475143)[-1]
end = default_timer()
time = end - start
print('result:' + str(result))
print(' time to calcualte result:' + str(time) + ' seconds')