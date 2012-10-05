import gmpy
import bisect
import time
import itertools
import math

#def div1(x):
"""Helper fxn for solution 1:  checks whether a no. is divisible by 3 or 5"""
 # return x%3 == 0 or x%5 == 0

def fibNos():
  """Helper function for sol2: retuns a list of fib no.s """
  a, b = 0 , 1
  fibs = []
  while a < 4000000:
    fibs.append(b)
    a, b = b, a+b
  return fibs

def sol1():
  """Function to add all the integers divisible by 3 or 5 in range 1000."""
  return sum(filter(lambda x: x%3 == 0 or x%5 == 0,range(1000000)))

def sol2():
  """Function to find sum of even fibonacci no.'s below 4 million.

  This function uses the observation that the even no's  follow the
  sequence x+y, 3x+5y and so on in a fibonnace sequence of no's
  """
  a, b, sum = 1, 1, 0
  while sum < 4000000:
    sum += (a+b)
    a, b = a + 2*b, 2*a + 3*b
  return sum

def sol3(x):
  """ This is a lazy solution for getting largest prime factor of a no."""
  i = 2
  while x != 1:
    if x%i == 0:
      x /= i
    else:
      i += 1
  return i

def palindrome(num):
  return str(num) == str(num)[::-1]

def sol4():
  """Finding largest palindrome no. which is product of two 3-digit no.'s."""
  a, b = 999, 990
  max = 111111
  count = 0
  while b > 109:
    while a > 100 and a*b > 111111:
      count += 1
      a -= 1
      if palindrome(a*b):
	temp = a*b
	if max < temp:  
	  max = temp
	  break
    b -= 11
    a = 999
  print count
  return max

def sol5():
  """Finding smallest no. which evenly divides no.'s from 1 to 20."""
  allNos = range(21)
  result = 1
  for x in range(21):
    if allNos[x] > 1:
      result *= allNos[x]
      for j in range(2*x,21,x):
	allNos[j] /= allNos[x]
  return result

def sol6():
  """Difference between sum of squares and squares of sum."""
  squares = [ i*i for i in range(1,101)]
  singles = range(1,101)
  sumSq = reduce(lambda x,y: x+y, squares)
  sumSi = reduce(lambda x,y: x+y, singles)
  sqSingles = sumSi*sumSi
  return sqSingles-sumSq

def ssQ(n):
  """Returns sum of squares uptil n."""
  return (n*(n+1)*((2*n)+1))/6

def sumN(n):
  """Returns sum of numbers uptill n."""
  return (n*(n+1))/2

def sol6Alt():
  sumSq = ssQ(100)
  sum = sumN(100)
  sqSum = sum*sum
  return sqSum - sumSq

def isPrime(num):
  temp = 3
  while temp <= (int(math.sqrt(num))+1):
    if num % temp == 0:
      if temp != num:
	return False
      elif temp == num:
	return True
    else:
      temp += 2 
  return True

def sol7(n):
  """Returns nth prime no."""
  s = time.time()
  count = 2
  num = 3
  while count < n:
    num += 2
    if(isPrime(num)):
      count += 1
  print time.time() - s
  return num

def sol8():
  """Greatest product of 5 consecutive digits in given no."""

  number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

  array = list(number)
  limit = range(1000)
  i = 0
  maxPr = 0
  while i < len(limit):
    product = 1
    for x in range(i, i+5):
      if x >= len(limit):
	return maxPr
      if array[x] == '0':
	break
      product *= int(array[x])
    if(maxPr < product):
      maxPr = product
    i += 1
  return maxPr

def sol9():
  """Finding pythagorean triplet for a+b+c=1000."""

  #We know that ab = 1000(a+b-500) that means a+b > 500
  abc = [a*b*c for a in range(500) for b in range(500) for c in range(500)
      if c*c == (a*a) + (b*b) and a + b + c == 1000]
  return set(abc)

def sol10(n):
  """Sum of all primes below n."""
  nums = range(2,n+1)
  p = 1
  primes = [2]
  #Find all primes upto n
  while p < n:
    p += 2
    if(p < n and isPrime(p)):
      primes.append(p)
