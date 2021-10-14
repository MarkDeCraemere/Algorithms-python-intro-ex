from mersenne import generatePotentialMP, isPrime

def test_generatePotentialMP():
  assert(generatePotentialMP(3) == 7)
  assert(generatePotentialMP(2) == 3)
  assert(generatePotentialMP(1) == 1)

def test_isPrime():
  assert(isPrime(7))
  assert(isPrime(2))
  assert(isPrime(11))
  assert(isPrime(1) == False)
  assert(isPrime(4) == False)
