#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#nth even number = 4*(n-1)th + (n-2)th. 

import functions
import timeit

total =0
time =0

time = timeit.timeit(total = functions.sumEvenFibonacciTermsUsingGoldenRule(4000000))
  
print(total)
print("time to exectute: " + str(time))