def printString(aString):
	print(aString)

def helloWorld():
	print("Hello World")
    
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of upper multiplier1 or multiplier2 below an upperNumber.

def findSum(upperNumber, multiplier1, multiplier2):

    number = 1
    total = 0

    while number < upperNumber:
        if number % multiplier1 == 0 or number % multiplier2 == 0:
            total = total + number
        number = number +1
    return total

#More efficient solution usig arithmetic sequence formula
#n(a+an)/2
#n = number of terms
#a = first term
#an = nth term
#https://en.wikipedia.org/wiki/Arithmetic_progression

def findSumEnhanced(upperNumber, multiplier):

    an = upperNumber-1
    n = an // multiplier
    sn = n*(multiplier+an)/2
    return sn

def isEvenNumber(aNumber):
    return aNumber % 2 ==0

def sumEvenFibonacciTerms(firstTerm, secondTerm, upperLimit):

    nextTerm = 0
    total = 0

    while nextTerm <= upperLimit:
        if isEvenNumber(secondTerm):
            total = total + secondTerm    
        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
    
    return total
   
#every 3rd term is even so only the 3rd term needs to be added.
#n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
#xn =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377

def sumEvenFibonacciTermsNoTesting(upperLimit):
   firstTerm = 1
   secondTerm = 1
   thirdTerm = firstTerm + secondTerm
   total = 0
   while thirdTerm <= upperLimit:
      total = total + thirdTerm
      firstTerm = secondTerm + thirdTerm
      secondTerm = firstTerm + thirdTerm
      thirdTerm = firstTerm + secondTerm
   return total

#using the golden ratio, the nth term - xn is expressed as: xn = (φn − (1−φ)^n)/√5
#https://www.mathsisfun.com/numbers/fibonacci-sequence.html

def sumEvenFibonacciTermsUsingGoldenRule(upperLimit):
   
   total = 0
   thirdTerm = 0
   termCount = 0

   while thirdTerm <= upperLimit:
      total = total + thirdTerm
      thirdTermCount = 0
      for each in range(3):
         thirdTermCount = thirdTermCount + 1
         termCount = termCount + 1
         if thirdTermCount == 3:
            thirdTerm = calculateFibonacciTerm(termCount)
            thirdTermCount = 0
   return total

def calculateFibonacciTerm(termCount):
   import math
   goldenRatio = deriveGoldenRatioUsingSin54()
   result = (goldenRatio**termCount - (1 - goldenRatio)**termCount) / math.sqrt(5)
   return int(result)

#φ = 1/2 + √5/2
#https://www.mathsisfun.com/numbers/golden-ratio.html

def deriveGoldenRatio():
   import math
   return 1/2 + math.sqrt(5)/2

#the Golden Ratio is also equal to 2 × sin(54°)

def deriveGoldenRatioUsingSin54():
   import math
   sin54 = math.sin(math.radians(54))
   return 2*sin54

def factorsOf(aNumber):
   result = []
   count = 2
   while count <= aNumber / 2:
      if isFactorOf(count,aNumber):
         result.append(count)
      count = count + 1  
   return result

def isWholeNumber(aNumber):
   return aNumber % 1 == 0

def isFactorOf(aFactor,aNumber):
   return aNumber % aFactor == 0

def isPrimeFactorOf(aFactor,aNumber):
   return isPrimeFactor(aFactor) and isFactorOf(aFactor,aNumber) == 0

def isPrimeFactor(aFactor):
   if aFactor == 1:
      return False
   if aFactor == 2:
      return True
   if aFactor % 2 != 0:
      return len(factorsOf(aFactor)) == 0
   return False

def lastPrimeFactorOf(aNumber):
   return primeFactorsOf(aNumber)[-1]

