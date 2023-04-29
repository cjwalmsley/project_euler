import functions
    
def test_findSum():
    assert functions.findSum(10,3,5) == 23

def test_findSum2():
    assert functions.findSum(1000,3,5) == 233168
    
def test_findSumEnhanced():
    #the sum of all multiples of 3 between 1 and 1000 is 166833
    assert functions.findSumEnhanced(1000,3) == 166833
    
def test_findSumEnhanced2():
     assert functions.findSumEnhanced(10,3) == 18
        
def test_sumEvenFibonacciTerms():
     assert functions.sumEvenFibonacciTerms(1, 2, 4000000) == 4613732
        
def test_sumEvenFibonacciTerms2():
     assert functions.sumEvenFibonacciTerms(1, 2, 40) == 44
      
def test_sumEvenFibonacciTermsNoTesting():
     assert functions.sumEvenFibonacciTermsNoTesting(4000000) == 4613732
      
def test_sumEvenFibonacciTermsNoTesting2():
     assert functions.sumEvenFibonacciTermsNoTesting(40) == 44
      
def test_sumEvenFibonacciTermsUsingGoldenRule():
     assert functions.sumEvenFibonacciTermsUsingGoldenRule(40) == 44

def test_sumEvenFibonacciTermsUsingGoldenRule2():
     assert functions.sumEvenFibonacciTermsUsingGoldenRule(4000000) == 4613732
      
def test_calculateFibonacciTerm():
     assert functions.calculateFibonacciTerm(3) == 2
     assert functions.calculateFibonacciTerm(6) == 8
     assert functions.calculateFibonacciTerm(9) == 34
     assert functions.calculateFibonacciTerm(7) == 13
   
def test_deriveGoldenRatio():
     assert round(functions.deriveGoldenRatio(),8)  == 1.61803399
     assert functions.deriveGoldenRatio()  ==1.618033988749895
   
def test_deriveGoldenRatioUsingSin54():
     assert round(functions.deriveGoldenRatioUsingSin54(),8)  == 1.61803399
     assert functions.deriveGoldenRatioUsingSin54()  ==1.618033988749895
      
def test_primeFactorsOf():
#The prime factors of 13195 are 5, 7, 13 and 29.
   result = functions.primeFactorsOf(13195)
   assert result == [5,7,13,29]
   result = functions.primeFactorsOf(60)
   assert result == [2,3,5]
   
def test_primeFactorsOfEnhancedToHandle2():
   result = functions.primeFactorsOfEnhancedToHandle2(13195)
   assert result == [5,7,13,29]
   result = functions.primeFactorsOfEnhancedToHandle2(60)
   assert result == [2,3,5]

def test_primeFactorsOfEnhancedToUseSqaureRoot():
   result = functions.primeFactorsOfEnhancedToUseSqaureRoot(13195)
   assert result == [5,7,13,29]
   result = functions.primeFactorsOfEnhancedToUseSqaureRoot(60)
   assert result == [2,3,5]   
   
def test_factorsOf():
   result = functions.factorsOf(30)
   assert result == [2,3,5,6,10,15]

def test_isWholeNumber():
   assert functions.isWholeNumber(3)
   assert functions.isWholeNumber(2.2) == False
   
def test_isFactorOf():
   assert functions.isFactorOf(3,30)
   assert functions.isFactorOf(4,30) == False
   
def test_isPrimeFactor():
   assert functions.isPrimeFactor(5)
   assert functions.isPrimeFactor(6) == False
   assert functions.isPrimeFactor(53)
   assert functions.isPrimeFactor(57) == False
   assert functions.isPrimeFactor(2)
   
def test_sumPrimeFactorsOf():
   assert functions.sumPrimeFactorsOf(13195) == 54
   
def test_lastPrimeFactorOf():
   assert functions.lastPrimeFactorOf(600851475143) == 6857
      
if __name__ == "__main__":
    test_findSum()
    test_findSum2()
    test_findSumEnhanced()
    test_findSumEnhanced2()
    test_sumEvenFibonacciTerms()
    test_sumEvenFibonacciTerms2()
    test_sumEvenFibonacciTermsNoTesting()
    test_sumEvenFibonacciTermsNoTesting2()
    test_sumEvenFibonacciTermsUsingGoldenRule()
    test_sumEvenFibonacciTermsUsingGoldenRule2()
    test_calculateFibonacciTerm()
    test_deriveGoldenRatio()
    test_deriveGoldenRatioUsingSin54()
    test_isWholeNumber()
    test_isFactorOf()
    test_isPrimeFactor()
    test_factorsOf()
    test_primeFactorsOf()
    test_sumPrimeFactorsOf()
    test_lastPrimeFactorOf()
    test_primeFactorsOfEnhancedToHandle2()
    test_primeFactorsOfEnhancedToUseSqaureRoot()
      
    print("Everything passed")