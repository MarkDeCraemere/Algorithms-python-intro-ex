def generatePotentialMP(n):
  return 2**n - 1

def isPrime(x):
  if x < 2:
    return False
  for i in range(2,x//2+1):
    if x % i == 0:
      return False
  return True

mpFound = 0
counter = 0
while mpFound < 5:
  potential = generatePotentialMP(counter)
  if isPrime(potential):
    mpFound += 1
    print(potential)
  counter += 1


#for i in range (1,10):
#    if isPrime(generatePotentialMP(i)):
#        print(generatePotentialMP(i))