import unittest
import functions

class TestSum(unittest.TestCase):
   
   
   def test_findLargestPalindromeFrom(self):
      self.assertEqual(functions.findLargestPalindromeFrom(99,99), 9009)
      #self.assertEqual(functions.findLargestPalindromeFrom(999,999), 9009)

   def test_isPalindrome(self):
      self.assertTrue(functions.isPalindrome(9009))
      self.assertTrue(functions.isPalindrome(5))
      self.assertTrue(functions.isPalindrome(11))
      self.assertTrue(functions.isPalindrome(111))
      self.assertFalse(functions.isPalindrome(9008))
      self.assertFalse(functions.isPalindrome(12))
      
   def test_smallestMultiple(self):
      #2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
      self.assertEqual(functions.smallestMultiple(range(1,10)), 2520)
      
   def test_canBeDividedWithoutRemainderbyEachIn(self):
      self.assertTrue(functions.canBeDividedWithoutRemainderbyEachIn(2520,range(1,10)))
      self.assertFalse(functions.canBeDividedWithoutRemainderbyEachIn(2519,range(1,10)))

   def testSumOfSquares(self):
      self.assertEqual(functions.sumOfSquares(range(1,11)), 385)
   
   def testSumOfSquaresEnhanced(self):
      self.assertEqual(functions.sumOfSquares(range(1,11)), 385)
      self.assertEqual(functions.sumOfSquares(range(1,101)), 338350)
      
   def testSumOfSquared(self):
      self.assertEqual(functions.sumOfSquared(range(1,11)), 3025)
   
   def testSumOfIntegers(self):
         self.assertEqual(functions.sumOfIntegers(range(1,1001)), 500500)
      
   def testLastPrimeNumberInSequenceEndingWith(self):
      self.assertEqual(functions.lastPrimeNumberInSequenceEndingWith(5),11)
      self.assertEqual(functions.lastPrimeNumberInSequenceEndingWith(6),13)
      self.assertEqual(functions.lastPrimeNumberInSequenceEndingWith(7),17)
      self.assertEqual(functions.lastPrimeNumberInSequenceEndingWith(8),19)
      
   def testflooredSquareRootOf(self):
      self.assertEqual(functions.flooredSquareRootOf(5),2)
      
   def testLastPrimeNumberInSequenceEndingWith(self):
      self.assertTrue(functions.isPrime(17))
      self.assertFalse(functions.isPrime(16))
      self.assertTrue(functions.isPrime(5915587277))
      self.assertTrue(functions.isPrime(2))
      self.assertTrue(functions.isPrime(3))
      self.assertTrue(functions.isPrime(5))
      self.assertTrue(functions.isPrime(7))
      self.assertFalse(functions.isPrime(1))
      self.assertFalse(functions.isPrime(4))
      
   def testProductOfDigitsIn(self):
      self.assertEqual(functions.productOfDigitsIn([1,2,3,4,5,6,7,8,9]), 362880)
      self.assertEqual(functions.productOfDigitsIn([9,9,8,9]), 5832)

   def testFindAdjacentDigits(self):  
      number = functions.sample1000digitNumber()
      self.assertEqual(functions.findAdjacentDigits(number,4),[9,9,8,9])

   def testConvertIntegerToList(self):
      self.assertEqual(functions.convertIntegerToList(1234),[1,2,3,4])
   
   def testConvertListToString(self):
      self.assertEqual(functions.convertListToString([1,2,3,4]), '1234')
      
   def testConvertStringToListOfIntegers(self):
      self.assertEqual(functions.convertStringToListOfIntegers('1234'), [1,2,3,4])
   
   def testSumOfPrimesBelow(self):
      #The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
      self.assertEqual(functions.sumOfPrimesBelow(10), 17)
      self.assertEqual(functions.sumOfPrimesBelow(2), 0)
      self.assertEqual(functions.sumOfPrimesBelow(3), 2)
      
   def testProductOfPythagoranTripletWhereSumIs(self):
      #A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
      self.assertEqual(functions.productOfPythagoranTripletWhereSumIs(12), 60)
      self.assertEqual(functions.productOfPythagoranTripletWhereSumIs(24), 480)
   
   def testcreatePythagoranTripletsWithSumUpTo(self):
      #A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
      self.assertEqual(functions.createPythagoranTripletsWithSumUpTo(12)[12], [3,4,5])
      self.assertEqual(functions.createPythagoranTripletsWithSumUpTo(30)[30], [5,12,13])
      self.assertEqual(functions.createPythagoranTripletsWithSumUpTo(24)[24], [8,6,10])
      
   def testTwoDimensionalArrayFromString(self):
      aString = '1 2 3\n4 5 6\n7 8 9'
      self.assertEqual(functions.twoDimensionalArrayFromString(aString), [[1,2,3],[4,5,6],[7,8,9]])
      
   def testGreatestProductOf4AdjacentNumbersIn(self):
      aString = '1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7'
      anArray = functions.twoDimensionalArrayFromString(aString)
      #self.assertEqual(functions.greatestProductOf4AdjacentNumbersIn(anArray),3024)

   def testGreatestProductOf4AdjacentHorizontalNumbersIn(self):
      aString = '1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7'
      anArray = functions.twoDimensionalArrayFromString(aString)
      #self.assertEqual(functions.greatestProductOf4AdjacentHorizontalNumbersIn(anArray),3024)
                       
   def testGreatestProductOf4AdjacentVerticalNumbersIn(self):
      aString = '1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7'
      anArray = functions.twoDimensionalArrayFromString(aString)
      #self.assertEqual(functions.greatestProductOf4AdjacentVerticalNumbersIn(anArray),1440)
                          
   def testGreatestProductOf4AdjacentDiagonalNumbersIn(self):
      aString = '1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7'
      anArray = functions.twoDimensionalArrayFromString(aString)
      #self.assertEqual(functions.greatestProductOf4AdjacentDiagonalNumbersIn(anArray),1440)
      
   def testHorizontalArraysIn(self):
      aString = '1 2\n 3 4'
      anArray = functions.twoDimensionalArrayFromString(aString)
      self.assertEqual(functions.horizontalArraysIn(anArray),[[1,2],[3,4]]) 
      
   def testVerticalArraysIn(self):
      aString = '1 2\n 3 4'
      anArray = functions.twoDimensionalArrayFromString(aString)
      self.assertEqual(functions.verticalArraysIn(anArray),[[1,3],[2,4]])
      
   def testDiagonalArraysIn(self):
      aString = '1 2\n 3 4'
      anArray = functions.twoDimensionalArrayFromString(aString)
      self.assertEqual(functions.diagonalArraysIn(anArray),[[1,4],[3,2]])
      
   def testAllXandYCoordinatesIn(self):
      aString = '1 2\n 3 4'
      anArray = functions.twoDimensionalArrayFromString(aString)
      self.assertEqual(functions.allXandYCoordinatesIn(anArray),[[1,1],[1,2],[2,1],[2,2]])
      
if __name__ == '__main__':   
   unittest.main()