#  print primes
  return reduce(lambda x, y: x+y, primes)

def getMaxProductH(matrix):
  """Returns the maximum horizontal product in the matrix."""
  maxPr = 0
  for i in range(len(matrix)):
    for j in range(i,len(matrix[0])-3):
      temp = reduce(lambda x,y: x*y, matrix[i][j:j+4])
      if temp > maxPr:
	maxPr = temp
  return maxPr

def getMaxProductV(matrix):
  """Returns the maximum vertical product for the matrix."""
  maxPr = 0
  for i in range(len(matrix)):
    tempLi = [row[i] for row in matrix]
    for j in range(i, len(matrix[0])-3):
      temp = reduce(lambda x,y: x*y, tempLi[j:j+4])
      if temp > maxPr:
	maxPr = temp
  return maxPr

def getMaxProductD(matrix):
  """Returns the maximum diagonal product for the matrix."""
  maxPr = 0
  for i in range(len(matrix)-3):
    for j in range(len(matrix[0])-3):
      tempL = tempR = temp = 1
      for x in range(4):
	tempL *= matrix[i+x][j+x]
	tempR *= matrix[i+x][20-j-x-1]
      temp = max(tempL, tempR)
      if temp > maxPr:
	maxPr = temp
  return maxPr

def sol11():
  """Greatest product of four adjacent numbers in any direction."""
  #Read file into n * n matrix
  f = open('q11','r')
  """mStr = f.readlines()
  matrix = []
  for i in range(len(mStr)):
    st = mStr[i].rstrip('\n')
    temp = [int(x) for x in st.split(' ')]
    matrix.append(temp)
"""
  matrix = [ map(int, line.rstrip('\n').split(' ')) for line in f]
  #get max sum horizontally
  hor = getMaxProductH(matrix)
  #get max sum vertically
  ver = getMaxProductV(matrix)
  dia = getMaxProductD(matrix)
  maxPr = max(hor,ver,dia)
  return maxPr
#get max diagonally
  #return max of 3

def getDivisors(num):
  """Gets the number of divisors for the number."""
  #Start with 2 for num and 1
  numDivisors = 2 
  for i in range(2,(int(math.sqrt(num))+1)):
    if(num%i == 0):
      numDivisors += 2
  if gmpy.is_square(num):
    numDivisors -= 1
  return numDivisors

def sol12(n):
  """Gets the first triangle number with more than 500 divisors."""
  #for each number
  num = 1
  s = time.time()
  for i in itertools.count(3,1):
    num = (i*(i+1))/2
    numDivisors = getDivisors(num)
    #get numdivisors for each i
    #break when numdivisors > 500
   # print num, numDivisors
    if numDivisors > n:
      break
  print time.time() - s
  return num

def getSumList(matrix):
  """Creates and returns a list with sum of all the numbers represented by
  matrix."""
  sumMa = 0
  carry = 0
  sumList = []
  for i in range(len(matrix[0])):
    tempLi = [row[len(matrix[i])-i-1] for row in matrix]
    sumMa = ((reduce(lambda x,y: x+y, tempLi))+carry)
    carry = sumMa / 10
    sumList.append( sumMa % 10)
  sumList.append(carry)
  return sumList

def sol13(n):
  """Gets the first n digits of the sum of numbers given in the file"""
  f = open('q13','r')
  matrix = [ [int(i) for i in line.rstrip('\n')] for line in f]
  sumList = getSumList(matrix)
  sumStr = [ str(i) for i in sumList]
  strSum = reduce(lambda x,y: x+y, sumStr)
  return strSum[len(strSum)-1:len(strSum)-n-1:-1]

def sol14(n):
  """Gets the starting number under n which produces longest chain."""
  # Create tree according to the rules for different possibilities.
  # Find max hieght of the tree and its leaf element
  returnNo = 0
  maxLen = 0
  countMap = {}
  countMap[1] = 1
  start = 2
  while start < n :
    startNo = start
    count = 0
    while startNo != 1:
      if start in countMap:
	count += countMap[start]
	break
      if startNo % 2 == 0:
	startNo /= 2
      else:
	startNo = (3*startNo) + 1
      count += 1
    countMap[start] = count
    if count > maxLen:
      maxLen = count
      returnNo = start
    start += 1
  return returnNo

