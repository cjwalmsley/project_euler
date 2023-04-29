#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million. (142,913,828,922)

import functions
from timeit import default_timer

start = default_timer()

result = functions.sumOfPrimesBelow(2000000)

end = default_timer()
time = end - start
print('Result: ' + str(result))
print('\n time to calcualte result:' + str(time) + ' seconds')