def primeFactorsOf(aNumber):
   factor=2
   lastFactor=1
   workingNumber = aNumber
   result = []
   while workingNumber > 1:
      if workingNumber % factor == 0:
         lastFactor = factor
         result.append(lastFactor)
         workingNumber = workingNumber // factor
         while workingNumber % factor == 0:        
            workingNumber = (workingNumber // factor)
      factor = factor+1
   return result

def primeFactorsOfEnhancedToHandle2(aNumber):

   factor = 3
   result = []
   workingNumber = aNumber

   if workingNumber % 2 == 0:
      workingNumber = workingNumber / 2
      lastFactor = 2
      result.append(lastFactor)
      while workingNumber % 2 == 0:
         workingNumber = workingNumber // 2   
   else:
      lastFactor = 1   

   while workingNumber > 1:
      if workingNumber % factor == 0:
         lastFactor = factor
         result.append(lastFactor)
         workingNumber = workingNumber // factor
         while workingNumber % factor == 0:
            print ('workingNumber: ' + str(workingNumber) + 'factor: ' + str(factor))
            workingNumber = (workingNumber // factor)
      factor = factor+2
   return result

def primeFactorsOfEnhancedToUseSqaureRoot(aNumber):
   import math
   factor = 3
   result = []
   workingNumber = aNumber

   if workingNumber % 2 == 0:
      workingNumber = workingNumber / 2
      lastFactor = 2
      result.append(lastFactor)
      while workingNumber % 2 == 0:
         workingNumber = workingNumber // 2   
   else:
      lastFactor = 1   

   while workingNumber > 1 and lastFactor < math.sqrt(aNumber):
      if workingNumber % factor == 0:
         lastFactor = factor
         result.append(lastFactor)
         workingNumber = workingNumber // factor
         while workingNumber % factor == 0:
            print ('workingNumber: ' + str(workingNumber) + 'factor: ' + str(factor))
            workingNumber = (workingNumber // factor)
      factor = factor+2
   return result

def sumPrimeFactorsOf(aNumber):
   sum = 0
   for each in primeFactorsOf(aNumber):
      sum = sum + each
   return sum

def isPalindrome(aNumber):
     
   list = []
   reverseString = ''
   for character in str(aNumber):
        list.append(character)
   list.reverse()
   for character in list:
      reverseString = reverseString + character
   return aNumber == int(reverseString) 
   
def findLargestPalindromeFrom(number1, number2):
   results = []
   factor1 = number1
   factor2 = number2
   largestResult = 0
   while factor1 > 0:
      result = 0
      factor2 = number2
      while result == 0 and(factor2 > 0):
         result = findLargestPalindrome(factor1,factor2,largestResult)
         if result > largestResult:
            largestResult = result
         factor2 = factor2 -1
      factor1 = factor1 -1
   return largestResult

def findLargestPalindrome(fixedNumber, variableNumber, upperLimit):
   result = 0
   product = fixedNumber * variableNumber
   variableFactor = variableNumber
   while result == 0 and(variableFactor > 0) and(product > upperLimit):
      product = fixedNumber * variableFactor
      if isPalindrome(fixedNumber * variableFactor):
         result = fixedNumber * variableFactor
      variableFactor = variableFactor -1
   return result

def smallestMultiple(range):
   result = len(range)
   while canBeDividedWithoutRemainderbyEachIn(result, range) == False:
      result = result + 1
   return result

def canBeDividedWithoutRemainderbyEachIn(number,aRange):
   reversedRange = range(aRange.stop,aRange.start,-1)
   for each in reversedRange:
      if number % each != 0:
         return False
   return True

def sumOfSquares(aRange):
   sum = 0
   for each in aRange:
      sum = sum + each * each
   return sum

def sumOfSquaresEnhanced(aRange):
#Sum of squares of n natural numbers formula: 12 + 22 + 32 + ... + n2 = [n(n+1)(2n+1)] / 6
   numberOfTerms = len(aRange)
   return numberOfTerms * (numberOfTerms +1) * (2 * numberOfTerms +1) / 6


def sumOfSquared(aRange):
   return sumOfIntegers(aRange)**2

def sumOfIntegers(aRange):
#The formula to calculate the sum of integers #is given as, S = n(a + l)/2, where, S is sum #of the consecutive integers n is number of #integers, a is first term and l is last term.
 
   firstTerm = aRange[0]
   lastTerm = aRange[-1]
   numberOfTerms = len(aRange)

   return int(numberOfTerms * (firstTerm + lastTerm) / 2)

def lastPrimeNumberInSequenceEndingWith(aNumber):
   lastPrimeNumber = 0
   sequenceCount = 1
   count = 1
   while sequenceCount < aNumber:
      if isPrime(count):
         lastPrimeNumber = count
         sequenceCount = sequenceCount + 1
      count = count + 2
   print(sequenceCount)
   return lastPrimeNumber

def flooredSquareRootOf(aNumber):
   import math
   return math.floor(math.sqrt(aNumber))

def isPrime(aNumber):
   if aNumber == 1:
      return False
   if aNumber < 4:
      return True
   if aNumber % 2 == 0:
      return False
   if aNumber < 9:
      return True
   if aNumber % 3 == 0:
      return False
   factor = 5
   while factor <= flooredSquareRootOf(aNumber):
      if aNumber % factor == 0:
         return False
      if aNumber % (factor + 2) == 0:
         return False
      factor = factor + 6
   return True

def productOfDigitsIn(aList):
   product = 1
   for number in aList:
      product = product * number
   return product

def convertIntegerToList(anInteger):
   return list(map(int, str(anInteger)))

def convertListToString(aList):
   result = ''
   for each in aList:
      result = result + (str(each))
   return result

def convertStringToListOfIntegers(aString):
   result = []
   for each in aString:
      result.append(int(each))
   return result
   
def sample1000digitNumber():
#with open('file_name.text') as file:
#some code here   
   file = open("1000DigitNumber.txt", "r")
   number = int(file.read())
   file.close()
   return number

def sample1000digitNumber2():
#with open('file_name.text') as file:
#some code here   
   with open("1000DigitNumber.txt") as file:
      number = int(file.read())
   return number

def sample20by20Grid():
   with open("20by20Grid.txt") as file:
      grid = twoDimensionalArrayFromString(file.read())
   return grid

def findAdjacentDigits(aNumber, aNumberOfAdjacentDigits):
   dictionary = {}
   startIndex = 0
   endIndex = aNumberOfAdjacentDigits
   integers = convertIntegerToList(aNumber)
   while endIndex < len(integers):
      slice = integers[startIndex:endIndex]
      dictionary.update({convertListToString(slice): productOfDigitsIn(slice)})
      startIndex = startIndex + 1
      endIndex = endIndex + 1
      result = sorted(dictionary.items(), key=lambda x:x[1])[-1][0]
   return convertStringToListOfIntegers(result) 
   
def sumOfPrimesBelow(aNumber):
   if aNumber <= 2:
      return 0
   sum = 2
   if aNumber % 2 == 0:
      count = aNumber - 1
   else:
      count = aNumber -2
   while count > 2:
      if isPrime(count):
         sum = sum + count
      count = count - 2
   return sum

def productOfPythagoranTripletWhereSumIs(aSum):
   triplet = createPythagoranTripletsWithSumUpTo(aSum)[aSum]
   result = 1
   for each in triplet:
      result = result * each
   return result  

def createPythagoranTripletsWithSumUpTo(aSum):
#It is easy to construct sets of Pythagorean Triples.
#When m and n are any two positive integers (m > n):
#a = m^2 − n^2
#b = 2mn
#c = m^2 + n^2
#Then a, b and c form a Pythagorean Triple. This is known as "Euclid's formula".
   a = 0
   b = 0
   c = 0
   m = 2
   n = 1
   largestM = 2
   result = {}
   while (a + b + c) != aSum:
      a = m**2 - n**2
      b = 2 * m * n
      c = m**2 + n**2
      result.update({a + b + c : [a,b,c]})
      if m - 1 == n:
         n = 1
         m = m + 1
      else:
         n = n + 1
#      print('n = ', str(n))
#      print('m = ', str(m))
#      print('result = ', str(result))
   return result

def twoDimensionalArrayFromString(aString):
   #string must contain rows of elements separated by spaces
   rows = []
   for eachLine in aString.split('\n'):
      row = []
      for eachCharacter in eachLine.split():
         row.append(int(eachCharacter))     
      rows.append(row)
   return rows

def greatestProductOf4AdjacentNumbersIn(aTwoDimensionalArray):
   return 0

def horizontalArraysIn(aTwoDimensionalArray):
   return aTwoDimensionalArray

def verticalArraysIn(aTwoDimensionalArray):
   result = []
   for count in range(len(aTwoDimensionalArray[0])):
      result.append([])
   for anArray in aTwoDimensionalArray:
      index = 0
      while index < len(anArray):
         result[index].append(anArray[index])
         index = index + 1
   return result

def diagonalArraysIn(aTwoDimensionalArray):
   result = []
   length = len(aTwoDimensionalArray[1])
   depth = len(aTwoDimensionalArray)

   #walk matrix from top left to bottom right.
   xCoordinate = 1
   yCoordinate = depth
   diagonalArray = []
   #keep going until the top right is reached
   #check if at bottom right corner
   while not(xCoordinate == length and yCoordinate == 1):
      diagonalArray.append([xCoordinate, yCoordinate])
      #check if there is another coordinate in the diagonal
      print('y= ', str(yCoordinate))
      print('x= ', str(xCoordinate))
      if xCoordinate + 1 <= length and yCoordinate - 1 >= 1:
         xCoordinate = xCoordinate + 1
         yCoordinate = yCoordinate - 1
      else:
         #move to next diagonal
      yCoordinate = yCoordinate + 1
   return diagonalArray

1,2
1,1 2,2
2,1


2 a  b
1 c  d
  1  2
def allXandYCoordinatesIn(aTwoDimensionalArray):
   #assumes array is equal in length and depth
   result = []
   xMax = len(aTwoDimensionalArray[1])
   yMax = len(aTwoDimensionalArray)
   for xCoordinate in range(1,xMax + 1):
      for yCoordinate in range(1,yMax + 1):
         result.append([xCoordinate, yCoordinate])
   return result
      
def greatestProductOf4AdjacentHorizontalNumbersIn(aTwoDimensionalArray):
   result = 0
   for eachArray in aTwoDimensionalArray:
      startIndex = 0
      endIndex = 4
      while endIndex <= len(eachArray):
         product = productOfDigitsIn(eachArray[startIndex:endIndex])
         if product > result:
            result = product
         startIndex = startIndex + 1
         endIndex = endIndex +1
   return result
                                     
def greatestProductOf4AdjacentVerticalNumbersIn(aTwoDimensionalArray):
   return 0

def greatestProductOf4AdjacentDiagonalNumbersIn(aTwoDimensionalArray):
   return 0