counts = {}
def getRoutes( startX, startY, finalX, finalY, count):
  """Recursive solution to get the no. of routes. """
  global counts
  point = (startX, startY)
  if point in counts:
    countAhead = counts[point] 
    return count+countAhead
  if startX == finalX and startY == finalY:
    count += 1
    return count
  if startX != finalX:
    count = getRoutes(startX+1,startY, finalX, finalY,count)
  if startY != finalY:
    count = getRoutes(startX,startY+1, finalX, finalY,count)
  return count

def sol15(x,y):
  """Gets the no. of routes without backtracking for an xXy grid."""
  count = 0
  global counts
  for i in range(x-1,-1,-1):
    for j in range(y-1,-1,-1):
      count = 0
      point = (i, j)
      counts[point] = getRoutes(i,j,x,y,count)
  return getRoutes(0,0,x,y,count)

def sol16(num):
  """Gets the sum of digits for the given number."""
  sumDigits = 0
  while num != 0:
    sumDigits += num%10
    num /= 10
  return sumDigits

def getNoInWords(n):
  """Returns no. in words."""


def sol17(n):
  """Gets the number of letters in number words."""
  numWords = {}
  numWords[1] = 3
  numWords[2] = 3
  numWords[3] = 5
  numWords[4] = 4
  numWords[5] = 4
  numWords[6] = 3
  numWords[7] = 5
  numWords[8] = 5
  numWords[9] = 4
  numWords[10] = 3
  numWords[11] = 6
  numWords[12] = 6
  numWords[13] = 8
  numWords[14] = 8
  numWords[15] = 7
  numWords[16] = 7
  numWords[17] = 9
  numWords[18] = 8
  numWords[19] = 8
  numWords[20] = 6
  numWords[30] = 6
  numWords[40] = 5
  numWords[50] = 5
  numWords[60] = 5
  numWords[70] = 7
  numWords[80] = 6
  numWords[90] = 6
  numWords[100] = 7
  numWords[1000] = 11
  numLetters = 0
  for i in range(1,n+1):
    #Case 1 to 20 and multiples of 10 less than 100
    toBeAdded = 0
    if i < 100:
      if i<20 or i%10 == 0 :
	toBeAdded += numWords[i]
      #Otherwise
      else:
	toBeAdded += numWords[i%10]+numWords[i-(i%10)]
    else:
      # add 3 for and
      #Make one hundred
      temp = i
      toBeAdded += (numWords[100] + numWords[temp/100])
      if i % 100 != 0:
	toBeAdded += 3 
      else:
	numLetters += toBeAdded
	continue

      # for 1 to 20 and multiples of 10
      if i%100 < 20 or i%10 == 0 :
	toBeAdded += numWords[i%100]
      # for others
      else:
      # Add last digit
	toBeAdded += numWords[i%10]
	# Create last two digit word
	temp -= (temp%10)
	toBeAdded += numWords[temp%100]
    numLetters  += toBeAdded
  return numLetters

def getMaxSum(listOfLists,level, pos, size):
  if level == size:
    return 0 
  maxSum = listOfLists[level][pos] 
  leftSum = getMaxSum(listOfLists, level+1, pos, size)
  rightSum = getMaxSum(listOfLists,level+1, pos+1, size)
  maxSum += max(leftSum,rightSum)
  return maxSum

def getMaxSumEff(listOfLists,size):
  for i in range(size-1, 0 , -1):
    for j in range(i):
      listOfLists[i-1][j] += max(listOfLists[i][j],listOfLists[i][j+1])
  return listOfLists[0][0]

def sol18():
  """Gets the maximum total from top to bottom of a triangle."""
  s = time.time()
  f = open('triangle.txt','r')
  listOfLists = [ map(int, line.rstrip('\n').split(' ')) for line in f]
  size = len(listOfLists)
  #print getMaxSum(listOfLists,0,0,size)
  print getMaxSumEff(listOfLists, size)
  print time.time()-s

