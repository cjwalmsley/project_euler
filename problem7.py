#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?  104743
#time to calcualte result:569.919406979 seconds

import functions
from timeit import default_timer

start = default_timer()
result = functions.lastPrimeNumberInSequenceEndingWith(10001)
end = default_timer()
time = end - start
print('result: ' + str(result))
print('\n time to calcualte result:' + str(time) + ' seconds')