#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc. 31875000

import functions
from timeit import default_timer

start = default_timer()

result = functions.productOfPythagoranTripletWhereSumIs(1000)

end = default_timer()
time = end - start
print('Result: ' + str(result))
print('\n time to calcualte result:' + str(time) + ' seconds')