def calculateDOW(year, month, lastMD):
  """ Gets the 1st day of that month and year."""
  
  thirtyDays = [1,2,4,6,8,9,11]
  thirtyOnedays = [5,7,10,12]        
  
  if month in thirtyDays:
    nextDay = lastMD + 3
  """ if month == 4 or month == 6 or month == 9 or month == 11:
	nextDay = lastMD + 3"""
  
  if month in thirtyOnedays:
    nextDay = lastMD + 2
  
  if month == 3:
    if year % 4 == 0:
      nextDay = lastMD + 1
    else:
      nextDay = lastMD 
  return nextDay


def sol19(n):
  """Gets the no. of Sundays that fell on 1st of month in the twetieth century."""
  numSundays = 0
  tempDay = 5
  for i in range(1,n+1):
    for j in range(1,13):
      print i
      tempDay = calculateDOW(i,j, tempDay) % 7
      if tempDay == 6:
	numSundays += 1            
  return numSundays 

def sol20(n):
  """Returns the sum of digits for n!."""
  for i in range(1,n):
    n *= i
  #Another way
  #reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, n)))])
  return sol16(n)

def getProperDivisors(n):
  """Returns all the proper divisors of n."""
  divisors = [1]
  for i in range(2,(int(math.sqrt(n))+1)):
    if(n%i == 0):
      divisors.append(i)
      divisors.append(n/i)
  sumDivisors = reduce(lambda x,y: x+y, set(divisors))
  return sumDivisors
  
def sol21(n):
  """Returns sum of all amicable numbers below n."""
  s = time.time()
  sumList = []
  for i in range(n):
    sumList.append(getProperDivisors(i))
  normalList = [i for i in range(n)]
  amicableSum = 0
  #print sumList
  #print normalList
  #print len(sumList)
  for i in range(n):
    #print i
    if sumList[i] >= n:
      continue
    #print normalList[i],sumList[i]
    if sumList[i] != 1 and i != sumList[i] and i == sumList[sumList[i]]:
      amicableSum += sumList[i]
      #print i,sumList[i]
  print time.time() - s
  return amicableSum

def getWordValue(wordNo, word):
  """Returns the value of word/name in the name list given for q22."""
  sumWord  = reduce(lambda x,y: x+y, [(ord(i)-ord('A')+1) for i in word])
  return wordNo*sumWord

def sol22():
  """Returns the total of all name scores in the file."""
  s = time.time()
  f = open('names.txt','r')
  temp = [ line.split(',') for line in f]
  nameList = [ word.lstrip('"').rstrip('"') for word in temp[0]]
  nameList.sort();
  #print nameList
  totalSum = 0
  listSize = len(nameList)
  for i in range(listSize):
    totalSum += getWordValue(i+1, nameList[i])
  print time.time() - s
  return totalSum

def sol23():
  """Returns the sum of all the numbers which cannot be written as sum of two
  abundant numbers."""
  s = time.time()
  abunNums = [ x for x in range(12, 20161) if x < getProperDivisors(x) ] 
  #print abunNums
  limit = 20161
  possibleSums = set([])
  index = 0
  sizeAb = len(abunNums)
  for x in abunNums:
    for i in range(index, sizeAb):
      temp = x + abunNums[i]
      if temp > limit:
	break
      possibleSums.add(temp)
    index += 1
  #print possibleSums
  nonSums = set([x for x in range(1,20162) if x not in possibleSums])
  print reduce(lambda x,y: x+y, nonSums)
  print time.time() - s

def permute( number, numList, count, used, fixedPos):
  """Recursive function to get all permutations of numList."""
  if fixedPos == len(numList):
    #print number
    count += 1
    #print count
    return count
  for i in range(0, len(numList)):
    if used[i]:
      continue
    number.append(numList[i])
    used[i] = True
    count = permute(number, numList, count,used,fixedPos+1)
    if count == 1000000:
      return count
    used[i] = False
    #print count, number
    number.pop()
  return count


def sol24():
  """Returns the millionth lexicographical permutation of digits 0 to 9"""
  count = 0
  numList = [str(i) for i in range(10)]
  used = [False for i in range(10)]
  index = 0
  number = []
  permute(number, numList, count, used, index)
  return reduce(lambda x,y: x+y, number)

def fibo(a,b):
  """Returns the next fibonacci number."""
  return b,a+b

def sol25(n):
  """Returns the first fibonacci term to contain n digits."""
  a,b = 1,1
  index = 2
  while True:
    a,b = fibo(a,b)
    index += 1
    if len(str(b)) == n:
      return index

def getNumRecDigits(num):
  """Returns the number or recurring digits in 1/num."""
  numerator = 1000
  quotients = []
  remainders = []
  rem = numerator % num 
  if rem == 0:
    return 0
  rem = 10
  while rem != 0:
    """Get quotient and remainder when numer*10 is divided by num.
    if result in dictionary with same remainder get count from there
    to this point.
    """
    quo = rem/num
    ind = [i for i,x in enumerate(quotients) if x == quo]
    quotients.append(quo)
    rem = rem % num
    for i in ind:
      if remainders[i] == rem:
	return len(remainders) - i
    remainders.append(rem)
    rem *= 10
  return 0

def sol26():
  """Returns the value d < 1000 for which 1/d contains longest recurring
  cycle."""
  value = 0
  currMax = 0
  s = time.time()
  for i in range (2,1000):
    numDigits = getNumRecDigits(i)
    if numDigits > currMax:
      value = i
      currMax = numDigits
  print time.time() - s
  return value

def sol27():
  """Returns product of coefficients of prime number generator equation."""
  s = time.time()
  primeNo = [i for i in range(1,1000,2) if isPrime(i)]
  lower , upper = 41, 997
  a,b,n = 0,0,0
  maxLength = 0
  for i in range(-999,1001,2):
    for j in primeNo:
      if j < 41:
	continue
      x = 0
      while isPrime( math.fabs((x*x) + (i*x) + j)):
	x += 1
      if x > n:
	a, b, n = i, j, x
  print time.time() - s
  return a*b

def sol28(n):
  """Returns sum of numbers on diagonals in nXn spiral matrix."""
  s = time.time()
  startPos = n/2
  num = 1
  matrix = []
  for i in range(n):
    temp = [0 for j in range(n)]
    matrix.append(temp)
  matrix[startPos][startPos] = num
  startPosX, startPosY = startPos, startPos
  maxNum = n*n
  i = 1
  #print maxNum
  while num < maxNum:
    i += 1
    for j in range(1,i):
      startPosY += 1
      num += 1
      matrix[startPosX][startPosY] = num
      if num == maxNum:
       break
    if num == maxNum:
      break
    for j in range(1,i):
      num += 1
      startPosX += 1
      matrix[startPosX][startPosY] = num 
    
    i += 1
    for j in range(1,i):
      startPosY -= 1
      num += 1
      matrix[startPosX][startPosY] = num 
    for j in range(1,i):
      num += 1
      startPosX -= 1
      matrix[startPosX][startPosY] = num 
  #print matrix
  diag1 = reduce( lambda x,y: x+y, [matrix[i][i] for i in range(n)])
  diag2 = reduce( lambda x,y: x+y, [matrix[n-i-1][i] for i in range(n)])
  print time.time() - s
  return diag1+diag2-1

def sol29(a,b):
  """Returns distinct terms in sequence generated by a**b from a to b."""
  return len(set([i**j for i in range(2,a) for j in range(2,b)]))

def sol30():
  """Returns sum of all numbers that can be written as sum of fifth powers
  of their digits."""
  nums = []
  s = time.time()
  for i in itertools.count(243,1):
    if i >= 354294:#(9**5)*6
      break
    temp = i
    sumDig = 0
    dig = temp%10
    while temp > 0:
      sumDig += dig**5
      temp /= 10
      dig = temp%10
    """for a in str(i):
      sumDig += (int(a)**5)"""
    if sumDig == i:
      nums.append(i)
  print time.time() - s
  return reduce(lambda x,y: x+y, nums)
